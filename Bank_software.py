import bank_customer


class Bank:
    def __init__(self):
        self.bank_names = {}
        self.employees = {}
        self.customers_in_banks = []    # [bank_name, [cust_ids]]
        self.customer_obj = bank_customer.Customer()

    def add_new_bank(self, bank_name):
        self.bank_names[bank_name] = []

    def add_employee(self, employee_name, age, bank_name):
        if bank_name in self.bank_names:
            self.employees[employee_name] = {'age': age, 'bank': bank_name}
            self.bank_names[bank_name].append(employee_name)
        else:
            print(f"The bank '{bank_name}' does not exist.")

    def add_customer_to_bank(self, cust_id, bank_name):
        banks = self.customers_in_banks
        if bank_name in self.bank_names:
            if bank_name not in banks:
                banks.append([bank_name, cust_id])
            else:
                for bank in banks:
                    if bank[0] == bank_name:
                        bank.append(cust_id)
        else:
            print(f"The bank '{bank_name}' does not exist.")

    def check_bank(self, bank_name):
        if bank_name not in self.bank_names:
            create = input(f"The bank '{bank_name}' does not exist. Create? (y/n): ")
            if create.lower() == 'y':
                self.add_new_bank(bank_name)

    def check_employee(self, employee_name):
        if employee_name not in self.employees:
            create = input(f"The employee '{employee_name}' does not exist. Add? (yes/no): ")
            if create.lower() == 'yes':
                age = int(input("Employee's age: "))
                self.add_employee(employee_name, age, None)

    def del_bank(self, bank_name):
        if bank_name in self.bank_names:
            del self.bank_names[bank_name]
            print(f"The bank '{bank_name}' has been deleted.")

    def del_employee(self, employee_name):
        if employee_name in self.employees:
            del self.employees[employee_name]
            print(f"The employee '{employee_name}' has been deleted.")

    def list_banks(self):
        print("Banks, employees, and assigned customers:")
        for bank, employees in self.bank_names.items():
            print(f"- {bank}")
            if employees:
                print("  Employees:")
                for emp in employees:
                    print(f"    -Name: {emp}, Age: {self.employees[emp]['age']}")
            else:
                print("  No employees in this bank.")
            for customer_bank in self.customers_in_banks:
                if customer_bank[0] == bank:
                    print(customer_bank)

    def list_employees(self):
        print("Employees:")
        for emp, details in self.employees.items():
            print(f"- {emp}, Age: {details['age']}")

    def save_to_file(self, filename='save.txt'):
        with open(filename, 'w') as file:
            file.write("Bank Names:\n")
            for bank_name, employees in self.bank_names.items():
                file.write(f"{bank_name}: {employees}\n")

            file.write("\nEmployees:\n")
            for employee, details in self.employees.items():
                file.write(f"{employee}: {details}\n")

            file.write("\nCustomers in Banks:\n")
            for bank_customer in self.customers_in_banks:
                file.write(f"{bank_customer[0]}: {bank_customer[1]}\n")

        print(f"Data saved to '{filename}'.")

    def load_from_file(self, filename='save.txt'):
        with open(filename, 'r') as file:
            lines = file.readlines()
            current_section = None
            self.bank_names = {}
            self.employees = {}
            self.customers_in_banks = []

            for line in lines:
                line = line.strip()
                if line == "Bank Names:":
                    current_section = 'bank_names'
                elif line == "Employees:":
                    current_section = 'employees'
                elif line == "Customers in Banks:":
                    current_section = 'customers_in_banks'
                elif line:
                    if current_section == 'bank_names':
                        bank_name, employees = line.split(': ')
                        self.bank_names[bank_name] = eval(employees)
                    elif current_section == 'employees':
                        employee, details = line.split(': ')
                        self.employees[employee] = eval(details)
                    elif current_section == 'customers_in_banks':
                        bank_name, customers = line.split(': ')
                        self.customers_in_banks.append([bank_name, eval(customers)])

        print(f"Data loaded from '{filename}'.")