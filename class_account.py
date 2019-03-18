class account:
    def __init__(self,num,balance):
        self.num=num
        self.balance=balance

    def __str__(self):
        return "Account number is : " + str(self.num) +"\n" \
               "Balance is : " + str (self.balance) +"\n"

class checking(account):
    def __init__(self, num, balance,fee):
        account.__init__(self,num,balance)
        self.fee=fee

    def __str__(self):
        retstr="Account type = Checking \n"
        retstr+=account.__str__(self)
        return retstr

    def printfee(self):
        return "fee is : " + str(self.fee)

    def deposit(self,amount):
        print ("Trying to deposit " + str(amount))
        self.balance+=amount

    def withdrawal(self,amount):
        print ("Trying to withdraw "+ str(amount) )
        if amount > self.balance:
            print ("Not Enough funds!!")
        else:
            self.balance= self.balance - amount - self.fee


c1= checking(123,1200,1)
print (c1)
c1.deposit(1000)
print (c1)
c1.withdrawal(2000)
print (c1)