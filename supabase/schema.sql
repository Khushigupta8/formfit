-- FormFit Pro database. Paste into Supabase > SQL Editor > New query > Run.
-- Safe to run again: it only creates what's missing.
--
-- Who can do what:
--   profiles  users can read their own row; only the server (service role,
--             i.e. api/*.py) changes subscription fields.
--   plans     users read and delete their own saved plans; the server writes
--             them (the generator lives in api/plan.py).
--   logs      progress entries. Users manage their own, and adding new ones
--             needs an active Pro subscription, checked here in the database
--             so it can't be bypassed from the browser.

create table if not exists public.profiles (
  id uuid primary key references auth.users (id) on delete cascade,
  email text,
  plan text,                               -- 'monthly' | 'yearly'
  status text,                             -- Razorpay subscription status
  razorpay_subscription_id text,
  current_period_end timestamptz,          -- Pro until this moment (+1 day grace)
  cancel_at_period_end boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.plans (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users (id) on delete cascade,
  inputs jsonb not null,
  plan jsonb not null,
  created_at timestamptz not null default now()
);
create index if not exists plans_user_idx on public.plans (user_id, created_at desc);

create table if not exists public.logs (
  id bigint generated always as identity primary key,
  user_id uuid not null default auth.uid() references auth.users (id) on delete cascade,
  kind text not null check (kind in ('weight', 'waist', 'lift')),
  logged_on date not null default current_date,
  value numeric not null check (value > 0 and value < 1000),   -- kg or cm
  reps int check (reps is null or (reps > 0 and reps < 100)),  -- lifts only
  exercise text check (exercise is null or length(exercise) <= 60),
  note text check (note is null or length(note) <= 200),
  created_at timestamptz not null default now()
);
create index if not exists logs_user_idx on public.logs (user_id, kind, logged_on);

-- Same rule as is_pro() in api/_lib.py.
create or replace function public.is_pro(uid uuid)
returns boolean language sql stable security definer set search_path = public as $$
  select exists (
    select 1 from profiles
    where id = uid
      and coalesce(status, '') <> 'halted'
      and current_period_end + interval '1 day' > now()
  );
$$;

-- A profile row for every new sign-up.
create or replace function public.handle_new_user()
returns trigger language plpgsql security definer set search_path = public as $$
begin
  insert into profiles (id, email) values (new.id, new.email) on conflict (id) do nothing;
  return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

alter table public.profiles enable row level security;
alter table public.plans enable row level security;
alter table public.logs enable row level security;

drop policy if exists "own profile" on public.profiles;
create policy "own profile" on public.profiles
  for select using (auth.uid() = id);

drop policy if exists "read own plans" on public.plans;
create policy "read own plans" on public.plans
  for select using (auth.uid() = user_id);
drop policy if exists "delete own plans" on public.plans;
create policy "delete own plans" on public.plans
  for delete using (auth.uid() = user_id);

drop policy if exists "read own logs" on public.logs;
create policy "read own logs" on public.logs
  for select using (auth.uid() = user_id);
drop policy if exists "add logs when pro" on public.logs;
create policy "add logs when pro" on public.logs
  for insert with check (auth.uid() = user_id and public.is_pro(auth.uid()));
drop policy if exists "delete own logs" on public.logs;
create policy "delete own logs" on public.logs
  for delete using (auth.uid() = user_id);
