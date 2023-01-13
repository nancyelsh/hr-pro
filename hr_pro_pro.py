from datetime import date

class Employee:
    def __init__(self, name, age, salary, employment_year):
         self.name = name
         self.age = age
         self.salary = salary
         self.employment_year = employment_year

    def get_working_years(self):
        return date.today().year - self.employment_year

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.get_working_years()}"

class Manager(Employee):
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
         super().__init__(name, age, salary, employment_year)
         self.bonus_percentage = bonus_percentage

    def get_bonus(self):
        return self.bonus_percentage * self.salary

    def __str__(self):
        properties = [
            super().__str__(),
            f"Bonus: {self.get_bonus()}"
        ]
        return ", ".join(properties)

def show_options():
    print("""
        Welcome to HR Pro 2019
        Options:
        1. Show Employees
        2. Show Managers
        3. Add An Employee
        4. Add A Manager
        5. Exit

        """)

def get_user_choice():
    option = input("What would you like to do? ")
    return option

def show_employees(employees):
    print("""
    -----------------
    Employees
    
    """)
    for employee in employees:
        print(f"    {employee}")
    print("    -----------------")

def add_employee(employees):
    print("-----------------")
    EMP_name = input("Name: ")
    EMP_age = input("Age: ")
    EMP_salary = int(input("Salary: "))
    EMP_employment_year = int(input("Employement year: "))
    employees.append(Employee(EMP_name, EMP_age, EMP_salary, EMP_employment_year))
    print("Employee added succesfully")

def show_managers(managers):
    print("""
    -----------------
    Managers
    
    """)
    for manager in managers:
        print(f"    {manager}")
    print("    -----------------")

def add_manager(managers):
    print("-----------------")
    MGR_name = input("Name: ")
    MGR_age = input("Age: ")
    MGR_salary = int(input("Salary: "))
    MGR_employment_year = int(input("Employement year: "))
    MGR_bonus_percentage = float(input("Bonus Percentage: "))
    managers.append(Manager(MGR_name, MGR_age, MGR_salary, MGR_employment_year, MGR_bonus_percentage))
    print("Manager added succesfully")

def main():
    employees = []
    managers = []

    show_options()
    OPT = get_user_choice()

    while OPT != 5:        
        if int(OPT) == 1:
            show_employees(employees)
        elif int(OPT) == 2:
            show_managers(managers)
        elif int(OPT) == 3:
            add_employee(employees)
        elif int(OPT) == 4:
            add_manager(managers)
        else:
            print("Input is invalid. Try again, please.")

        OPT = get_user_choice()

if __name__ == '__main__':
	main()
