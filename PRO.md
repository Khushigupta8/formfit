# FormFit Pro: setup

FormFit Pro is the paid tier: a personal diet + training plan generator,
progress tracking (weight, waist, lifts), saved/printable plans and no ads.
The free site is unchanged and still fully static.

    /pro          pricing page (indexed, in the sitemap)
    /account      sign in (email link), subscribe, cancel      (noindex)
    /dashboard    plan generator + progress, Pro only          (noindex)

    api/me.py                GET  status of the signed-in user
    api/subscribe.py         POST create a Razorpay subscription
    api/verify.py            POST check the payment signature after checkout
    api/cancel.py            POST cancel at the end of the paid period
    api/plan.py              POST generate + save a plan (Pro only)
    api/razorpay_webhook.py  POST renewals, failures, cancellations
    api/_lib.py, _plan.py    shared code (the "_" keeps Vercel from serving them)
    supabase/schema.sql      tables + row level security
    static/js/pro.js         everything in the browser

Until SUPABASE_URL and SUPABASE_ANON_KEY are filled in, /account and
/dashboard show "Accounts aren't switched on yet" and nothing else changes.

## 1. Supabase (accounts + database), free tier is fine

1. supabase.com > New project (region: Mumbai).
2. SQL Editor > New query > paste `supabase/schema.sql` > Run.
3. Authentication > URL Configuration:
   - Site URL: `https://www.formfit.in`
   - Redirect URLs: `https://www.formfit.in/**` and `http://127.0.0.1:5000/**`
4. Authentication > Emails: the built-in sender is rate limited (a few emails
   an hour). Before launch, set up custom SMTP (the same Gmail App Password
   the contact form uses works).
5. Optional: Authentication > Providers > Google, then `GOOGLE_LOGIN = True`
   in app.py.
6. Project settings > API: copy the Project URL and the `anon` public key into
   `SUPABASE_URL` / `SUPABASE_ANON_KEY` in app.py. Copy the `service_role`
   key for step 3 below. Never put service_role in app.py.

## 2. Razorpay (payments)

1. Sign up, finish KYC, and enable Subscriptions (Razorpay may need to
   switch it on for your account; ask support if it's not in the menu).
2. Work in Test mode first. Subscriptions > Plans > Create:
   - Monthly: period monthly, interval 1, Rs 99
   - Yearly: period yearly, interval 1, Rs 799
   If you change prices, also change `PRO_PRICES` in app.py.
3. Settings > API Keys > Generate test key.
4. Settings > Webhooks > Add:
   - URL `https://www.formfit.in/api/razorpay_webhook`
   - choose a secret
   - events: every `subscription.*` event

## 3. Vercel environment variables

Project > Settings > Environment Variables, then redeploy:

    SUPABASE_URL               https://xxxx.supabase.co
    SUPABASE_SERVICE_ROLE_KEY  service_role key
    RAZORPAY_KEY_ID            rzp_test_... (rzp_live_... at launch)
    RAZORPAY_KEY_SECRET
    RAZORPAY_WEBHOOK_SECRET
    RAZORPAY_PLAN_MONTHLY      plan_...
    RAZORPAY_PLAN_YEARLY       plan_...

For local testing, put the same lines in `.env.local` (gitignored);
`python app.py` reads it. Webhooks can't reach localhost, so test those on
a Vercel preview deploy.

## 4. Test before going live

With test keys (Razorpay test card 4111 1111 1111 1111, any future date, any
CVV; or UPI id `success@razorpay`):

- [ ] Sign in by email link on /account
- [ ] Subscribe monthly: checkout opens, the page flips to "FormFit Pro"
- [ ] Supabase > profiles row shows status active and a current_period_end
- [ ] Ads disappear on calculator pages (same browser)
- [ ] /dashboard: build a plan, reload, it's in "Saved plans"; print works
- [ ] Log weight 3 times on different dates: chart and trend appear
- [ ] Log a lift: shows under Best lifts; delete an entry
- [ ] Cancel on /account: still Pro, message shows the end date
- [ ] Razorpay > Webhooks shows 200 responses
- [ ] Sign in with a second, free account: /dashboard shows the upsell, and
      /api/plan answers 402

Then switch to live keys and live plan ids in Vercel, add the webhook again in
Live mode, and redeploy.

## How it decides who is Pro

`profiles.current_period_end` + 1 day grace, unless the status is `halted`
(renewals failed). The same rule is in `is_pro()` in api/_lib.py and in
supabase/schema.sql. The webhook keeps it up to date; api/verify.py sets it
straight after checkout so people don't wait. Pro data rules are enforced on
the server and in the database. The browser's `ff_pro` value only decides
whether ads load.
