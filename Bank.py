class XBank:
    loggedinCounter = 0
    def __init__(self,theatmpin,theaccountbalance,thename):
        self.atmpin = theatmpin
        self.accountbalance = theaccountbalance
        self.name = thename

    def CollectMoney(self, amounttowithdraw):
        if(amounttowithdraw > self.accountbalance):
            print("Sorry we are unable to process at this time")
        else:
            print("Collect your cash... Thanks fro banking with XBank")

    def  Changepin(self, newPin):
        self.atmpin = newPin
        print("Your pin has been changed... Thanks for banking with XBank")
    @classmethod
    def NoofCustomersLoggedin(cls):
        print(f"We have a total of {XBank.loggedinCounter} users that have logged in")
        

f = open("DataBase.txt",'r')
#print(f.readline())
password = []
accountB = []
name = []
breaker = []
for x in f:
    breaker = x.split(' ')
    password.append(breaker[0])
    accountB.append(breaker[1])
    name.append(breaker[2])
    break


print("Enter your pin.......")
pasw = input()
if (pasw == password[0]):
    customer = XBank(password[0],accountB[0],name[0])