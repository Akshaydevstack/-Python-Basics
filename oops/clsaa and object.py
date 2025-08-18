# class Student:
#     name="Akshay"

# s1=Student()
# print(s1.name)

# class Cars:
#     color="blue"

# c1=Cars()
# c2= Cars()

# print(c1.color)
# print(c2.color)

# class Student:
#     collage="Abcd collage" # class atribute
#     def __init__(self,name,marks):  # constrecter
#         self.name=name # object atribute
#         self.marks=marks
#         print("Adding to DB")


# s1= Student("Akshay",23)
# print(s1.name,s1.marks)


# class Student:
#     collage="Abcd Collage"
#     def __init__(self,name,marks):
#         self.name= name
#         self.marks=marks

#     def hello(self): # methods in class or object
#         print(f"My name is {self.name}")
#     def get_marks(self):
#         return self.marks


# s1= Student("Akshay",100)
# print(s1.marks)
# print(s1.name)
# print(s1.collage)
# print(Student.collage)
# s1.hello()
# print(s1.get_marks())


##############################

# practice Qus

class Student:
    collage = "Abcd collage"

    def __init__(self, name, *marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks)/len(self.marks)

    @classmethod
    def chnage_collage(cls,name):
        cls.collage=name
        print(f"Hello guys {Student.collage}")

    @staticmethod
    def greet():
        print("hiiii")

s1 = Student("Akshay", 23, 45, 67)
print(s1.average())
print(s1.name)
s1.name = "Vimal"
print(s1.name)
print(Student.chnage_collage("Vimal jothi"))
s2= Student("Ajmal",24)
print(s2.collage)
print(s1.greet())
###################################
