list1 = []
list2 = []
sum1=0
sum2 = 0
size1 = int(input("Enter size of list 1 :"))
size2 = int(input("Enter size of list 2 :"))
print("Numbers of list 1 : ")
for i in range(0,size1):
    n1 = int(input())
    list1.append(n1)
print("Numbers of list 2 : ")
for j in range(0, size2):
    n2 = int(input())
    list2.append(n2)
for i in list1:
    sum1 += i
for j in list2:
    sum2 += j
print("Sum of list1 = ",sum1)
print("Sum of list2 = ",sum2)
if sum1 == sum2 :
    print("Two lists have same sum ")
else:
    print("Two lists have different sum ")
