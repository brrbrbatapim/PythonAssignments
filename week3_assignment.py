# Week 3 Assignment
# Programming Fundamentals - Conditionals and Loops


def atm_withdrawal_validator(balance, daily_withdrawn, amount):
    print("Question 1 - ATM Withdrawal Validator")
    print(f"Balance: NPR {balance}")
    print(f"Already withdrawn today: NPR {daily_withdrawn}")
    print(f"Requested withdrawal: NPR {amount}")

    daily_limit = 50000

    if amount % 500 != 0:
        print("Invalid amount. Must be a multiple of NPR 500.")
    elif amount > balance:
        print("Insufficient balance.")
    elif daily_withdrawn + amount > daily_limit:
        print("Daily withdrawal limit reached.")
    else:
        balance -= amount
        print("Withdrawal successful.")
        print(f"Your current balance after withdrawal: NPR {balance}")


def online_store_discount(total_purchase, is_loyalty_member):
    print("\nQuestion 2 - Online Store Discount System")
    print(f"Total purchase amount: NPR {total_purchase}")
    print(f"Loyalty member: {'Yes' if is_loyalty_member else 'No'}")

    if total_purchase < 1000:
        discount_rate = 0
    elif total_purchase <= 4999:
        discount_rate = 0.05
    elif total_purchase <= 14999:
        discount_rate = 0.10
    else:
        discount_rate = 0.20

    discount_amount = total_purchase * discount_rate
    amount_after_discount = total_purchase - discount_amount

    if is_loyalty_member:
        loyalty_discount = amount_after_discount * 0.05
    else:
        loyalty_discount = 0

    final_amount = amount_after_discount - loyalty_discount

    print(f"Regular discount: NPR {discount_amount:.2f}")
    print(f"Loyalty discount: NPR {loyalty_discount:.2f}")
    print(f"Final payable amount: NPR {final_amount:.2f}")


def inventory_restock_alert(inventory):
    print("\nQuestion 3 - Inventory Restock Alert")
    restock_count = 0

    for product in inventory:
        if product["stock"] < product["threshold"]:
            print(
                f"Restock alert: {product['item']} "
                f"(Stock: {product['stock']}, Threshold: {product['threshold']})"
            )
            restock_count += 1

    print(f"Total number of items that need restocking: {restock_count}")


def password_strength_checker(passwords):
    print("\nQuestion 4 - Password Strength Checker")
    special_characters = "!@#$%^&*"

    for password in passwords:
        missing = []

        if len(password) < 8:
            missing.append("at least 8 characters")
        if not any(char.isupper() for char in password):
            missing.append("one uppercase letter")
        if not any(char.islower() for char in password):
            missing.append("one lowercase letter")
        if not any(char.isdigit() for char in password):
            missing.append("one digit")
        if not any(char in special_characters for char in password):
            missing.append("one special character from !@#$%^&*")

        if len(missing) == 0:
            print(f"{password}: Strong password.")
        else:
            print(f"{password}: Weak password. Missing: {', '.join(missing)}.")


def taxi_fare_calculator(trips):
    print("\nQuestion 5 - Taxi Fare Calculator")

    for index, trip in enumerate(trips, start=1):
        distance = trip["distance"]
        hour = trip["hour"]

        if distance <= 2:
            fare = 150
        elif distance <= 10:
            fare = 150 + (distance - 2) * 35
        else:
            fare = 150 + 8 * 35 + (distance - 10) * 28

        if hour >= 22 or hour < 5:
            fare += fare * 0.10
            surcharge = "Yes"
        else:
            surcharge = "No"

        print(
            f"Trip {index}: Distance = {distance} km, Hour = {hour}, "
            f"Night surcharge = {surcharge}, Fare = NPR {fare:.2f}"
        )


# Main program with sample inputs
balance = 60000
daily_withdrawn = 20000
amount = 15000
atm_withdrawal_validator(balance, daily_withdrawn, amount)

online_store_discount(total_purchase=16000, is_loyalty_member=True)

inventory = [
    {"item": "Rice", "stock": 5, "threshold": 10},
    {"item": "Eggs", "stock": 24, "threshold": 12},
    {"item": "Milk", "stock": 3, "threshold": 6},
    {"item": "Bread", "stock": 8, "threshold": 5},
    {"item": "Chicken", "stock": 0, "threshold": 4},
    {"item": "Cooking Oil", "stock": 2, "threshold": 3},
]
inventory_restock_alert(inventory)

passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]
password_strength_checker(passwords)

trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]
taxi_fare_calculator(trips)
