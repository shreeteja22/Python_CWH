#set is a collection of well defined objects

set = {2,"teja",True,24,394,3,2}
print(set)
#set ka order kaise bhi aata hai no order
# set it cant be changed 
#agar empty set banana hai toh set() likte for eg
harry = set()
print(type(harry))


#methods to manipulate
set1= {1,2,4,6,8}
set2 = [3,4,5,6,7,9]
print(set1.union(set2))
print(set1.update(set2)) #isme set 2 mai jo numbers hai woh jaake set 1 mai fix hote
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
