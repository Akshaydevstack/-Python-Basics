from collections import Counter

# single inheritance
#...............................
# class car:

#     @staticmethod
#     def start():
#         print("Car started")

#     @staticmethod
#     def stop():
#         print("Car stoped")    

# class Polo(car):
#     def __init__(self,name):
#         self.owner_name=name

# car1= Polo("Akshay")
# print(car1.owner_name)
# print(car1.start())



# Multilevel Inheritance
#..............................

# class car:

#     @staticmethod
#     def start():
#         print("Car started")

#     @staticmethod
#     def stop():
#         print("Car stoped")    

# class Toyota(car):
#     def __init__(self,name):
#         self.owner_name=name


# class Fornuter(Toyota):
#     def __init__(self, fule_type):
#         self.fule_type= fule_type
        

# car1= Fornuter("Petrol")

# print(car1.fule_type)



#multiple iheritance
#.....................


# class A:
#     varA= "Variable A"

# class B:
#     varA="Variable B"

# class c (A,B):
#     varC="Variable C"

# test1= c()

# print(test1.varC)
# print(test1.varA) # Order matters: A first, then B


#Super Method.....


# class car:
#     def __init__(self,type):
#         self.type=type
#     @staticmethod
#     def start():
#         print("Car started")

#     @staticmethod
#     def stop():
#         print("Car stoped")    

# class Polo(car):
#     def __init__(self,name,type):
#         self.owner_name=name
#         super().__init__(type)
# car1= Polo("Akshay","Petrol")
# print(car1.owner_name)
# print(car1.start())
# print(car1.type)


name="ak2sha34y"
count=0
for ch in name:

    if(ch.isnumeric()):
        count+=1

print(count)

