numlist = []
poslist = []
size =int(input ("Size of the list :"))
print ("Enter numbers")
for i in range(0,size):
    num=int(input())
    numlist.append(num)
print("The positive list ")
for i in range(0,size):
    if numlist[i] >= 0:
        poslist.append(numlist[i])
print(poslist)


