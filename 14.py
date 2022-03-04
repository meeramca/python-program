l1 = []
l2 = []
n1 = int(input("size of color list1"))
n2 = int(input("size of color list2"))
print("enter colors for colorlist1")
for i in range(0,n1):
   a = input()
   l1.append(a)
print("enter colors for colorlist2")
for i in range(0, n2):
   b = input()
   l2.append(b)
print("all colors from color-list1 not contained in color-list2")
for x in l1:
   if (x in l1) and (x not in l2):
       print(x)
