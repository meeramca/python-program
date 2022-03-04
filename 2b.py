size = int(input("Number of elements "))
list =[]
square=[]
print("Enter {} numbers ".format(size))
for i in range(0,size):
    num = int(input())
    list.append(num)
print("Square of entered numbers are:")
for number in list:
    sq = number ** 2
    square.append(sq)
for i in range(0,size):
    print("Square of {} is {}".format(list[i],square[i]))
