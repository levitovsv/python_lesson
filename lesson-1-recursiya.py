def privet(x):
    if x==0:
        return
    else:
        print("Hello world")
        privet(x-1)

privet(5)

def sum (x):
    if x==0:
        return 0
    else:
        return x+sum(x-1)

print (sum(5))

def factorial (x):
    if x==0:
        return 1
    else:
        return x * factorial(x-1)

print (factorial(5))

def fibon (x):
    if x==0 or x==1:
        return x
    else:
        return fibon(x-1) + fibon(x-2)

print (fibon(11))


