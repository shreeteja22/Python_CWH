# name = str(input("ENTER YOUR NAME : "))
# print("Hello," + name)      

# letter = "Walter white"
# letter1 = "Mutukundu"
# letter2 = "Srinivasulu"
# len1 = len(letter)       #checking length
# len2 = len(letter1)
# len3 = len(letter2)
# print(len1 , len2 , len3)

# letter = "ShreetejaSrinivasuluMutukundu"
# len1 = len(letter)
# print(letter[0:20])      #slicing 

# letter = "ShreetejaSrinivasuluMutukundu"
# len1 = len(letter)            #middle letter slicing
# print(letter[9:20])   

# # upper case ka method
# a = "Harry!"
# print(len(a))       #(letter keywords)
# print(a.upper())
# print(a.replace("Harry", "Teja"))   #letter keywords
# print(a.rstrip("!"))

# a = "harry ! Teja Teja Teja Teja Teja !"
# # print(a.split(" "))
# # print(a.capitalize())   #capitalise starting letter ko capital karke baki sb small kardeta
# # print(a.count("Teja"))
# print(a.endswith("Reddy"))   #ye value Boolean(true aur false) mai hi deta ...agar endswith(teja) hai toh true ...if not then false


# x = int(input("enter your number which suits x : "))

# match x:

#     case 0 :
#         print("x is zero")

#     case 4:
#         print("case is 4")

#     case _:
#         print(x)


# list = [ "red" , "yellow" , "orange" , "purple"]

# for i in list :
#     print(i)
#     for t in i:
#         print(t)


# i = int(input("enter your first number: "))
# while (i<=300):
#     print(i)
#     i += 1            #wile loop ka method

# i = int(input("enter your first number: "))
# while (i>0):
#     print(i)  #minus one esach variable
#     i -= 1


# for i in range(16):
#     print("5 X", i+1 ,"=" , 5 * (i +1))
#     if (i==9):
#       break


# for i in range(16):
#     if(i>=12):
#         print("Hello World")
#         continue
# print("5 X", i+1 ,"=" , 5 * (i +1))


# list = ["Harry" , 34 , 54 , 424 , "teja"]
# # print(list)
# print(list[:-4])
# l = [1,3,2,4,24,6,775,48,24]
# print(l)
# l.append(92)
# l.sort() if you want descending order use reverse=true
# print(l.index(4))
# print(l)
# m = [234,54,32]
# l.extend(m)
# print(l)



# tuples
# tup = (1,2,3,4,5)
# print(len(tup))
# tup2 = tup[1:4]
# print(tup2)
# res = tup.index(3)
# print(res)
