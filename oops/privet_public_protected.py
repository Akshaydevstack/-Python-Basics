class Accont:
    bank_name="ICICI"

    def __init__(self,acc_no,acc_password):
        self.acc_no=acc_no
        self.__acc_password= acc_password
    
    def reset_pass(self):
       return self.__acc_password
acc_1=Accont(22123232,"Akshay@989w")

print(acc_1.acc_no)
print(acc_1.reset_pass())
print(acc_1.__acc_password)
