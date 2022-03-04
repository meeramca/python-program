# From a list of integers, create a list removing even numbers
integers=[]
size=int(input("size of list :"))
print("enter intiger:" )
for i in range(0,size):
    integer= int(input())
    integers.append(integer)
for i in integers:
    if i%2 == 0 :
        integers.remove(i)
print(integers)
