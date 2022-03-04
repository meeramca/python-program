word=input("Enter a word ")
letters=[]
length=len(word)
for i in range(0,length):
    letter=word[i]
    ordinal=ord(letter)
    print("Ordinal value of {} is {}".format(letter,ordinal))
