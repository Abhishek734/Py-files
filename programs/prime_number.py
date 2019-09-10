# upper = 50
# lower = 100

# for num in range(upper,lower+1):
#     if num > 1:
#         for n in range(2,num):
#             if num % n == 0:
#                 break
#         else:
#             print(num)


# primelist = lambda n : [x for x in range(2, n) if not 0 in map(lambda z : x % z, range(2,x))]

# print(", ".join(map(str, primelist(100))))
# print(type(primelist))
# tt = primelist(100)
# print(tt)

# primelist = lambda n : [x for x in range(50,101) if not 0 in map(lambda t: x%t, range(50,101))]
# print(",".join(map(str, primelist(22))))

print([num for num in range(50,101) if 0 not in [num%cc for cc in range(2,num)]])
