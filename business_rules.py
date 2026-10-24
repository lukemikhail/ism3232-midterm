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
    """Calculate room cost before discounts"""
    return nightly_rate * nights


def get_stay_discount(nights: int, corporate: bool = False) -> float:
    """get the discount for your stay"""
    if nights >= LONG_STAY_NIGHTS:
        return LONG_STAY_DISCOUNT
    if nights >= SHORT_STAY_NIGHTS or corporate:
        return STANDARD_DISCOUNT
    return 0.0


def calculate_stay_total(nightly_rate: float, nights: int, corporate: bool = False) -> float:
    """Get the total cost of the stay"""
    room_cost = calculate_room_cost(nightly_rate, nights)
    discount = get_stay_discount(nights, corporate)
    discounted_cost = room_cost * (1 - discount)

    if discounted_cost <= CLEANING_FEE_THRESHOLD:
        discounted_cost += CLEANING_FEE

    return discounted_cost


def requires_credit_check(total: float) -> bool:
    """Check for credit check"""
    return total >= CREDIT_CHECK_THRESHOLD


def gets_welcome_package(nights: int, total: float) -> bool:
    """Check if guest gets a welcome package."""
    return nights > WELCOME_PACKAGE_MIN_NIGHTS and total >= WELCOME_PACKAGE_MIN_TOTAL


def total_reserved(stays: list) -> float:
    """Add up the total for all stays."""
    total = 0.0

    for stay in stays:
        total += calculate_stay_total(
            stay["nightly_rate"],
            stay["nights"],
            stay.get("corporate", False)
        )

    return total


def largest_stay(stays: list) -> str:
    """Find the guest with the biggest stay."""
    largest_guest = ""
    largest_total = -1.0

    for stay in stays:
        stay_total = calculate_stay_total(
            stay["nightly_rate"],
            stay["nights"],
            stay.get("corporate", False)
        )

        if stay_total > largest_total:
            largest_total = stay_total
            largest_guest = stay["guest"]

    return largest_guest


def format_stay_line(guest: str, total: float, credit_check: bool, welcome_package: bool) -> str:
    """Format the stay information into one line."""
    credit = "yes" if credit_check else "no"
    welcome = "yes" if welcome_package else "no"
    return f"{guest}: ${total:.2f} | credit check: {credit} | welcome package: {welcome}"