import bank_customer


class Bank:
    def __init__(self):
        self.bank_names = {}
        self.employees = {}
        self.customers_in_banks = []
        self.customer_obj = bank_customer.Customer()

    def add_new_bank(self, bank_name):
        self.bank_names[bank_name] = []     # Új bank hozzáadása a bank nevek szótárához

    def add_employee(self, employee_name, age, bank_name):
        if bank_name in self.bank_names:    # Dolgozó hozzáadása a megadott bankhoz
            self.employees[employee_name] = {'age': age, 'bank': bank_name}
            self.bank_names[bank_name].append(employee_name)
        else:
            print(f"The bank '{bank_name}' does not exist.")    # Ellenőrzi, hogy a megadott bank létezik-e
            create = input("Create? (y / n): ")
            if create.lower() == 'y':
                self.add_new_bank(bank_name)    # Ha a megadott bank nem létezik, kiírja az üzenetet
                self.employees[employee_name] = {'age': age, 'bank': bank_name}
                self.bank_names[bank_name].append(employee_name)

    def add_customer_to_bank(self, cust_id, bank_name):
        banks = self.customers_in_banks     # Ügyfél hozzáadása a megadott bankhoz
        if bank_name in self.bank_names:
            if bank_name not in banks:
                banks.append([bank_name, cust_id])
            else:
                for bank in banks:
                    if bank[0] == bank_name:
                        bank.append(cust_id)
        else:
            print(f"The bank '{bank_name}' does not exist.")    # Ha a megadott bank nem létezik, kiírja az üzenetet

    def check_bank(self, bank_name):
        if bank_name not in self.bank_names:
            create = input(f"The bank '{bank_name}' does not exist. Create? (y/n): ")    # Ellenőrzi, hogy a megadott bank létezik-e
            if create.lower() == 'y':
                self.add_new_bank(bank_name)
        else:
            print("This bank exist")

    def check_employee(self, employee_name):
        if employee_name not in self.employees:
            create = input(f"The employee '{employee_name}' does not exist. Add? (yes/no): ")
            if create.lower() == 'yes':
                age = int(input("Employee's age: "))
                self.add_employee(employee_name, age, None)
        else:
            print("This employe exist")

    def del_bank(self, bank_name):
        if bank_name in self.bank_names:
            del self.bank_names[bank_name]
            print(f"The bank '{bank_name}' has been deleted.")
        else:
            print("Bank does not exist")

    def del_employee(self, employee_name):
        if employee_name in self.employees:
            del self.employees[employee_name]
            print(f"The employee '{employee_name}' has been deleted.")
        else:
            print("employee does not exist")

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
            print("  Customers:")
            self.customer_obj.list_bank_customer(bank)

    def list_customers(self):
        print("  Customers:")
        for bank, employees in self.bank_names.items():
            self.customer_obj.list_bank_customer(bank)

    def list_employees(self):
        print("  Employees:")
        for bank, employees in self.bank_names.items():
            for emp in employees:
                print(f"    -Name: {emp}, Age: {self.employees[emp]['age']}, Bank: {bank}")

    def save_to_file(self, filename='save.txt'):        # Adatok mentése fájlba
        with open(filename, 'w') as file:
            file.write("Bank Names:\n")
            for bank_name, employees in self.bank_names.items():
                file.write(f"{bank_name}: {','.join(employees)}")

            file.write("\nEmployees:\n")
            for employee, details in self.employees.items():
                file.write(f"{employee}: {details['age']},{details['bank']}\n")

            file.write("\nCustomers in Banks:\n")
            for bank_customer in self.customers_in_banks:
                file.write(f"{bank_customer[0]}: {','.join(bank_customer[1])}\n")

        print(f"Data saved to '{filename}'.")

    def load_from_file(self, filename='save.txt'):      # Adatok betöltése fájlból
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
                        if len(line.split(': ')) == 1:
                            bank_name = line.strip()
                            a = len(bank_name)-1     # csak azért kell hogy ne legyen : banknév végén
                            bank_name = bank_name[:a]
                            self.bank_names[bank_name] = []
                        else:
                            bank_name, employees = line.split(': ')
                            self.bank_names[bank_name] = employees.split(',')
                    elif current_section == 'employees':
                        employee, details = line.split(': ')
                        age, bank = details.split(',')
                        self.employees[employee] = {'age': int(age), 'bank': bank}
                    elif current_section == 'customers_in_banks':
                        bank_name, customers = line.split(': ')
                        self.customers_in_banks.append([bank_name, customers.split(',')])

        print(f"Data loaded from '{filename}'.")
