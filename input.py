# a=input('enter your name')
# print("my name is",a)
# print("my name is",a,sep=" ")
# print("my name is",int(a))
# print("my name is",float(a))
# print("my name is"+' '+str(a)) 
# print("my name is"+' '+a)

# a=int(input('enter your phone number:'))
# print("your phone number is",a)          # your phone number is 2343
# print("your phone number is",a,sep=" ")  # your phone number is 2343
# print("your phone number is",int(a))     # your phone number is 2343
# print("your phone number is",float(a))   # your phone number is 2343.0
# print("your phone number is"+' '+str(a))   # your phone number is 2343

# a=float(input('enter your BMI:'))
# print("your BMI is",a)             #  your BMI is 45.9
# print("your BMI is",a,sep=" ")     #  your BMI is 45.9
# print("your BMI is",int(a))          #  your BMI is 45
# print("your BMI is",float(a))      #  your BMI is 45.9
# print("your BMI is"+' '+str(a))    #  your BMI is 45.9

# name=input("enter your name:")
# age=int(input("enter your age:"))
# per=float(input("enter your graduation percentage %:"))
# print(name,age,per)       # prava 23 75.0
# print(age,name,age)         # 23 prava 23
# print(age,name,per)           #  23 prava 75.0  
# print(name)                 # prava

# name=input("enter your name:")
# age=int(input("enter your age:"))
# per=float(input("enter your graduation percentage :"))

# print("your name is",name,"your age is",age, \
#     "your graduation percentage is",per)     # your name is prava your age is 23 your graduation percentage is 75.0

# print("your name is"+' '+name,"and age is",age, \
#     "graduation percentage is",str(per)+'%') # your name is prava and age is 23 graduation percentage is 90.0%
# print("your name is %s and age is %d.\
#     graduation percentage is %.2f"%(name,age,per))

# print(" your name is {} and age is {}.\
# graduation percentage is {}".format(name,age,per)) # your name is prava and age is 23.graduation percentage is 99.0

# print(" your name is {1} and age is {o}.\
# graduation percentage is {2}".format(name,age,per))

# print(" your name is {name} and age is {age}.\
# graduation percentage is {per}".format(name,age,per))

# a=int(input())    # 2
# b=int(input())    # 3
# print(a+b)        # 5

# a,b=[float(x) for x in input('enter any two number: ').split()]
# print(a+b)     #  2 4 = 6.0

# a=[float(x) for x in input().split(',')]
# print(sum(a))       #  4=4.0

# import math
# a=[float(x) for x in input().split(',')]
# print(math.prod(a))     # 6=6.0

# x='123456789'
# print(int(x[0])+int(x[-1]))  # we are adding index'0' and index'1' postion.so, 1+9=10