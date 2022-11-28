enemy = {
    'loc_x' : 10,
    'loc y' : 85,
    'color' : 'green',
    'health': 100,
    'name'  : 'mudillo'
}
print(enemy)
print("x="+str(enemy['loc_x'])+" y=" + str(enemy['loc y']) + "name=" + enemy['name'])
enemy['Rank']='Admiral'
print (enemy)
del enemy['Rank']
print(enemy)