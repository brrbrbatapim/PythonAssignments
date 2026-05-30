# Week 6 Assignment - Scope and Module
# Programming Fundamentals

import math
import random
import datetime
from discount import final_price, TAX_RATE


station_name = "Kathmandu Weather Station"
college_name = "Bhaktapur Multiple Campus"
random.seed(42)


def get_average(temps):
    return sum(temps) / len(temps)


def get_deviation(temps):
    mean = get_average(temps)  # local variable
    variance = sum((temp - mean) ** 2 for temp in temps) / len(temps)
    return math.sqrt(variance)


# Accessing mean outside get_deviation() would cause a NameError because
# mean is a local variable created only inside that function.


def get_summary(temps):
    print("Question 1 - Temperature Logger")
    print(station_name)
    print(f"Minimum temperature: {min(temps):.2f} C")
    print(f"Maximum temperature: {max(temps):.2f} C")
    print(f"Average temperature: {get_average(temps):.2f} C")
    print(f"Standard deviation: {get_deviation(temps):.2f}")


def split_bill(friends, total):
    return total / len(friends)


def pick_lucky(friends):
    return random.choice(friends)


def final_summary(friends, total):
    print("\nQuestion 2 - Bill Splitter")
    share = split_bill(friends, total)
    lucky_person = pick_lucky(friends)

    for friend in friends:
        if friend == lucky_person:
            lucky_total = share + 50  # local variable
            print(f"{friend}: NPR {lucky_total:.2f}")
        else:
            print(f"{friend}: NPR {share:.2f}")

    print(f"Lucky person paying extra NPR 50: {lucky_person}")


def parse_date(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d")


def get_exam_date(start_str, days):
    start = parse_date(start_str)
    exam_date = start + datetime.timedelta(days=days)
    return exam_date.strftime("%Y-%m-%d")


def print_schedule(start_str, exams):
    print("\nQuestion 3 - Exam Scheduler")
    print(college_name)
    for subject, days in exams:
        print(f"{subject}: {get_exam_date(start_str, days)}")


# Main program
if __name__ == "__main__":
    temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]
    get_summary(temperatures)

    friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]
    total_bill = 3750
    final_summary(friends, total_bill)

    start_date = "2025-05-01"
    exams = [
        ("Python Programming", 0),
        ("Data Structures", 3),
        ("Database Systems", 6),
        ("Computer Networks", 10),
        ("Mathematics", 14),
    ]
    print_schedule(start_date, exams)

    print("\nQuestion 4 - Shopping Discount")
    products = [
        ("Laptop", 85000, 10),
        ("Headphones", 4500, 15),
        ("Phone Case", 800, 5),
        ("USB Cable", 600, 0),
    ]

    print(f"Imported TAX_RATE: {TAX_RATE}")
    for name, price, discount_pct in products:
        final = final_price(price, discount_pct)
        print(f"{name}: Original price = NPR {price}, Final price = NPR {final:.2f}")
