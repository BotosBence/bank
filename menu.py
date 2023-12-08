from Bank_software import Bank, Customer
language=int(input("Language/Nyelv/Sprache: [1] English, [2] Magyar, [3] Deutsch: "))
bank = Bank()
customer = Customer()
c=()

if language==1:
    def print_menu():
        print("Menü:")
        print("1. Add new bank")
        print("2. Add employee")
        print("3. Check bank ")
        print("4. Check employee ")
        print("5. Delete bank")
        print("6. Delete employee")
        print("7. List banks")
        print("8. List employees")
        print("9. Add new customer")
        print("10. Delete customer")
        print("11. List customers")
        print("12. Assign bank to customer")
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
            enter = input("--- Press enter to continue --- ")
        elif c =="8":
            bank.list_employees
            enter = input("--- Press enter to continue --- ")
        elif c == "9":
            cust_name = input("Enter customer name: ")
            age = int(input("Enter customer age: "))
            bank_name = input("Enter bank name to assign customer: ")
            bank.check_bank(bank_name)
            bank.customer_obj.add_customer(cust_name, age, bank_name)
        elif c == "10":
            cust_id = int(input("Enter customer ID to delete: "))
            customer.del_customer(cust_id)
        elif c == "11":
            customer.list_customers()
            enter = input("--- Press enter to continue --- ")
        elif c == "12":
            user_id = input("Please give the customers ID: ")
            bank_id = input("Please give the banks name that you want your customer to be assigned to: ")
            customer.assign_bank(user_id, bank_id)
        elif c == "0":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid. Please try again.")

if language==2:
    def print_menu1():
        print("Menü:")
        print("1. Új bank")
        print("2. Új dolgozó")
        print("3. Bank létezésének ellenőrzése ")
        print("4. Dolgozó létezésének ellenőrzése ")
        print("5. Bank törlése")
        print("6. Dolgozó törlése")
        print("7. Bankok listája")
        print("8. Dolgozók listája")
        print("9. Új felhasználó")
        print("10. Felhasználó törlése")
        print("11. Felhasználók listázása")
        print("12. Felhasználó bankhoz adása")
        print("0. Kilépés")

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
            employee_name = input("Törlendő dolgozó neve: ")
            bank.del_employee(employee_name)
        elif c == "7":
            bank.list_banks()
            enter = input("--- nyomjon enter-t a tovább haladáshoz --- ")
        elif c =="8":
            bank.list_employees
            enter = input("--- nyomjon enter-t a tovább haladáshoz --- ")
        elif c == "9":
            cust_name = input("Felhasználó neve: ")
            age = int(input("Felhasználó kora: "))
            bank_name = input("Bank ahol dolgozik: ")
            bank.check_bank(bank_name)
            bank.customer_obj.add_customer(cust_name, age, bank_name)
        elif c == "10":
            cust_id = int(input("Felhasználó törléséhez id megadása: "))
            customer.del_customer(cust_id)
        elif c == "11":
            customer.list_customers()
            enter = input("--- nyomjon enter-t a tovább haladáshoz --- ")
        elif c == "12":
            user_id = input("Kérem adja meg az ügyfél id-ját: ")
            bank_id = input("Kérem adja meg a bank nevét amihez hozzá szeretné addni az ügyfelet: ")
            customer.assign_bank(user_id, bank_id)
        elif c == "0":
            print("Kilépés, köszönjük hogy ezt a programot használja!")
            break
        else:
            print("Hibás választás")

if language==3:
    def print_menu2():
        print("menu:")
        print("1. Neue bank")
        print("2. Neue arbeiter")
        print("3. Überprüfung der existenz enier bank ")
        print("4. Überprüfung der existenz enier arbeiter ")
        print("5. Löschen bank")
        print("6. Löschen arbeiter")
        print("7. Liste der banken")
        print("8. Liste der arbaiter")
        print("9. Neue benutzer")
        print("10. Löschen benutzer")
        print("11. Liste der benutzer")
        print("12. Hinzufügen eines Benutzers zur bank")
        print("0. Ausfhart")

    while c!= 0:
        print_menu2()
        c = input("Asgewählten menüponkt: ")

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
            enter = input("--- Drücken Sie die Eingabetaste, um fortzufahren --- ")
        elif c =="8":
            bank.list_employees
            enter = input("--- Drücken Sie die Eingabetaste, um fortzufahren --- ")
        elif c == "9":
            cust_name = input("Benutzer name: ")
            age = int(input("Alt aus der benutzer: "))
            bank_name = input("Name aus der bank im whelche er/sie arbaite: ")
            bank.check_bank(bank_name)
            bank.customer_obj.add_customer(cust_name, age, bank_name)
        elif c == "10":
            cust_id = int(input("ID für löschen benutzer: "))
            customer.del_customer(cust_id)
        elif c == "11":
            customer.list_customers()
            enter = input("--- Drücken Sie die Eingabetaste, um fortzufahren --- ")
        elif c == "12":
            user_id = input("Bitte geben Sie die Kunden-ID an: ")
            bank_id = input("Bitte geben Sie den Namen der Bank an, der Ihr Kunde zugeordnet werden soll: ")
            customer.assign_bank(user_id, bank_id)
        elif c == "0":
            print("Ausfhart, danke für du zu whälen eure program!")
            break
        else:
            print("Falsche entscheidung")