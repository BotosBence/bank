class Bank:
    def __init__(self):
        self.bankname = {}
        self.employee = {}

    def add_new_bank(self, bank_name):
        self.bankname[bank_name] = []

    def add_employee(self, employee_name, age, bank_name):
        if bank_name in self.bankname:
            self.employee[employee_name] = {'age': age, 'bank': bank_name}
            self.bankname[bank_name].append(employee_name)
        else:
            print(f"Bank '{bank_name}' does not exist.")

    def check_bank(self, bank_name):
        if bank_name not in self.bankname:
            create = input(f"Bank '{bank_name}' does not exist. Do you want to create it? (yes/no): ")
            if create.lower() == 'yes':
                self.add_new_bank(bank_name)

    def check_employee(self, employee_name):
        if employee_name not in self.employee:
            create = input(f"Employee '{employee_name}' does not exist. Do you want to add them? (yes/no): ")
            if create.lower() == 'yes':
                age = int(input("Enter employee's age: "))
                self.add_employee(employee_name, age)

    def del_bank(self, bank_name):
        if bank_name in self.bankname:
            del self.bankname[bank_name]
            print(f"Bank '{bank_name}' deleted.")

    def del_employee(self, employee_name):
        if employee_name in self.employee:
            del self.employee[employee_name]
            print(f"Employee '{employee_name}' deleted.")

    def list_banks(self):
        print("List of Banks and Employees:")
        for bank, employees in self.bankname.items():
            print(f"- {bank}")
            if employees:
                print("  Employees:")
                for emp in employees:
                    print(f"    - {emp}, Age: {self.employee[emp]['age']}")
            else:
                print("  No employees in this bank.")


    def list_employees(self):
        print("List of Employees:")
        for emp, age in self.employee.items():
            print(f"- {emp}, Age: {age}")

class Customer:
    def __init__(self):
        self.customers = {}

    def last_cust_id(self):
        return max(self.customers.keys()) if self.customers else 0

    def add_customer(self, cust_name, age):
        last_id = self.last_cust_id()
        self.customers[last_id + 1] = {'name': cust_name, 'age': age, 'bank': None}

    def assign_bank(self, cust_id, bank_name):
        if cust_id in self.customers:
            self.customers[cust_id]['bank'] = bank_name
            print(f"Bank '{bank_name}' assigned to customer ID '{cust_id}'.")

    def del_customer(self, cust_id):
        if cust_id in self.customers:
            del self.customers[cust_id]
            print(f"Customer with ID '{cust_id}' deleted.")

    def list_customers(self):
        print("List of Customers:")
        for cust_id, details in self.customers.items():
            bank = details['bank'] if details['bank'] else "Not assigned"
            print(f"- ID: {cust_id}, Name: {details['name']}, Age: {details['age']}, Bank: {bank}")