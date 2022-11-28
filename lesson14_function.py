
def privetstvie(name):
    """"privet"""
    print("Privetsvie\nHeloo " + name)

def aaa():
    print("AAAA")

def summa(x,b):
    return x+b
def factorial(x):
    if x==1: return 1
    else:
        return x*factorial(x-1)

#=======================
print("----------------------")
privetstvie("Serhii")
privetstvie("")
aaa()
print(summa(5,10))
print(summa("5","10"))
print(factorial(5))