# def greet():
#     print(" Hi Function")
# greet()

# def greet_user(name):
#     print("Hi" , name)
# greet_user("Ann")
# greet_user('Jon')

# #վերադարձվող արժեք
# def square(x):
#     return x*x
# print(square(5))

# #կարող ենք տալ դեֆոլտ արժեք

# def greet_user(name="gest"):
#     print("Hi" , name)
# greet_user()
# greet_user("Ann")




# def say_hello():
#     print("Helo world")
# say_hello()

# def multiply(a,b):
#     return a*b
# print(multiply(5,6))

# #ֆունկցիա որը ստանում է թիվ և ստուգում  կենտ է թե զույգ
# def num_even_odd(x):
#   if x % 2 == 0:
#     return " even"
#   else:
#       return "odd"
# print(num_even_odd(5))
# print(num_even_odd(20))
    
    
# #ֆունկցիա որը հաշվում է ֆակտորիալ

# def factorial(n):
#     result = 1
#     for i in range(1 , n+1):
#         result *=i
#     return result
# print(factorial(5))

# while True:
#     password = input("enter password")
#     if password == "py":
#         print("success")
#         break
    
    
def my_message(name, age):
    print(name, age , "years old")
my_message("Rita" ,25)

def sum(a, z):
   return a+z
print(sum(5,8))


def even_odd(x):
    if x % 2 ==0:
        print(" num iz odd")
    else:
        print("num is even")
even_odd(21)

    