class Customer:
    def __init__(self):
        # Szótár az ügyfél részleteinek tárolására az azonosítójukkal kulcsként
        self.customers = {}

    def last_cust_id(self):
        # Visszaadja az utolsó hozzáadott ügyfél azonosítóját
        return max(self.customers.keys()) if self.customers else 0

    def add_customer(self, cust_name, age, bank):
        # Új ügyfél hozzáadása nevével, életkorával és kezdetben hozzárendelt bank nélkül
        last_id = self.last_cust_id()
        self.customers[last_id + 1] = {'name': cust_name, 'age': age, 'bank': bank}

    def assign_bank(self, cust_id, bank_name):
        # Bank hozzárendelése a megadott ügyfélhez
        if cust_id in self.customers:
            self.customers[cust_id]['bank'] = bank_name
            print(f"A(z) '{bank_name}' bank hozzárendelve a(z) '{cust_id}' azonosítójú ügyfélhez.")

    def del_customer(self, cust_id):
        # Megadott ügyfél törlése
        if cust_id in self.customers:
            del self.customers[cust_id]
            print(f"A(z) '{cust_id}' azonosítójú ügyfél törölve.")

    def list_customers(self):
        # Az ügyfél és részleteik listázása, beleértve a hozzárendelt bankot
        print("Ügyfelek listája:")
        for cust_id, details in self.customers.items():
            bank = details['bank'] if details['bank'] else "Nincs hozzárendelve"
            print(f"- Azonosító: {cust_id}, Név: {details['name']}, Életkor: {details['age']}, Bank: {bank}")


class Bank:
    def __init__(self):
        # Szótár a banknevek tárolására kulcsként, alkalmazottak listájával értékül
        self.bankname = {}
        # Szótár az alkalmazottak részleteinek tárolására, az alkalmazott nevével kulcsként
        self.employee = {}
        # Szótár a bankokhoz hozzárendelt ügyfelek tárolására
        self.customers_in_banks = {}
        # Meghívja a customer osztályt
        self.customer_obj = Customer()

    def add_new_bank(self, bank_name):
        # Új bank hozzáadása üres alkalmazottak és ügyfél listájával
        self.bankname[bank_name] = []
        self.customers_in_banks[bank_name] = []

    def add_employee(self, employee_name, age, bank_name):
        # Alkalmazott hozzáadása a megadott bankhoz
        if bank_name in self.bankname:
            # Alkalmazott részleteinek tárolása szótárban
            self.employee[employee_name] = {'age': age, 'bank': bank_name}
            # Alkalmazott hozzáadása a bank alkalmazottainak listájához
            self.bankname[bank_name].append(employee_name)
        else:
            print(f"A(z) '{bank_name}' bank nem létezik.")

    def add_customer_to_bank(self, cust_id, bank_name):
        # Ügyfelek hozzáadása a megadott bankhoz
        if bank_name in self.customers_in_banks:
            self.customers_in_banks[bank_name].append(cust_id)
        else:
            print(f"A(z) '{bank_name}' bank nem létezik.")

    def check_bank(self, bank_name):
        # Ellenőrzi, hogy létezik-e a bank, ha nem, felkínálja a létrehozását
        if bank_name not in self.bankname:
            create = input(f"A(z) '{bank_name}' bank nem létezik. Szeretné létrehozni? (y/n): ")
            if create.lower() == 'y':
                self.add_new_bank(bank_name)

    def check_employee(self, employee_name):
        # Ellenőrzi, hogy létezik-e az alkalmazott, ha nem, felkínálja hozzáadását
        if employee_name not in self.employee:
            create = input(f"A(z) '{employee_name}' alkalmazott nem létezik. Szeretné hozzáadni? (igen/nem): ")
            if create.lower() == 'igen':
                age = int(input("Az alkalmazott életkora: "))
                self.add_employee(employee_name, age)

    def del_bank(self, bank_name):
        # Megadott bank törlése
        if bank_name in self.bankname:
            del self.bankname[bank_name]
            print(f"A(z) '{bank_name}' bank törölve.")

    def del_employee(self, employee_name):
        # Megadott alkalmazott törlése
        if employee_name in self.employee:
            del self.employee[employee_name]
            print(f"A(z) '{employee_name}' alkalmazott törölve.")

    def list_banks(self):
        # Bankok, alkalmazottak és a bankokhoz hozzárendelt ügyfelek listázása
        print("Bankok, alkalmazottak és a bankokhoz hozzárendelt ügyfelek listája:")
        for bank, employees in self.bankname.items():
            print(f"- {bank}")
            if employees:
                print("  Alkalmazottak:")
                for emp in employees:
                    print(f"    - {emp}, Életkor: {self.employee[emp]['age']}")
            else:
                print("  Nincsenek alkalmazottak ebben a bankban.")

            assigned_customers = self.customers_in_banks[bank]
            if assigned_customers:
                print("  Ügyfelek:")
                for cust_id in assigned_customers:
                    # Ügyfél részleteinek lekérése a Customer osztályból és kiírása
                    print(f"    - Azonosító: {cust_id}, Név: {self.customer_obj.customers[cust_id]['name']}, Életkor: {self.customer_obj.customers[cust_id]['age']}")
            else:
                print("  Nincsenek ügyfelek hozzárendelve ehhez a bankhoz.")

    def list_employees(self):
        # Alkalmazottak listázása
        print("Alkalmazottak listája:")
        for emp, details in self.employee.items():
            print(f"- {emp}, Életkor: {details['age']}")