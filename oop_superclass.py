class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay
        
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = (self.pay*self.raise_amt)
        
class Developer(Employee):
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang) -> None:
        super().__init__(first, last, pay)
        # ? Employee.__init__(self, first, last, pay) Alternative way to use it
        self.prog_lang = prog_lang
        
class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None) -> None:
            super().__init__(first, last, pay)
            
            if employees is None:
                self.employees = []
            else:
                self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())
    
    
    
    
dev_1 = Developer("Jeff", "Weng", 50000, "Python")
dev_2 = Developer("Test", "Employee", 60000, "Java")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

print(isinstance(mgr_1, Manager))