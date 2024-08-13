a = (int(input("ENTER YOUR NUMBER BETWEEN 2 AND 6 : ")))
if (a>2 or a<6):
    raise ValueError("NUMBER SHOULD BE BETWEEN 2 AND 6")
#Raise keyword is use to rqaise custom error in the program to stop immediately