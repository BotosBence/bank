import time

class bank():
    def add(self, key, value):
      self[key] = value
    def __init__(self): # this defines lists
      self.banknames = {} # bankName, headquarters
      self.bankoffices = {} # bankName, userAccounts - this is (probably) where tech support is
    def add_new_bank(self, user_input = None): # record new bank to bankname list
      while user_input == None:
        user_input = str(input("Type in a name of the bank: "))
        if user_input in self.banknames:
          user_input = None
        else:
          self.banknames.add(user_input, None)
    def check_bank_name(self): # search for bank in bankname
      user_input = str(input("Type in the name of the bank you're searching for: "))
      return (True if user_input in self.banknames else False) # False means it couldn't find the bank
    def addBankOffices(self): # new bank office felvetele
      user_input = None
      while user_input == None:
        user_input = str(input("Type in a name of the office: "))
        if user_input in self.bankoffices:
          user_input = None


# TODO need to be carefull with user_input being None


      # needs to be appended in self to bankoffices
    def smart_check_bank(self): # this function checks if bank doesn't exist in bankname and gives you the chance to record it
      user_input = None
      get = None
      while user_input == None:
        user_input = str(input("Type in the name of the bank: ")).lower()
        if user_input.lower() not in self.banknames:
          while get == None:
            get = input("This bankname doesn't exists! Would you like to record it into bankname?(y/n) ")
            if ["y", "yes"] in get.lower():
              self.banknames.add(user_input, None)
              get = None
            elif ["n", "no"] in get.lower():
              print("understood it will not be recorded")
              get = None
    def smart_bankoffice_del(self): # searches for and deletes bank office, it's smart because it searches
      user_input = None
      get = None
      get2 = None
      while user_input == None:
        user_input = str(input("Type in the name of the bank: ")).lower()
        if user_input.lower() in self.banknames: # searches for name in bankoffices list
          while get == None:
            get = input("This bankname exists! Would you like to delete it?(y/n) ")
            if ["y", "yes"] in get.lower():
              while get2 == None:
                get2 = input("Are you sure?(y/n) ")
                if ["y", "yes"] in get2.lower():
                  del self.banknames[user_input]
                elif ["n", "no"] in get2.lower():
                  pass
                else:
                  get2 = None
            elif ["n", "no"] in get.lower():
              print("understood it will not be deleted")
              get = None
        else:
          print(f"this bankname doesn't exist: {user_input}")
          user_input = None
    def bankoffice_list(self): # lists bankoffices
      print(self.bankoffices)
    def save(self): # probably doesn't work
      f = open('save.txt', 'r')
      f.write(f"{self.banknames} \nself.bankoffices")
      f.close()
    def load(self): # probably doesn't work
      f = open('save.txt', 'r')
      for sor in range(len(f)):
        data = [self.banknames, self.bankoffices]
        data[sor] = f.readlines[sor]
        f.close()


class customer():
  def __init__(self): # this function was made for list_customer function
    self.customers = []
  def last_id(self): # I don't know what this does or why this was created but it needs to be called 
    return 
  def add_customer(self): # add new customer to customer list
    user_input = None
    while user_input == None:
      user_input = input("Type in a name of the office: ")
      if user_input in self.customers:
        return user_input # needs to appended in self
  def list_customer(self): # lists customers from self
    print(self.customers)











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