#Q.1-
#Ans:
# age=int(input("Enter your age : "))
# if(age<13):
#     print("You are a Child")
# elif(age>=13 and age<=19):
#     print("You have a Teenager")
# elif(age>=20 and age<=59):
#     print("You are a Adult")
# else:
#     print("You are a Senior")

#Q.2-
# day="Thrusday"
# age=16
# price=12 if age>=18 else 8
# if(day=="Wednesday"):
#     price-=2

# print("Movie Ticket Price is: $",price)

#Q.3-
# score=900
# if(score>100):
#     print("Score can not be more than 100")
#     exit()

# if(score>=90):
#     print("A")
# elif(score>=80):
#     print("B")
# elif(score>=70):
#     print("C")
# elif(score>=60):
#     print("D")
# else:
#     print("F")

# Q.4-
# status={"ripe":{"Banana":"Yellow","Apple":"Red"},"Unripe":{"Banana":"Green","Apple":"Green"},"overripe":{"Banana":"Brown","Apple":"Black"}}
# fruit=input("Enter Fruit Name: ")
# color=input("Enter Fruit Color: ")
# if color in status["ripe"].get(fruit):
#     print("This Fruit is ripe")
# elif color in status["Unripe"].get(fruit):
#     print("This Fruit is Unripe")
# if color in status["overripe"].get(fruit):
#     print("This Fruit is Overripe")

# Q.5-
# wether={"Sunny":"Go for a walk","Rainy":"Read a Book","Snowy":"Build A snowman"}
# rwether=input("Enter the Wether : ")
# if rwether in wether:
#     print(wether.get(rwether))

# Q.6-
# distance=15
# if(distance<3):
#     transportation="Walk"
# elif(distance<15):
#     transportation="Bike"
# else:
#     transportation="Car"
# print(transportation)

# Q.7-
# order_size="Medium"
# extra_shot=True
# if extra_shot:
#     coffee=order_size+" coffee with an extra shot"
# else:
#     coffee=order_size+" coffee"
# print("order : ",coffee)

# Q.8-
# password="123d"
# password_length=len(password)
# if(password_length<6):
#     check="weak"
# elif(password_length<10):
#     check="medium"
# else:
#     check= "strong"

# print(check +" password")

# Q.9-
# year=2021
# is_leap_year=((year%4==0 and year%100!=0) or year%400==0)
# if(is_leap_year):
#     print("This is a leap year ")
# else:
#     print("This is not leap year")