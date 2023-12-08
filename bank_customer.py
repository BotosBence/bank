class Customer:
    def __init__(self):
        self.customers = {}
        self.customers_in_banks = []

    def last_customer_id(self):
        return max(self.customers.keys()) if self.customers else 0

    def add_customer(self, name, age, bank):
        last_id = self.last_customer_id()
        self.customers[last_id + 1] = {'name': name, 'age': age, 'bank': bank}

    def delete_customer(self, cust_id):
        if cust_id in self.customers:
            del self.customers[cust_id]

    def list_customers(self):
        print("Customers:")
        for cust_id, details in self.customers.items():
            bank = details['bank'] if details['bank'] else "Not assigned"
            print(f"ID: {cust_id}, Name: {details['name']}, Age: {details['age']}, Bank: {bank}")

    def save_to_file(self, filename='save.txt'):
        with open(filename, 'w') as file:
            for cust_id, details in self.customers.items():
                file.write(f"{cust_id},{details['name']},{details['age']},{details['bank']}\n")

    def load_from_file(self, filename='save.txt'):
        self.customers = {}
        with open(filename, 'r') as file:
            for line in file:
                cust_id, name, age, bank = line.strip().split(',')
                self.customers[int(cust_id)] = {'name': name, 'age': int(age), 'bank': bank}
