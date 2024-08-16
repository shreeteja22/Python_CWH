a = [12,13,45,36,674,434,65,8,54,3,36678,765432]
# index = 0
# for number in a:
#     print(number)
#     if (index==4):
#         print("Enumerate function")
#     index += 1
# index = 0.......(no need of this value too)
for index,number in enumerate(a):    #enumerate just makes the work of adding plus 1 to index or other functions
    print(number)
    if (index==4):
        print("Enumerate function")
    # index += 1.........(no need of this)