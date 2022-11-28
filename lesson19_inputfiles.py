inputfiles="txt/rockyou.txt"
outputfile="txt/mypassword.txt"
password_for_look="vasya"
myfile=open(inputfiles,mode='r',encoding='latin_1')
myfile1=open(outputfile,mode='a',encoding='latin_1')
#print (myfile.read())
for num,line in enumerate(myfile,1):
    if password_for_look in line:
        print ("Number line "+str(num)+" "+line.strip())
        myfile1.write("Found password :"+line)
myfile.close()
myfile1.close()


