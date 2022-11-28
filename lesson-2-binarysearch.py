def sbin (mylist,num,start,stop):
    if start>stop:
        return False
    else:
        mid = (start+stop)//2
        if num == mylist[mid]:
            return mid
        elif num < mylist[mid]:
            stop=mid-1
            return sbin (mylist,num,start,stop)
        else:
            start=mid+1
            return sbin(mylist, num, start, stop)

mylist = [10,12,13,15,20,24,27,33,42,51,57,68,70,77,79,81]
num=20
x= sbin(mylist,num,0,len(mylist))
if x==False:
    print("Item not find")
else:
    print ("Item",num,"index massiv=",x)


