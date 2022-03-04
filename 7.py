# add ing if ing present add ly
string = input("string= ")
print("new string = ")
if len(string)<3:
    print(string+'ing')
elif string[-3:] == 'ing':
         print(string+'ly')
else:
    print(string + 'ing')
