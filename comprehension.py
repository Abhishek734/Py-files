nums = [1,2,3,4,5,6,7,8,9,10]

## list comprehensions

# my_list = []
# for n in nums:
#     my_list.append(n)

# print(my_list)

# my_list = [n for n in nums]
# print(my_list)

## ex-2

# my_squares = [n*n for n in nums]
# print(my_squares)

## map and lambda(func)

# my_list = map(lambda n: n*n, nums)
# print(list(my_list))

## i want 'n' for earch 'n' in nums if 'n' is even

# my_list = [n for n in nums if n%2==0]
# print(my_list)

## filters and lambda
# my_list = filter(lambda n:n%2==0, nums)
# print(list(my_list))

## i want a (letter,num) pair for each letter in 'abcd' and each number in '0123'

# my_list=[]
# for letter in 'abcd':
    # for nums in range(4):
        # my_list.append((letter,nums))
# print(my_list)

# my_list = [(letter,nums) for letter in 'abcd' for nums in range(4)] # nested for loop
# print(my_list)


## Dictionary Comprehension

## zip func
names = ['a','b','c']
nums = ['1','2','3']

# print(list(zip(names,nums)))

# i want a dict{'name':'nums'} for each name, hero in zip(names, heros)

# my_dict = {}
# for name,nums in zip(names, nums):
#     my_dict[name] = nums
# print(my_dict)

# my_dicts = {name : nums for name, nums in zip(names, nums)}
# print(my_dicts)

## if name not equal to c

# my_dicts = {name : nums for name, nums in zip(names, nums) if name != 'c'}
# print(my_dicts)

## set comprehension (list with unique values)

nums = [1,2,2,2,3,3,4,4,1,1,5,6,5,6,7,7,7,8,9,9,9,9]

# my_set = set()
# for n in nums:
    # my_set.add(n)
# print(my_set)

# my_set = {n for n in nums} # use dictionary for sets without colon (:)
# print(my_set)

## generator expression
nums = [1,2,3,4,5,6,7,8,9,10]
# def gen_func(nums):
#     for n in nums:
#         yield(n*n)
# for i in my_gen:            # my_gen = gen_func(nums) # print(list(my_gen))
#     print(i)

my_gen = (n*n for n in nums)        # use () for generators
print(type(my_gen))

for i in my_gen:
    print(i)

