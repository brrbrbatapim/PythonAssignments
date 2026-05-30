# Week 4 Assignment - Functions
# Programming Fundamentals - Agrata Shrestha


def process_order(inventory, cart):
    print("Question 1 - Small Shop Billing and Inventory System")
    print("---- Bill ----")
    grand_total = 0
    purchased_items = []

    for item, quantity in cart.items():
        if item not in inventory:
            print(f"{item} is not available in inventory")
            continue

        if inventory[item]["stock"] >= quantity:
            item_total = inventory[item]["price"] * quantity
            grand_total += item_total
            inventory[item]["stock"] -= quantity
            purchased_items.append(item)
            print(f"{item} x{quantity} = NPR {item_total}")
        else:
            print(f"Sorry, not enough stock for {item}")

    print(f"Grand Total: NPR {grand_total}")
    print("--------------")
    updated_stock = ", ".join(f"{item}={inventory[item]['stock']}" for item in purchased_items)
    print(f"Updated stock: {updated_stock}")


def check_water_level(location, level_metres):
    if level_metres < 3:
        return "Safe"
    elif level_metres <= 5:
        return "Warning - Alert nearby villages"
    else:
        return "DANGER - Evacuate immediately!"


def convert_date(date_str, from_cal, to_cal):
    year, month, day = date_str.split("-")
    year = int(year)

    if from_cal == to_cal:
        converted_year = year
    elif from_cal == "AD" and to_cal == "BS":
        converted_year = year + 56
    elif from_cal == "BS" and to_cal == "AD":
        converted_year = year - 56
    else:
        return "Invalid calendar type"

    return f"{converted_year:04d}-{month}-{day}"


def ordinal_day(day):
    day = int(day)
    if 10 <= day % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    return f"{day}{suffix}"


def format_date(date_str, calendar, style):
    bs_months = [
        "Baisakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin",
        "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"
    ]
    year, month, day = date_str.split("-")

    if style == "iso":
        return f"{date_str} {calendar}"
    elif style in ["full", "nepali"] and calendar == "BS":
        month_name = bs_months[int(month) - 1]
        return f"{ordinal_day(day)} {month_name}, {year} {calendar}"
    elif style == "full":
        return f"{ordinal_day(day)}-{month}-{year} {calendar}"
    else:
        return f"{date_str} {calendar}"


def word_frequency(text):
    punctuation = ",.!?;:()\"'"
    words = text.lower().split()
    counts = {}

    for word in words:
        clean_word = word.strip(punctuation)
        counts[clean_word] = counts.get(clean_word, 0) + 1

    top_three = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]
    return top_three


accounts = {
    "A001": {"name": "Ramesh Thapa", "balance": 15000, "pin": "1234"},
    "A002": {"name": "Sunita Karki", "balance": 8500, "pin": "5678"},
    "A003": {"name": "Bikash Rai", "balance": 22000, "pin": "9012"}
}


def atm(account_id, pin, action, amount=0):
    if account_id not in accounts:
        print("Account not found")
        return

    account = accounts[account_id]

    if account["pin"] != pin:
        print("Incorrect PIN")
        return

    if action == "balance":
        print(f"{account['name']} - Current balance: NPR {account['balance']}")
    elif action == "deposit":
        account["balance"] += amount
        print(f"Deposit successful. New balance: NPR {account['balance']}")
    elif action == "withdraw":
        if amount > account["balance"]:
            print("Insufficient funds")
        else:
            account["balance"] -= amount
            print(f"Withdrawal successful. New balance: NPR {account['balance']}")
    else:
        print("Invalid action")


# Main program
inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30}
}

cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}

process_order(inventory, cart)

print("\nQuestion 2 - Water Level Alert System")
sensors = [
    ("Chatara", 2.8),
    ("Tribeni Ghat", 5.4),
    ("Koshi Barrage", 4.1),
    ("Sunsari Bridge", 1.9),
    ("Saptakoshi Camp", 6.0),
]

for location, level in sensors:
    print(f"{location} ({level} m): {check_water_level(location, level)}")

print("\nQuestion 3 - Date Converter for Nepal Bank System")
customers = [
    {"name": "Ramesh Thapa", "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki", "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai", "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"},
]

for customer in customers:
    converted = convert_date(customer["date"], customer["cal"], customer["need"])
    formatted = format_date(converted, customer["need"], customer["style"])
    print(f"{customer['name']} | Original: {customer['date']} {customer['cal']} | Converted: {formatted}")

print("\nQuestion 4 - Word Frequency Counter")
text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""

print("Top 3 words:")
for word, count in word_frequency(text):
    print(f"{word} - {count} times")

print("\nQuestion 5 - Simple ATM Simulator")
atm("A001", "1234", "balance")
atm("A002", "0000", "withdraw", 2000)
atm("A002", "5678", "deposit", 3000)
atm("A003", "9012", "withdraw", 25000)
atm("A004", "1111", "balance")
