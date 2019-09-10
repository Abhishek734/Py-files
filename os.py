import os

# print(dir(os))
print(os.getcwd()) # current dir
os.chdir('C:/Users/Acer/Desktop/') # change dir
print(os.getcwd())
print(os.listdir()) # return list of dir

# os.mkdir("NST-2/sub-Dir-2") # making new dir
os.makedirs("NST-2/sub-Dir-2") # making new dir
