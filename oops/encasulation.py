# class Cars:
#     def __init__(self):
#         self.acc=False
#         self.cluch=False
#         self.brk=False
#     def start(self):
#         self.acc=True
#         self.brk=True
#         print("Car Started.....")
# polo= Cars()

# polo.start()

class Accoiunt:
    def name():
        print("hello")
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance
    def credit(self,amount):
        self.balance+=amount
        return f"Your account: {self.acc_no} credited with {amount} current balce is ",self.balance
    def debit(self,amount):
        self.balance-=amount
        return f"Your account: {self.acc_no} debited with {amount} current balce is ",self.balance
    def accbalance(self):
        return f"Your balnce is : {self.balance} "


person1= Accoiunt(100,1000) 
person2= Accoiunt(200,2000)
print(person1.acc_no,person1.balance)
print(person1.credit(200))
print(person1.debit(200))
print(person1.accbalance())
print(person2.acc_no,person2.balance)
print(person2.credit(200))
print(person2.debit(200))
print(person2.accbalance())
# del person1.acc_no
print(person1.acc_no)
Accoiunt.name()