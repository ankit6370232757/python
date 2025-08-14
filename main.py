# print("We are learning python ")

# # For comment we use #
# """" this is doc string use for multiline comment"""

# SheryiansSchool = "Students" #pascal case
# sheryiansSchool ="students" #camel case


# a= 12
# b =56.6
# c = 12/3

# v = 34j
# print( type(a))
# print( type(b))
# print( type(c))
# print( type(v))


# st='123455555 efefhehfe @#$$##%^^^#'
# print(type(st))

# b = True
# t = False
# print(type(b))
# print(type(t))

# """""strings"""
# a = "A"
# print(ord(a))
# b ="😂"
# print(ord(b))

# a ="ANKIT"
# print(a[3],a[-2])

# a ="ANKIT RATH"
# print(a[0:3:1])

# num = input("Tell me a number")
# print(num)

# a = 5
# b = 32
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(5**3)
# print(32%5)


# print(12+4-3)

# a= 20
# print(a+(a+20))

# a= 12
# b = 12

# print(a== b)
# print ( a != b )
# print( a>= b)

# print( 23 > 78)
#compound assignmet operations

# a = 20

# a += 20
# a += 40
# a += 60
# a-=
# a*=
# a/=
# a//=
# a**=

# print(a)

# a = 12.1
# b = 12 

# print(a == b)

# print(a != b)

# print(a > b)
# print(45 < 67)
# print(23 >= 23)
# print(45 <= 45)


# print(ord("A"))
# print(ord("B"))

# print("ABC" > "ACD")

# print("A" > 34)

# print(12 >20 and 123 > 100 and 34 == 34 and 45 < 90)

# print(12 !=12 or 23 ==45 or 67 == 56 or 10 > 5)

# print(not 12 == 12)

#IF else 

# a = 6

# if a > 10:
#     print("I will do task A")

# else:
#     print("I will do task B")

# money = int(input("please provide me the money :- "))

# if money == 10:
#     print("I will have a choco bar icecream")

# elif money == 20:
#     print("I will have a mangodolly")

# elif money == 30:
#     print("I will have a frosty")
    
# else:
#     print("I will have a cone")

# num1 = int(input("pleae tell your first number "))
# num2 = int(input("pleae tell your second number "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")

# else:
#     print("Both the numbers are same")


# gen = input("please tell your gender as character (M or F):-")

# if gen == 'M' or gen == 'm':
#     print("Good morning SIR")
# elif gen == "F" or gen == 'f':
#     print("Good morning MAM")

# else:
#     print("Unidentified gender")


# num = int(input("please tell your number :- "))

# if num%2 == 0:
#     print("even number")

# else:
#     print("Odd number")

# name = input("please tell your name : - ")
# age = int(input("now tell your age :- "))

# if age >=18 :
#     print(f"hello {name} you are a valid vote")

# else:
#     print(f"hello {name} you are not a valid vote")

# year = int(input("tell your year :- "))

# if year %100 == 0 and year %400 == 0:
#     print("Its a leap year")

# elif  year %100 != 0 and year %4 ==0:
#     print("Its a leap year")

# else:
#     print("its a normal year")

t = int(input("please tell the temprature :- "))

if t < 0:
    print("Freezing cold")

elif t >= 0 and t <10:
    print("very cold")

elif t >= 10 and t <20:
    print("cold")

elif t >= 20 and t <30:
    print("plesant")

elif t >= 30 and t <40:
    print("hot")

else:
    print("temprature is very hot ")



