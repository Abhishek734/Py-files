nums = [1,2,3,4,5,6,7,8,9,10]

## option 1

# my_list = []
# for n in nums:
#     my_list.append(n)

# print(my_list)
# list comprehension

# my_list = [n for n in nums]
# print(my_list)

# my_squares = [n*n for n in nums]
# print(my_squares)

# #map and lambda(func)
# my_list = map(lambda n: n*n, nums)
# print(list(my_list))

# i want 'n' for earch 'n' in nums if 'n' is even

# my_list = [n for n in nums if n%2==0]
# print(my_list)

# filters and lambda
# my_list = filter(lambda n:n%2==0, nums)
# print(list(my_list))

## i want a (letter,num) pair for each letter in 'abcd' and each number in '0123'

# my_list=[]
# for letter in 'abcd':
    # for nums in range(4):
        # my_list.append((letter,nums))
# print(my_list)

my_list = [(letter,nums) for letter in 'abcd' for nums in range(4)]

print(my_list)
