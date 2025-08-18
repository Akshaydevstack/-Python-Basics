# def main_function():
#     def local_function():
#         nonlocal test
#         test="Test from local function"
#     def gobal_function():
#         global test
#         test= "test form global function"
#     test="Test form main function"

#     print(test)
#     local_function()
#     print(test)
#     gobal_function()
#     print(test)

# main_function()
# print(test)

x=0

def increment():
    global x
    y=0
    x+=1
    def add1():
        nonlocal y
        y+=1
        print(y)
    add1()

increment()
increment()
increment()
print(x)