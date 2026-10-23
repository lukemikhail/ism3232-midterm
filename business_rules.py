SHORT_STAY_NIGHTS = 4
STANDARD_DISCOUNT = 0.06
LONG_STAY_NIGHTS = 14
LONG_STAY_DISCOUNT = 0.18
CLEANING_FEE_THRESHOLD = 300.00
CLEANING_FEE = 40.00
CREDIT_CHECK_THRESHOLD = 2000.00
WELCOME_PACKAGE_MIN_NIGHTS = 5
WELCOME_PACKAGE_MIN_TOTAL = 1000.00

def calculate_room_cost(nightly_rate: float, nights: int) -> float:
    """Calculate room cost before discounts."""
    return nightly_rate * nights