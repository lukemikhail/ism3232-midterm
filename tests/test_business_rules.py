import business_rules

def test_calculate_room_cost():
    assert business_rules.calculate_room_cost(100.0, 3) == 300.0
    assert business_rules.calculate_room_cost(150.0, 5) == 750.0

def test_calculate_stay_total():
    assert business_rules.calculate_stay_total(100.0, 3, False) == 340.0
    assert business_rules.calculate_stay_total(150.0, 5, True) == 705.0

def test_requires_credit_check():
    assert business_rules.requires_credit_check(2500.0) == True
    assert business_rules.requires_credit_check(1500.0) == False


def test_credit_check_threshold():
    assert business_rules.requires_credit_check(2000.0) == True


def test_credit_check_below_threshold():
    assert business_rules.requires_credit_check(1999.99) == False

def test_gets_welcome_package():
    assert business_rules.gets_welcome_package(6, 1200.0) == True
    assert business_rules.gets_welcome_package(4, 800.0) == False


def test_welcome_package_at_night_limit():
    assert business_rules.gets_welcome_package(5, 1200.0) == False


def test_welcome_package_at_total_limit():
    assert business_rules.gets_welcome_package(6, 1000.0) == True
    assert business_rules.gets_welcome_package(6, 999.99) == False


def test_get_stay_discount():
    assert business_rules.get_stay_discount(5, False) == business_rules.STANDARD_DISCOUNT
    assert business_rules.get_stay_discount(15, False) == business_rules.LONG_STAY_DISCOUNT
    assert business_rules.get_stay_discount(3, True) == business_rules.STANDARD_DISCOUNT
    assert business_rules.get_stay_discount(2, False) == 0.0


def test_get_stay_discount_at_4_nights():
    assert business_rules.get_stay_discount(4, False) == business_rules.STANDARD_DISCOUNT


def test_long_stay_discount_at_14_nights():
    assert business_rules.get_stay_discount(14, False) == business_rules.LONG_STAY_DISCOUNT

def test_no_discount_under_four_nights():
    assert business_rules.get_stay_discount(3, False) == 0.0


def test_total_reserved():
    stays = [
        {"guest": "Kessler", "nightly_rate": 110.00, "nights": 2, "corporate": False},
        {"guest": "Lindqvist", "nightly_rate": 150.00, "nights": 2, "corporate": True},
        {"guest": "Moreno", "nightly_rate": 125.00, "nights": 6, "corporate": False},
    ]
    total = business_rules.total_reserved(stays)
    assert total == business_rules.calculate_stay_total(110.00, 2, False) + business_rules.calculate_stay_total(150.00, 2, True) + business_rules.calculate_stay_total(125.00, 6, False)


def test_largest_stay():
    stays = [
        {"guest": "Kessler", "nightly_rate": 110.00, "nights": 2, "corporate": False},
        {"guest": "Lindqvist", "nightly_rate": 150.00, "nights": 2, "corporate": True},
        {"guest": "Moreno", "nightly_rate": 125.00, "nights": 6, "corporate": False},
    ]
    largest = business_rules.largest_stay(stays)
    assert largest == "Moreno"  # Assuming Moreno has the largest stay based on the provided data


def test_largest_stay_with_tie():
    stays = [
        {"guest": "Kessler", "nightly_rate": 100.00, "nights": 2, "corporate": False},
        {"guest": "Moreno", "nightly_rate": 100.00, "nights": 2, "corporate": False},
    ]
    largest = business_rules.largest_stay(stays)
    assert largest == "Kessler"


def test_largest_stay_with_empty_list():
    stays = []
    largest = business_rules.largest_stay(stays)
    assert largest == ""  # Assuming the function returns None for an empty list


def test_total_reserved_with_empty_list():
    stays = []
    total = business_rules.total_reserved(stays)
    assert total == 0.0  # Assuming the function returns 0 for an empty list


def test_format_stay_line():
    line = business_rules.format_stay_line("Kessler", 340.0, True, False)
    assert line == "Kessler: $340.00 | credit check: yes | welcome package: no"

def test_cleaning_fee_applied():
    # Test that cleaning fee is applied when discounted cost is below threshold
    total = business_rules.calculate_stay_total(50.0, 1, False)  # 50 * 1 = 50, below threshold
    assert total == 50.0 + business_rules.CLEANING_FEE  # Cleaning fee should be added


def test_cleaning_fee_not_applied():
    # Test that cleaning fee is not applied when discounted cost is above threshold
    total = business_rules.calculate_stay_total(350.0, 1, False)  # 350 * 1 = 350, above threshold
    assert total == 350.0  # No cleaning fee should be added