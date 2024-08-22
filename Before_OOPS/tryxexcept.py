num = input("enter your mutiplication number : ")
print(f"Multiplication of table {num} is: ")
try:
  for i in range(1,11):
    print(f"{int(num)} X {i} = {int(num)*i}")
except :
    print("invalid input")

print("Thank You run again to multiply your number")
print("end of the code")