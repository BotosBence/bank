class bank():
    def add(self, key, value):  # this just adds a key and a value to a dictonary
        self[key] = value

    def __init__(self):  # this defines lists
        self.banknames = {}  # bankName, headquarters
        self.employees = {}  # bankName, userAccounts - this is (probably) where tech support is

    def add_new_bank(self):  # record new bank to bankname list
        user_input = input("Name of the bank: ")
        if user_input is not None:
            self.banknames.add(user_input, None)
        else:
            return False

    def check_bank_name(self):  # search for bank in bankname
        user_input = input("Type in the name of the bank you're searching for: ")
        return True if user_input in self.banknames else False, user_input
    def check_employee_name(self):  # search for employee in employees
        user_input = input("Type in the name of the employee you're searching for: ")
        return True if user_input in self.employees else False, user_input

    def addEmployee(self):  # new employee recording
        user_input = input("Name of the employee: ")
        if user_input is not None:
            self.employees.add(user_input, None)
        else:
            return False

    def smart_check_bank(self, get, user_input):  # function checks if bank doesn't exist in bankname and gives you the
        # chance to record it
        "There is a bank with that name" if get is True else "there are no banks with that name"
        while get:
            question = input("Would you like to record a new bank?[y/n]: ")
            if question:
                self.banknames.add(user_input, None)

    def smart_bankoffice_del(self):  # searches for and deletes bank office, it's smart because it searches

    def bankoffice_list(self):  # lists bankoffices
        print(self.employees)

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
        self.customers = []

    def last_id(self):  # I don't know what this does or why this was created but it needs to be called
        return

    def add_customer(self):  # add new customer to customer list
        user_input = None
        while user_input is None:
            user_input = input("Type in a name of the office: ")
            if user_input in self.customers:
                return user_input  # needs to appended in self

    def list_customer(self):  # lists customers from self
        print(self.customers)

