enemy = {
    'loc_x' : 10,
    'loc y' : 85,
    'color' : 'green',
    'health': 100,
    'name'  : 'mudillo',
    'awards': ['za otvagu','za otv']
}
all_enemey=[]


for x in range (0,10):
    all_enemey.append(enemy.copy())
for x in all_enemey:
    print(x)
print("--------------------------------------------")

all_enemey[5]['health']=30

for x in all_enemey:
    print(x)

x=10
x-=25
print (x)
