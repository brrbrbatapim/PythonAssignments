# Week 5 Assignment - Classes and Objects
# Programming Fundamentals


class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited NPR {amount} into {self.account_number}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds in {self.account_number}")
        else:
            self.balance -= amount
            print(f"Withdrawn NPR {amount} from {self.account_number}")

    def get_balance(self):
        print(f"{self.name} ({self.account_number}) - Current balance: NPR {self.balance}")


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 80:
            return "A"
        elif avg >= 65:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        avg = self.average()
        status = "Pass" if avg >= 40 else "Fail"
        print(f"{self.name} - Average: {avg:.2f}, Grade: {self.grade()}, Status: {status}")


class DeliveryPartner:
    def __init__(self, name, partner_id, deliveries):
        self.name = name
        self.partner_id = partner_id
        self.deliveries = deliveries

    def total_earning(self):
        return 0

    def display(self):
        print(
            f"{self.name} ({self.partner_id}) - Deliveries: {self.deliveries}, "
            f"Total earning: NPR {self.total_earning()}"
        )


class BikeRider(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, km_travelled):
        super().__init__(name, partner_id, deliveries)
        self.km_travelled = km_travelled

    def total_earning(self):
        return self.deliveries * 80 + self.km_travelled * 5


class Walker(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, rainy_deliveries):
        super().__init__(name, partner_id, deliveries)
        self.rainy_deliveries = rainy_deliveries

    def total_earning(self):
        return self.deliveries * 60 + self.rainy_deliveries * 50


class CarDriver(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, fuel_cost):
        super().__init__(name, partner_id, deliveries)
        self.fuel_cost = fuel_cost

    def total_earning(self):
        return self.deliveries * 120 - self.fuel_cost


class Bus:
    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = {}

    def book_seat(self, seat_number, passenger_name):
        if seat_number in self.booked:
            print(f"Seat already booked: Seat {seat_number}")
        elif seat_number < 1 or seat_number > self.total_seats:
            print(f"Invalid seat number: {seat_number}")
        else:
            self.booked[seat_number] = passenger_name
            print(f"Seat {seat_number} booked for {passenger_name}")

    def available_seats(self):
        return self.total_seats - len(self.booked)

    def passenger_list(self):
        print("Passenger List:")
        for seat, passenger in sorted(self.booked.items()):
            print(f"Seat {seat}: {passenger}")


# Main program
print("Question 1 - Bank Account Manager")
account_data = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai", "A003", 12000),
]

accounts = [BankAccount(name, acc_no, balance) for name, acc_no, balance in account_data]
accounts[1].deposit(3000)
accounts[2].withdraw(15000)
accounts[0].withdraw(2000)

print("Final balances:")
for account in accounts:
    account.get_balance()

print("\nQuestion 2 - Student Report Card")
students_data = [
    ("Aarav", [78, 85, 60, 90, 72]),
    ("Sita", [45, 50, 38, 60, 55]),
    ("Bishal", [30, 25, 40, 35, 28]),
    ("Priya", [90, 88, 95, 92, 87]),
]

students = [Student(name, marks) for name, marks in students_data]
for student in students:
    student.display()

print("\nQuestion 3 - Food Delivery App")
partners = [
    BikeRider("Santosh Rai", "B-01", 15, 42),
    Walker("Kabita Maharjan", "W-01", 18, 5),
    CarDriver("Roshan KC", "C-01", 20, 850),
]

for partner in partners:
    partner.display()

highest_partner = max(partners, key=lambda partner: partner.total_earning())
print(f"Highest earning partner: {highest_partner.name} with NPR {highest_partner.total_earning()}")

print("\nQuestion 4 - Bus Ticket Booking")
bus = Bus("Kathmandu - Pokhara", 10)
bookings = [
    (3, "Ramila Shrestha"),
    (7, "Deepak Gurung"),
    (3, "Anita Rai"),
    (1, "Prakash Magar"),
    (7, "Suman Tamang"),
]

for seat_number, passenger_name in bookings:
    bus.book_seat(seat_number, passenger_name)

print(f"Available seats: {bus.available_seats()}")
bus.passenger_list()
