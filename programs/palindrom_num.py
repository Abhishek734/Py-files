# palindrom_num.py
# reverse of a number.py
num =  int(input("Enter the number : "))
o_num = num
rev = 0
while(num > 0):
    rem = num%10
    rev = rev * 10 + rem
    num = num//10
print("Reversed Number : ",rev)
if int(rev) == int(o_num):
    print("the number is palindrom as : {} == {}".format(rev, o_num))
else:
    print(" the number is not palingdrom as: {} != {}".format(rev, o_num))
