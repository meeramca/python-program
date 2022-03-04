#LENGTH OF THE LONGEST WORD
words = []
number = int(input("number of words: "))
for i in range(0,number):
    word=input("enter a word")
    words.append(word)
temp = words[0]
length = len(words[0])
for i in words:
    if len(i) > length :
       temp = i
print("length of the longest word {} is {}".format(temp,len(temp)))
