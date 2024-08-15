from decimal import Decimal

diff_d = Decimal("10_000_000_000.2") - Decimal("10_000_000_000")
print(diff_d - Decimal("0.2"))
