# username="chaiaurcode"
# def func():
#     # username = "chai"
#     print(username)
# x=99
# def func2(y):
#     z= x+y
#     return z
# print(func2(3))
x=99
# def func():
#     global x
#     x=12
# func()
# print(x)
def chaicoder(num):
    def actualfun(x):
        return x**num
    return actualfun

f=chaicoder(2)
g=chaicoder(3)
print(f(3))
print(g(3))