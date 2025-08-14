try:
    num= int(input("Enter a number"))
    print(10/num)
except (ValueError,ZeroDivisionError) as e :
    print(f"{e}")
else:
    print("division done")
finally:
    print("I always run")        



