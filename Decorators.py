# def div (a,b):
#     return a/b

# def swiper(func):
#     def inner(a,b):
#         if b==0:
#             b=2
#         return func(a,b)
#     return inner

# div=swiper(div)

# print(div(2,0))



def swaper(func):
    def innerfun(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return innerfun

@swaper
def divid(a,b):
    return a/b

print(divid(2,5))