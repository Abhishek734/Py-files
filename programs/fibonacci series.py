n = int(input(the number: ))

def fibb(n):
    lis = [0,1]
    for i in range(2,n):
        temp = lis[i-2]+lis[i-1]
        lis.append(temp)
    return lis[0:n]
fibb(n)


