# bubble sort.py
import time

arr = list(map(int, input("Enter the string: ").split(",")))

# arr = [7,5,6,4,3,1,2,9]
# start = time.time()
for i in range(len(arr)):

    vv = len(arr)-1
    for j in  range(vv):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            vv-1
# end = time.time()
# print("execution_time : ",end-start)
print(arr)
