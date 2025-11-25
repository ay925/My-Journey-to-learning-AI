# Q.1-
# number=[1,-2,3,-4,5,6,-7,-8,9,10]
# count=0
# for num in number:
#     if(num>0):
#         count+=1
# print("Positive number in list is : ",count)

# Q.2-
# n=50
# sum=0
# for number in range(1,n+1):
#     if(number%2==0):
#         sum+=number
# print("Sum is:",sum)

# Q.3-
# num=10
# for i in range(1,num+1):
#     if(i==5):
#         continue
#     for j in range(1,11):
#         print(i,"X",j,"=",i*j)
#     print()

# Q.4-
# string="ABCDEF"
# revstring=""
# for i in string:
#    revstring=i+revstring
# print(revstring)

# Q.5-
# input_str="Anuu"
# non_repeted_char=""
# for char in input_str:
#    if input_str.count(char)==1:
#       non_repeted_char+=char
# print(non_repeted_char) 
  
# Q.6-
# num=5
# factorial=1
# i=1
# while(i<=num):
#     factorial*=i
#     i+=1
# print("Factorial:",factorial)

# Q.7-
# while True:
#     number=int(input("Enter the number 1 to 10 : "))
#     if 1 <=number <=10:
#         print("Thanks!")
#         break
#     else:
#         print("Invalid number,try again")

# Q.8-
# number=5
# is_prime=True
# if number>1:
#     for i in range(2,number):
#         if (number %i)==0:
#             is_prime=False
#             break
#     if(is_prime):
#         print("This number is prime")
#     else:
#         print("This number is composite ")

# Q.9-
# items=["apple","banana","orange","apple","mango"]
# for fruit in items:
#     if(fruit.count!=1):
#         print("fruit name:",fruit)
#         break
    
# Q.10-
# import time
# wait_time=1
# max_retries=5
# attempt=0

# while(attempt<max_retries):
#     print("Attempt",attempt+1,"-wait time",wait_time)
#     time.sleep(wait_time)
#     wait_time*=2
#     attempt+=1;
    

