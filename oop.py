
import datetime

class Employee(object):

    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:  # ! Monday == 0, Sunday = 6
            return False
        return True


emp_1 = Employee("Jeff", "Weng", 60000)
emp_2 = Employee("Test", "User", 12345)

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
