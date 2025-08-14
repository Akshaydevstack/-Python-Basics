# count=0

# def add():
#     count+=1
#     print(count)



count = 0  # global

def increment():
    global count
    count += 1
    print("Inside function:", count)

increment()
increment()

print("Outside function:", count)
