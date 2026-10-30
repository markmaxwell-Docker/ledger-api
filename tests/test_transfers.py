import sys
import unittest
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "vendor"))

import fastfixtures  # noqa: E402
from ledger import DAILY_LIMIT, InvalidTransfer, LimitExceeded, apply_fee, validate_transfer  # noqa: E402


class TransferTests(unittest.TestCase):
    def setUp(self):
        self.account = fastfixtures.make_account(balance="25000.00")

    def test_fee_is_rounded_to_cents(self):
        self.assertEqual(apply_fee(Decimal("100.00")), Decimal("100.25"))

    def test_rejects_zero_amount(self):
        with self.assertRaises(InvalidTransfer):
            validate_transfer(Decimal("0"))

    def test_daily_limit_blocks_overage(self):
        with self.assertRaises(LimitExceeded):
            validate_transfer(Decimal("2500.00"), sent_today=Decimal("8000.00"))

    def test_daily_limit_allows_exact_limit(self):
        validate_transfer(Decimal("2000.00"), sent_today=DAILY_LIMIT - Decimal("2000.00"))


if __name__ == "__main__":
    unittest.main()
