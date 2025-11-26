# Q.1-
# def squrenumber(n):
#     return n*n

# squre_number=squrenumber()

# print(squre_number)

# Q.2-
# def sum(a,b):
#     return(a+b)

# result =sum(3,4)
# print(result)

# Q.3-
# def multiply(p1,p2):
#     return p1*p2

# print(multiply(5,4))
# print(multiply('a',5))
# print(multiply(5,'a'))

# Q.4-
# from math import pi
# def area_circumfarance(radius):
#     circumfarence=round(2*pi*radius,2)
#     area=round(pi*(radius**2),2)
#     return area,circumfarence
# print(area_circumfarance(10))
# print(pi)

# Q.5-
# def greet(name="user"):
#     return "Hello,"+name+" !"

# print(greet())

# Q.6-
# cube=lambda x:x**3
# print(cube(3))

# Q.7-
# def sum_all(*args):
#     return sum(args)
# print(sum_all(1,2))

# Q.8-
# def print_kwargs(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")

# print_kwargs(name="shaktiman",power="lazer")
# print_kwargs(name="shaktiman")

# Q.9-
# def even_generator(limit):
#     for i in range(2,limit+1,2):
#         yield i
# for num in even_generator(10):
#     print(num)

#Q.10-
def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)
print(factorial(100))