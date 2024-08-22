for i in list :
    print(i)
    for t in i:
        print(t)


i = int(input("enter your first number: "))
while (i<=300):
    print(i)
    i += 1            #wile loop ka method

i = int(input("enter your first number: "))
while (i>0):
    print(i)  #minus one esach variable
    i -= 1


for i in range(16):
    print("5 X", i+1 ,"=" , 5 * (i +1))
    if (i==9):
      break


for i in range(16):
    if(i>=12):
        print("Hello World")
        continue
print("5 X", i+1 ,"=" , 5 * (i +1))