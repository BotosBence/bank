class bank():
    banknames = [] # bankName, headquarters
    bankoffices = [] # bankName, userAccounts


    def __init__(self): # this defines lists
      pass
    def add_new_bank(self, banknames): # record new bank to bankname list
      user_input = None
      while user_input == None:
        user_input = input("Type in a name of the bank: ")
        if user_input in banknames:
          user_input = None
    def check_bank_name(self, banknames): # search for bank in bankname
      user_input = input("Type in the name of the bank you're searching for: ")
      return (user_input if user_input in banknames else None) # None means it couldn't find the bank

# TODO check_bank_name needs to be called in self

    def addBankOffices(self, bankoffices): # new bank office felvetele
      user_input = None
      while user_input == None:
        user_input = input("Type in a name of the office: ")
        if user_input in bankoffices:
          user_input = None
      # needs to be appended in self to bankoffices
    def smart_check_bank(self, banknames): # this function checks if bank doesn't exist in bankname and gives you the chance to record it
      user_input = None
      while user_input == None:
        user_input = input("Type in a name of the bank: ")
        if user_input not in banknames:
          user_input = input("Type in a name of the bank: ") # needs to be appended to banknames
    def smart_bankoffice_del(self, bankoffices): # searches for and deletes bank office 
      # it's smart because it searches
      user_input = None
      while user_input == None:
        user_input = input("Type in a name of the office you wish to execute from the list: ")
        if user_input in bankoffices:
          return user_input # needs to be removed in self
    def bankoffice_list(self, bankoffices): # lists bankoffices
      print(bankoffices)

class customer():
  def __init__(self): # this function was made for list_customer function
    customers = []
  def last_id(self): # I don't know what this does or why this was created
    pass
  def add_customer(self, customers): # add new customer to customer list
    user_input = None
    while user_input == None:
      user_input = input("Type in a name of the office: ")
      if user_input in customers:
        return user_input # needs to appended in self
  def list_customer(self, customers): # lists customers
    print(customers)












    # def bank_up(self): # 
    #   pass
    # def bankaccount_up(self):
    #   pass
    # def bankaccount_list(self):
    #   pass
    # def bankaccount_del(self):
    #   pass
    # def user_up(self):
    #   pass
    # def user_list(self):
    #   pass
    # def user_del(self):
    #   pass