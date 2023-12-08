from Bank_software import Bank, Customer

bank = Bank()
bank.add_new_bank('Bank')
bank.add_employee('John Doe', 30, "Bank")
bank.list_banks()
bank.list_employees()

customer = Customer()
customer.add_customer('Alice', 25)
customer.add_customer('Bob', 35)
customer.list_customers()
