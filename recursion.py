# def fact(num):
#     if num == 1:
#         return 1
#     else:
#         return num * fact(num-1)


# print(fact(5))

def prtnum(start,stop):
    if(start==stop):
        return
    else:
        print(start)
        return prtnum(start+1,stop)
    

prtnum(0,5)