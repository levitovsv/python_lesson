
cities = ['New York','Kiev','Donetsk','Dnipro','Volnovakha']
print(cities)
for i in range(0,len(cities)):
    print(cities[i].upper())
cities[2]='Yalta'
print("")
for i in range(0,len(cities)):
    print(cities[i].upper())
cities.append('Deli')
print(cities)
cities.insert(2,'Mariupol')
print (cities)
del cities[2]
print(cities)
del cities[-2]
print(cities)
cities.remove('Kiev')
print(cities)
del_cities=cities.pop(2)
print (cities)
cities.sort()
print (cities)