class account:
    def __init__(self,num,balance):
        self.num=num
        self.balance=balance

    def __str__(self):
        return "Account number is : " + str(self.num) +"\n" \
               "Balance is : " + str (self.balance) +"\n"

    def deposit(self,amount):
        print ("Trying to deposit " + str(amount))
        self.balance+=amount

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

    def withdrawal(self,amount):
        print ("Trying to withdraw "+ str(amount) )
        if amount > self.balance:
            print ("Not Enough funds!!")
        else:
            self.balance= self.balance - amount - self.fee


class savings(account):
    def __init__(self,num,balance):
        account.__init__(self,num,balance)

    def __str__(self):
        retstr = "Account type = Savings \n"
        retstr += account.__str__ (self)
        return retstr

    '''
    test
    '''

    def withdrawal(self,amount):
        print ("Trying to withdraw "+ str(amount) )
        if amount > self.balance:
            print ("Not Enough funds!!")
        else:
            self.balance= self.balance - amount


c1= checking(123,1200,1)
print (c1)
c1.deposit(1000)
print (c1)
c1.withdrawal(2000)
print (c1)



c2= savings(234,2200)
print (c2)
c2.deposit(2000)
print (c2)
c2.withdrawal(2000)
print (c2)


print ("Displaying all accounts .... \n")
ac=[c1,c2]
for i in range(0,len(ac)):
    print(ac[i])
