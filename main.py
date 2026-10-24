import business_rules

stays = [
    {"guest": "Kessler", "nightly_rate": 110.00, "nights": 2, "corporate": False},
    {"guest": "Lindqvist", "nightly_rate": 150.00, "nights": 2, "corporate": True},
    {"guest": "Moreno", "nightly_rate": 125.00, "nights": 6, "corporate": False},
    {"guest": "Nakata", "nightly_rate": 140.00, "nights": 20, "corporate": False},
    {"guest": "Osei", "nightly_rate": 95.00, "nights": 15, "corporate": True},
    {"guest": "Petrov", "nightly_rate": 200.00, "nights": 5, "corporate": False},
    {"guest": "Quinn", "nightly_rate": 180.00, "nights": 6, "corporate": False},
    {"guest": "Rahman", "nightly_rate": 260.00, "nights": 10, "corporate": True},
]

print("Seabreeze Inn - Stay Report")

for stay in stays:
    total = business_rules.calculate_stay_total(
        stay["nightly_rate"], stay["nights"], stay["corporate"]
    )

    credit = business_rules.requires_credit_check(total)
    welcome = business_rules.gets_welcome_package(stay["nights"], total)

    line = business_rules.format_stay_line(
        stay["guest"], total, credit, welcome
    )
    print(line)

total = business_rules.total_reserved(stays)
largest = business_rules.largest_stay(stays)
average = total / len(stays)

credit_count = 0
welcome_count = 0

for stay in stays:
    stay_total = business_rules.calculate_stay_total(
        stay["nightly_rate"], stay["nights"], stay["corporate"]
    )

    if business_rules.requires_credit_check(stay_total):
        credit_count += 1

    if business_rules.gets_welcome_package(stay["nights"], stay_total):
        welcome_count += 1

        
print("\nSummary:")
print("Stays:", len(stays))
print(f"Total Reserved: ${total:.2f}")
print(f"Largest Stay: {largest}")
print(f"Average Stay: ${average:.2f}")
print(f"Credit Checks Required: {credit_count}")
print(f"Welcome Packages Given: {welcome_count}")
