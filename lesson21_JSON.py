import json
filename="txt/user_settings.txt"
myfile=open(filename,mode='w',encoding='latin')
player1={
    'PlayerName':"Donald Tramp",
    'Score': 245,
    'awards': ["AR","NW","COL"]
}
player2={
    'PlayerName':"Hilary Clinton",
    'Score': 246,
    'awards': ["WGT","TX","MIS"]
}
#-------- File JSON
myplayers=[]
myplayers.append(player1)
myplayers.append(player2)

json.dump(myplayers,myfile)
myfile.close()

#load file JSON
myfile=open(filename,mode='r',encoding='latin')
json_data=json.load(myfile)
for userdata in json_data:
    print("Username is : " +userdata['PlayerName'])
    for ind in range(0,len(userdata['awards'])):
         print("Award :"+userdata['awards'][ind])
    print("___________________\n\n")
myfile.close()