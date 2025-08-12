# print(f"My name is {name}") not posible to acces varible before inisilisation
name = "Akshay"  # string
age = 24  # number
mark = 123.873  # floating variables
job = False  # boolen


print(f"My name is {name} {mark}")  # F string usage

if age < 50:
    place = "kannur"
    print(f"place{place}")
else:
    print("hii")

a, b, c = 10, 20, 30  # single line assignement

print(a)
print(b)
print(c)

PI = 3.14  # constant declaration

print(PI)

print(type(PI))

print(isinstance(PI ,float))
