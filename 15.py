s1 = input("String 1 : ")
s2 = input("String 2 : ")
l1 = len(s1)
l2 = len(s2)
a = s1[0]
b = s2[0]
c = s1[1:l1]
d = s2[1:l2]
newstr = b + c +" "+ a + d
print(newstr)
