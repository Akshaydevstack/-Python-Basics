def addtwonum(lsitnum):
    sum=10
    print(sum)
    print(sum(lsitnum))

numList=[1,2,34,344,4,2]

try:
    addtwonum()
except:
    print("error")
else:
    print("code works")
finally:
    print("i will run always")
print(sum(numList))