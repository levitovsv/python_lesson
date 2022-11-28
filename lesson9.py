cars = ['bmw','renault','vw','mersedec','zapor']

for x in cars:
    print('My cars:'+x)

print (cars[1])
for x in range (0,len(cars)):
    print (x)
    print(cars[x])
mylist=list (range(0,10))
print(mylist)
mylist.sort(reverse=True)
print (mylist)
print ('Max number='+ str(max(mylist)))
print ('Min number='+ str(min(mylist)))
print ('Sum number='+ str(sum(mylist)))
print("=========================")
mycars = cars[2:3]
print(mycars)
mycars = cars[:2]
print(mycars)
mycars = cars[:-1]
print(mycars)
