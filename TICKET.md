# FP-142: Enforce the daily transfer limit

Customers can currently send any amount in a day. Compliance requires a daily
limit of 10,000.00 per account.

Acceptance criteria:
- `validate_transfer` raises `LimitExceeded` when the new transfer would take
  the account's total for the day above `DAILY_LIMIT`.
- Transfers that land exactly on the limit are allowed.
- The existing tests keep passing, and `test_daily_limit_*` pass.
