d1 = {}
n = int(input("size of dictionary"))
print("Enter data :")
for i in range(0,n):
    key = input("key : ")
    value = input("value : ")
    d1.update({key : value})

d2 = {}
n2 = int(input("size of dictionary"))
print("Enter data :")
for i in range(0,n2):
    key = input("key : ")
    value = input("value : ")
    d2.update({key : value})

print("dictionary1 is ",d1)
print("dictionary2 is ",d2)
d1.update(d2)
print("dictionary after merging ", d1)
