"""
cPanel / Passenger entry point.

cPanel's "Setup Python App" looks for a variable named `application`
in this file. Nothing else here needs changing.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from app import app as application  # noqa: E402,F401
