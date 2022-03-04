import operator
d1 = {}
n = int(input("Size of dictionary"))
print("Enter data :")
for i in range(0,n,1):
   key = input("Key : ")
   value = input("Value : ")
   d1.update({key : value})
print("Dictionary is ",d1)
asc = sorted(d1.items(),key=operator.itemgetter(1))
dsc = sorted(d1.items(),key=operator.itemgetter(1),reverse=True)
print("Ascending",asc)
print("Descending",dsc)
