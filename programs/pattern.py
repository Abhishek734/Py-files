# pattern.py
num = 6

for row in range(0,num):
    for column in range(0, num):
        if column != num/2:
            print("*", end = " ")
        else:
            print(" ")
    print()
