# for i in range(5):
#     print("number" , i)
    
# x = 1
# while x<= 5:
#     print("Number:", x)
#     x+=1
    
# for i in range(1,6):
#     if i == 3:
#         break
#     print(i)

# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i)
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*" , end="")
#     print()

#տպում է զուըգ թվերը
# 1 ին տարբերակը
# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)
#2 րդ տարբերակը
# for i in range( 2,21,2): #սկսում ենք 2 ից  և քայլերը = 2
#     print(i)


#տպում է կենտ թվերը
# for i in range(1,21):
#     if i % 2 == 1:
#         print(i)
    
    
# x = 1
# s = 0
# while x <= 5:
#     s += x
#     x += 1
# print("Գումարը =", s) # = 15



#լուծման 1 ին տարբերակ
# password = " "
# while password != "python234":
#     password =  input(" Enter valid password!! ")
# print(" successful")

#լուծման 2 րդ տարբերակ
while True:
    password = input(" enter password  ")
    if password == "python234":
        print(" successful")
        break