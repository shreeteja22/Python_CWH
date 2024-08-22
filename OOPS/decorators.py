
def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using the function")
    return mfx
    
@greet
def hello():
    print("hello world")
hello()