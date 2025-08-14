
def outer():
   

    def inner():
        count=0
        count += 1
        return count
    return inner


innerfun = outer()

print(innerfun())
print(innerfun())
print(innerfun())
