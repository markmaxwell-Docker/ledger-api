from decimal import Decimal

DAILY_LIMIT = Decimal("10000.00")
FEE_RATE = Decimal("0.0025")


class InvalidTransfer(ValueError):
    pass


class LimitExceeded(InvalidTransfer):
    pass


def apply_fee(amount: Decimal) -> Decimal:
    """Return the amount plus Fernhill's transfer fee, rounded to cents."""
    return (amount * (1 + FEE_RATE)).quantize(Decimal("0.01"))


def validate_transfer(amount: Decimal, sent_today: Decimal = Decimal("0")) -> None:
    """Reject transfers that break Fernhill's rules."""
    if amount <= 0:
        raise InvalidTransfer("amount must be positive")
    # FP-142: enforce DAILY_LIMIT using sent_today.
