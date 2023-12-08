class Customer:
    def __init__(self):
        self.customers = {}
        self.bank_customer_list = {}

    def last_customer_id(self):
        return max(self.customers.keys()) if self.customers else 0

    def add_customer(self, name, age, bank):
        last_id = self.last_customer_id()
        self.customers[last_id + 1] = {'name': name, 'age': age, 'bank': bank}

    def assign_bank(self, cust_id, bank_name):
        if cust_id in self.customers:
            self.customers[cust_id]['bank'] = bank_name
            self.bank_customer_list[bank_name] = self.customers[cust_id]

    def delete_customer(self, cust_id):
        if cust_id in self.customers:
            del self.customers[cust_id]

    def list_customers(self):
        print("Customers:")
        for cust_id, details in self.customers.items():
            bank = details['bank'] if details['bank'] else "Not assigned"
            print(f"ID: {cust_id}, Name: {details['name']}, Age: {details['age']}, Bank: {bank}")

    def save_customers(self, file_name):
        with open(file_name, 'w') as file:
            for cust_id, details in self.customers.items():
                bank = details['bank'] if details['bank'] else "Not assigned"
                file.write(f"{cust_id}:{details['name']}:{details['age']}:{bank}\n")

    def load_customers(self, file_name):
        with open(file_name, 'r') as file:
            self.customers = {}
            lines = file.readlines()
            for line in lines:
                cust_id, name, age, bank = line.strip().split(':')
                self.customers[int(cust_id)] = {'name': name, 'age': int(age), 'bank': bank}
