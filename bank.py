def add(self, key, value):  # this just adds a key and a value to a dictonary
    self[key] = value


class bank():
    def __init__(self):  # this defines lists
        self.banknames = {}  # bankNames, employees list, customer list
        self.employees = {}  # employeeName, bankName Where employee is working - this is (probably) where tech support is

    def add_new_bank(self, user_input = None):  # record new bank to bankname list
        while user_input is None:
            user_input = input("Name of the bank: ")
            if user_input not in self.banknames:
                self.banknames.add(user_input, None)
            else:
                user_input = None

    def rename_bank(self, user_input = None):  # record new bank to bankname list
        while user_input is None:
            user_input = input("Name of the bank: ")
            if user_input not in self.banknames:
                self.banknames.add(user_input, None)
            else:
                user_input = None

    def check_bank_name(self):  # search for bank in bankname
        user_input = input("Type in the name of the bank you're searching for: ")
        return True if user_input in self.banknames else False, user_input

    def check_employee_name(self):  # search for employee in employees
        user_input = input("Type in the name of the employee you're searching for: ")
        return True if user_input in self.employees.keys() else False, user_input

    def addEmployee(self, user_input = None):  # new employee recording
        while user_input is None:
            user_input = input("Name of the bank where you want to record the employee: ")
            if user_input in self.banknames:
                bank = user_input
            else:
                user_input = None
        while user_input is None:
            user_input = input("Name of the employee: ")
            if user_input not in self.employees:
                self.employees.add(user_input, bank)
            else:
                user_input = None

    def smart_check_bank(self, get = True, user_input = None):  # function checks if bank doesn't exist in bankname and gives you the
        # chance to record it
        while get:
            question = input("Would you like to record a new bank?[y/n]: ")
            if question.lower() is "y":
                self.banknames.add(user_input, None)
            else:
                question = input("Are you sure?[y/n]: ")
                if question.lower() is "y":
                    get = False



    def smart_bankoffice_del(self, get = True, user_input = None):  # searches for and deletes bank office, it's smart because it searches
        while get:
            question = input("Would you like to record a new bank?[y/n]: ")
            if question.lower() is "y":
                self.banknames.add(user_input, None)
            else:
                question = input("Are you sure?[y/n]: ")
                if question.lower() is "y":
                    get = False
    def bankoffice_list(self):  # lists bankoffices
        print(self.employees.keys())

    def save(self):  # probably doesn't work
        f = open('save.txt', 'r')
        f.write(f"{self.banknames} \nself.bankoffices")
        f.close()

    def load(self):  # probably doesn't work
        f = open('save.txt', 'r')
        for sor in range(len(f)):
            data = [self.banknames, self.employees]
            data[sor] = f.readlines[sor]
            f.close()

class customer():
    def __init__(self):  # this function was made for list_customer function
        self.customers = {}

    def last_id(self):  # I don't know what this does or why this was created but it needs to be called in self.customers
        pass

    def add_customer(self):  # add new customer to customer list
        user_input = None
        while user_input is None:
            user_input = input("Type in a name of the office: ")
            if user_input in self.customers:
                return user_input  # needs to appended in self

    def list_customer(self):  # lists customers from self
        print(self.customers)