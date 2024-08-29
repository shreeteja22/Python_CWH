class math:
    def __init__(self,num):
        self.num = num
    def addtonum(self,n):
        self.num = self.num + n

    @staticmethod
    def sum(a,b):
        return a+b 
    
a = math(5)
print(a.num)
print(a.sum(945,24))


#self ke bina program mai error aata so to use def function without self try static method