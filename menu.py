from Bank_software import Bank, Customer
import time
language=int(input("Language/Nyelv/Sprache: 1 English, 2 Magyar, 3 Deutsch"))
bank = Bank()
customer = Customer()
c=()

if language==1:
    def print_menu():
        print("menü:")
        print("1. Add new bank")
        print("2. Add employee")
        print("3. Check bank ")
        print("4. Check employee ")
        print("5. Delete bank")
        print("6. Delete employee")
        print("7. List banks")
        print("8. List employees")
        print("9. Add new customer")
        print("10. Assign bank to customer")
        print("11. Delete customer")
        print("12. List customers")
        print("0. Exit")

    while c!= 0:
        print_menu()
        c = input("Enter your choice: ")

        if c == "1":
            bank_name = input("Enter the name of the new bank: ")
            bank.add_new_bank(bank_name)
        elif c == "2":
            employee_name = input("Enter employee name: ")
            age = int(input("Enter employee age: "))
            bank_name = input("Enter bank name to add employee: ")
            bank.add_employee(employee_name, age, bank_name)
        elif c == "3":
            bank_name = input("Enter bank name to check existence: ")
            bank.check_bank(bank_name)
        elif c == "4":
            employee_name = input("Enter employee name to check existence: ")
            bank.check_employee(employee_name)
        elif c == "5":
            bank_name = input("Enter bank name to delete: ")
            bank.del_bank(bank_name)
        elif c == "6":
            employee_name = input("Enter employee name to delete: ")
            bank.del_employee(employee_name)
        elif c == "7":
            bank.list_banks()
        elif c =="8":
            bank.list_employees
        elif c == "9":
            cust_name = input("Enter customer name: ")
            age = int(input("Enter customer age: "))
            customer.add_customer(cust_name, age, bank)
        elif c == "10":
            cust_id = int(input("Enter customer ID: "))
            bank_name = input("Enter bank name to assign: ")
            customer.assign_bank(cust_id, bank_name)
        elif c == "11":
            cust_id = int(input("Enter customer ID to delete: "))
            customer.del_customer(cust_id)
        elif c == "12":
            customer.list_customers()
        elif c == "0":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid. Please try again.")
        if c== 7 or 8 or 12:
            time.sleep(10)

if language==2:
    def print_menu1():
        print("menü:")
        print("1. Új bank")
        print("2. Új dolgozó")
        print("3. Bank létezésének ellenőrzése ")
        print("4. Dolgozó létezésének ellenőrzése ")
        print("5. bank törlése")
        print("6. dolgozó törlése")
        print("7. bankokm listája")
        print("8. dolgozók listája")
        print("9. új felhasználó")
        print("10. felhasználó bankhoz adása")
        print("11. felhasználó törlése")
        print("12. felhasználók listázása")
        print("0. kilépés")

    while c!= 0:
        print_menu1()
        c = input("Választott menüpont: ")

        if c == "1":
            bank_name = input("Új bank nevének megadása: ")
            bank.add_new_bank(bank_name)
        elif c == "2":
            employee_name = input("Új dolgozó megadása: ")
            age = int(input("Dolgozó kora: "))
            bank_name = input("Dolgozó melyik bankhoz tartozik: ")
            bank.add_employee(employee_name, age, bank_name)
        elif c == "3":
            bank_name = input("Bank nevének megadása létezésének ellenőrzéséhez: ")
            bank.check_bank(bank_name)
        elif c == "4":
            employee_name = input("Dolgozó nevének megadása létezésének ellenőrzéséhez: ")
            bank.check_employee(employee_name)
        elif c == "5":
            bank_name = input("Törlendő bank neve: ")
            bank.del_bank(bank_name)
        elif c == "6":
            employee_name = input("törlendő dolgozó neve: ")
            bank.del_employee(employee_name)
        elif c == "7":
            bank.list_banks()
        elif c =="8":
            bank.list_employees
        elif c == "9":
            cust_name = input("Felhasználó neve: ")
            age = int(input("Felhasználó kora: "))
            customer.add_customer(cust_name, age)
        elif c == "10":
            cust_id = int(input("Felhasználó ID-ja: "))
            bank_name = input("Felhasználó bankhoz rendelése: ")
            customer.assign_bank(cust_id, bank_name)
        elif c == "11":
            cust_id = int(input("Felhasználó törléséhez id megadása: "))
            customer.del_customer(cust_id)
        elif c == "12":
            customer.list_customers()
        elif c == "0":
            print("Kilépés, köszönjük hogy ezt a programot használja!")
            break
        else:
            print("Hibás választás")
        if c== 7 or 8 or 12:
            time.sleep(10)
if language==3:
    def print_menu2():
        print("menu:")
        print("1. Neue bank")
        print("2. Neue arbeiter")
        print("3. Überprüfung der existenz enier bank ")
        print("4. Überprüfung der existenz enier arbeiter ")
        print("5. löschen bank")
        print("6. Löschen arbeiter")
        print("7. liste der banken")
        print("8. liste der arbaiter")
        print("9. Neue benutzer")
        print("10. Hinzufügen eines Benutzers zur bank")
        print("11. Löschen benutzer")
        print("12. Liste der benutzer")
        print("0. ausfhart")

    while c!= 0:
        print_menu2()
        c = input("asgewählten menüponkt: ")

        if c == "1":
            bank_name = input("Name aus der bank: ")
            bank.add_new_bank(bank_name)
        elif c == "2":
            employee_name = input("Name aus der arbeiter: ")
            age = int(input("Alte aus der arbaiter: "))
            bank_name = input("Im  welche bank ist er/sie arbaiten: ")
            bank.add_employee(employee_name, age, bank_name)
        elif c == "3":
            bank_name = input("Name aus der bank : ")
            bank.check_bank(bank_name)
        elif c == "4":
            employee_name = input("Name aus der arbaiter: ")
            bank.check_employee(employee_name)
        elif c == "5":
            bank_name = input("Name der bank, die gelöscht werden soll: ")
            bank.del_bank(bank_name)
        elif c == "6":
            employee_name = input("Name der arbaiter, die gelöscht werden soll: ")
            bank.del_employee(employee_name)
        elif c == "7":
            bank.list_banks()
        elif c =="8":
            bank.list_employees
        elif c == "9":
            cust_name = input("ame aus der benutzer: ")
            age = int(input("Alt aus der benutzer: "))
            customer.add_customer(cust_name, age)
        elif c == "10":
            cust_id = int(input("Benutzer-ID: "))
            bank_name = input("Der bank im welche sie/er arbaiten: ")
            customer.assign_bank(cust_id, bank_name)
        elif c == "11":
            cust_id = int(input("id für löschen benutzer: "))
            customer.del_customer(cust_id)
        elif c == "12":
            customer.list_customers()
        elif c == "0":
            print("Ausfhart, danke für du zu whälen eure program!")
            break
        else:
            print("falsche entscheidung")
        if c== 7 or 8 or 12:
            time.sleep(10)