# reverse of a number.py
num =  int(input("Enter the number : "))

# for i in range(len(str(num))):
    # print(num%10(len(str(num))))
rev = 0
while(num > 0):
    rem = num%10
    rev = rev * 10 + rem
    # num = num - rev
    num = num//10
print("Reversed Number : ",rev)
