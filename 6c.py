list1 = []
list2 = []
count=0
size1 = int(input("Enter size of list 1 :"))
size2 = int(input("Enter size of list 2 :"))
print("Numbers of list 1 : ")
for i in range(0,size1):
    n1 = int(input())
    list1.append(n1)

print("Numbers of list 2: ")
for j in range(0, size2):
    n2 = int(input())
    list2.append(n2)

print("Common elements are: ")
for i in list1:
    if (i in list1) and (i in list2) :
        count += 1

if count == 0:
    print("No common elements")
else:
     print("Common elements are ",set(list1) & set(list2))
