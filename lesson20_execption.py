import sys
filename="txt/name.txt"
try:
    myfile=open(filename,mode='r',encoding='latin_1')
except Exception:
    print("inside try open")
    print("Error found")
 #   sys.exit()
else:
    print("INside else")
    print(myfile.read())
finally:
    print ("Inside  FINALLY")

print("===========================")
