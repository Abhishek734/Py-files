# vowels in string.py
strr = input("Enter the string : ")
li = []
vowels = ['a','e','i','o','u','A','E','I','O','U']
count = 0
for s in strr:
    if s in vowels:
        count += 1
        print("Vowel Encountered : ",s)
        li.append(s)
print("{} volumns are present here".format(count))
print("And they are : ",li)
