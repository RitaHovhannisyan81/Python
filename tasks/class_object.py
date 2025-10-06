# class Person:
#     def __init__(self,name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
# tom = Person("Tom", 44, "male/female")# male-տղա/female-կին
# print(tom.name)
# print(tom.age)



# nams = []
# for i in range(1,20):
#     nams.append(i**2)
# print(nams)

# nums = [i**2 for i in range(1,11)]
# print(nums)

#-----lambda-----

# def define_cube(y):
#     return y*y*y

# lambda_cube = lambda y: y*y*y
# print(lambda_cube(2))
# print(define_cube(2))

#---  filter()
# my_list = [1,2,3,4,5,6,7,8,9, 10,20]
# new_list = list(filter(lambda x:(x%2==0),my_list))
# print(new_list)

# #--- map()
# current_list = [1,2,3,4,5,6,7,88]
# new_current = list(map(lambda x: x*2, current_list))
# print(new_current)

# #--- reduce()
# from functools import reduce

# m_list =[2,8,6,4,5,9]
# summa = reduce((lambda x,y : x+y),m_list)
# print(summa)

# #--- table()
# tables = [lambda x = x: x*5  for x in range(1,10)]
# for table in tables:
#     print(table())


#--> < =
# max_num = lambda a,b : a if a > b else b
# print(max_num(5,8))


#-------------գտնում է երկրորդը մեծությամբ էլեմենտը
# my_new_list = [ [8,6,9], [ 0,22,6,99], [3,5,8,7]]
# sorted_list = lambda x : (sorted(i)for i in x)
# second_largest = lambda x, func:[y[len(y)-2]for y in func(x)]
# result = second_largest(my_new_list,sorted_list)
# print(result)


#---Ինչպես ստեզծել ֆայլ և մեջը տեքստ գրել

# with open ("data.txt", "w") as f:
#     f.write("Data Science with python!\n")
    
# with open("data.txt", "r") as f:
#     content = f.read()
#     print(content)

import numpy as np
# #տպել 10 ից 50 միջակայքի այն թվերը որոնք 5 են բազմապատիկ
# x = np.arange(10,50, 5)
# print(x)

# #Ստեղծիր 3x3 մատրից, որի մեջ կլինեն պատահական թվեր (0–ից 10)։
# mat = np.random.randint(0,10,(3,3))
# print(mat)

# #Վերցրու այդ մատրիցից․
# second_row = mat [1,:]
# third_col = mat[:,2]
# print("second row :", second_row)
# print("Third column :", third_col)

# #Գտիր mean, median, std, min, max այդ մատրիցի համար։

# print(" Mean:", np.mean(mat))
# print("Median:",np.median(mat))
# print("Std:", np.std(mat))
# print(" Min:",np.min(mat))
# print("Max:", np.max(mat))

# 
import pandas as pd
import numpy as np
import zipfile

with zipfile.ZipFile("anime-recommendations-database.zip", "r") as zip_ref:
    zip_ref.extractall(".")