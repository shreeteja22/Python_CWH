#def fac(n):
#     if (n==0 or n==1):
#         return(1)
#     else:
#         return n * fac(n-1)
    
# print(fac(1))
# print(fac(2))
# print(fac(3))
# print(fac(4))
# print(fac(5))
# print(fac(6))
# print(fac(7))
# print(fac(8))
# print(fac(9))
# print(fac(10))




#fibannoci num
def fi(n):
    if(n==0):
        return(0)
    elif(n==1):
        return(1)
    else:
        return fi(n-1) + fi(n-2)

print(fi(1))
print(fi(2))
print(fi(3))
print(fi(4))
print(fi(5))
print(fi(6))
print(fi(7))
print(fi(8))
print(fi(9))
print(fi(10))  