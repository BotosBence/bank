import bank_customer


class Bank:
    def __init__(self):
        self.bank_names = {}
        self.employees = {}
        self.customers_in_banks = [] # [bank_name, [cust_ids]]
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
            if bank in self.customer_obj.customers:
                assigned_customers = self.customers_in_banks[bank]
                if assigned_customers:
                    print("  Customers:")
                    for cust_id in assigned_customers:
                        print(f"    -ID: {cust_id}, Name: {self.customer_obj.customers[cust_id]['name']}, Age: {self.customer_obj.customers[cust_id]['age']}")
                else:
                    print("  No customers assigned to this bank.")
            else:
                print("  There are no customers")
                print(self.customer_obj.customers)

    def list_employees(self):
        print("Employees:")
        for emp, details in self.employees.items():
            print(f"- {emp}, Age: {details['age']}")

    def save_bank_data(self, file_name):
        with open(file_name, 'w') as file:
            for bank, employees in self.bank_names.items():
                file.write(f"{bank}:\n")
                for emp in employees:
                    file.write(f"    {emp}:{self.employees[emp]['age']}\n")
                file.write('\n')

                assigned_customers = self.customers_in_banks[bank] if bank in self.customers_in_banks else []
                for cust_id in assigned_customers:
                    name = self.customer_obj.customers[cust_id]['name']
                    age = self.customer_obj.customers[cust_id]['age']
                    file.write(f"    {cust_id}:{name}:{age}\n")
                file.write('\n')

    def load_bank_data(self, file_name):
        with open(file_name, 'r') as file:
            self.bank_names = {}
            self.employees = {}
            self.customers_in_banks = {}
            lines = file.readlines()
            bank = ''
            employees = []
            assigned_customers = []
            for line in lines:
                if line.startswith('-'):
                    cust_id, name, age = line.strip().split(':')[1:]
                    assigned_customers.append(int(cust_id))
                    self.customer_obj.customers[int(cust_id)] = {'name': name, 'age': int(age)}
                elif line.startswith(' '):
                    parts = line.strip().split(':')
                    if len(parts) == 2:
                        emp_name, emp_age = parts
                        employees.append(emp_name)
                        self.employees[emp_name] = {'age': int(emp_age), 'bank': bank}
                else:
                    if bank:
                        self.bank_names[bank] = employees
                        self.customers_in_banks[bank] = assigned_customers
                        employees = []
                        assigned_customers = []
                    bank = line.strip().split(':')[0]
