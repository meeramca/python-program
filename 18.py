#Find gcd of 2 numbers.
def gcd( num1,num2):
    if num1 == 0 :
         return num2
    elif num2 == 0:
         return num1
    else:
         return gcd(num2,num1%num2)
num1= int(input("first number : "))
num2= int(input("first number : "))
print("gcd of {} and {} is {}".format(num1,num2,gcd(num1,num2)))
