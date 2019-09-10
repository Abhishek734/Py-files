# li = [9,6,7,8,4,5,3,2,1]
# s_li = sorted(li)   # method sorted // returns another sorted list
# print("original list: ",li)
# print("sorted list: ", s_li)

# li.sort()           # funtion sorted //returns none
# print("original list: ",li)

# li = [9,6,7,8,4,5,3,2,1]
# s_li = li.sort()
# print("sorted variable: ", s_li)

# # descending order
# li = [9,6,7,8,4,5,3,2,1]
# s_li = sorted(li, reverse = True)       # prefered
# print("original list: ",li)
# print("sorted list: ", s_li)
# li.sort(reverse=True)                   # only with list
# print("original list: ",li)

# # tuples
# tup = (9,6,7,8,4,5,3,2,1)
# # tup.sort() //error

# s_tup = sorted(tup)
# print("tuple\t",s_tup)

# # Dictionaries
# di = {'n':'wewe','t':"sgfs","r":"dfgbdf","a":"rgfdg"}
# s_di = sorted(di)           # returns only the keys
# print("dict keys\t", s_di)

# conditions

# li = [-6,-4,-3,1,2,3]
# # s_li = sorted(li) # order -,0,+
# # print(s_li)

# s_li = sorted(li, key=abs)
# print(s_li) ## optput was [1, 2, -3, 3, -4, -6]

class Employee():
    def __init__(self, name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},{})'.format(self.name, self.age,self.salary)

e1 = Employee("carl", 37,70000)
e2 = Employee("serah", 29, 8000)
e3 = Employee("john", 43, 90000)

empleyees = [e1,e2,e3]
print(empleyees)
# def e_sort(emp):
    # return emp.salary # emp.name, emp.age

# s_empleyees = sorted(empleyees, key=e_sort, reverse=True)
s_empleyees = sorted(empleyees, key=lambda e:e.name, reverse=True)
print(s_empleyees)

# importing attrgetter
from operator import attrgetter
s_empleyees = sorted(empleyees, key=attrgetter('salary'), reverse=True)
print(s_empleyees)
