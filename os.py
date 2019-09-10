import os

# print(dir(os))
print(os.getcwd()) # current dir
# os.chdir('C:/Users/Acer/Desktop/') # change dir
# print(os.getcwd())
# print(os.listdir()) # return list of dir

# os.mkdir("NST-2/sub-Dir-2") # making new dir
# os.makedirs("NST-2/sub-Dir-2") # making new dir //prefered

# os.rmdir("NST-2/sub-Dir-2") # delete dirs // prefered
# os.removedirs("NST-2/sub-Dir-2") # delete dirs

# print(os.listdir())

# os.rename("BasicResume.pdf","Basic_resume.pdf")

# print(os.stat("Basic_resume.pdf").st_size)
# print(os.stat("Basic_resume.pdf").st_mtime)

# from datetime import datetime
# print(datetime.fromtimestamp(os.stat("Basic_resume.pdf").st_mtime))


# print(os.listdir())
os.chdir('C:/Users/Acer/Desktop/') # change dir
print(os.getcwd())
os.walk()
