import os

# print(dir(os)) # dir assorciated with "os"
# print(os.getcwd()) # current dir
# os.chdir('C:/Users/Acer/Desktop/') # change dir
# print(os.getcwd())
print(os.listdir()) # return list of dir

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
# print(os.getcwd())
# for dirpath, dirnames, filenames in os.walk('C:/Users/Acer/Desktop/'):                # os.walk(path) //usefull
#     print("Current path: ", dirpath)
#     print("Directories: ", dirnames)
#     print("Files: ", filenames)

# print(os.environ.get("PUBLIC"))
# file_path = os.path.join(os.environ.get("PUBLIC"), 'test.txt') # os.path.join
# print(file_path)

# with open(file_pathm,"w") as f:
#     f.write()

# print(os.path.split("/tmp/test.txt")) # os.path.split
# print(os.path.exists("/tmp/test.")) # os.path.exists #os.path.isdir #os.path.isfile

# print(os.path.splitext("/tmp/test.txt")) # returns ('/tmp/test', '.txt')
# print(dir(os.path)) # read all the dirs in os.path
