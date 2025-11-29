# try:
#     number1=int(input('Enter the number 1 :'))
#     number2=int(input('Enter the number 2 :'))
#     result=number1/number2
#     print(round(result,2))
# except ZeroDivisionError:
#     print('you cannot be divide by 0')
# except ValueError:
#     print("You can not divide by string")

def password(password):
    if len(password)<8:
        raise Exception ("possword must be >=08")
    print("password is strong")
try:
    inputpassword=input("Enter your Password : ")
    password(inputpassword)

except Exception as e:
    print(e)
