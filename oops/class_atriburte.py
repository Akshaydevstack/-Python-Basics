# class Student:
#     collage = "HSAS"

#     @classmethod
#     def change_collage(cls, collage):
#         cls.collage = collage

#     def __init__(self,name,deprt):
#         self.name=name
#         self.deprt=deprt


# student1= Student("Akshay","BCA")

# print(student1.name)
# print(student1.collage)
# student1.change_collage("VHSE")
# print(student1.collage)


# class student:
#     school="Gvhss"

#     def __init__(self,name,student_class,age,maths,english,it):
#         self.name=name
#         self.student_class=student_class
#         self.age=age
#         self.maths=maths
#         self.english=english
#         self.it=it
    
#     @property
#     def avrg(self):
#         return (self.english+self.maths+self.it)/3
    
#     @classmethod
#     def change_collage(cls,school):
#         cls.school= school


# Akshay=student("Akshay","12th",17,76,91,80)
# Akshay.english=100
# student.school="sdsdsd"
# print(Akshay.avrg)
# print(student.school)
# ajmal=student("Akshay","12th",17,100,100,100)
# print(ajmal.school)                                                                                                                                            



strings="Helloworld"

count={}

for ch in strings:
    if(ch.isalpha):
        ch=ch.lower()
        count= count.get(ch,0)+1 

print(count)