import shutil
import os
# try:
#  with open("test.txt") as file:
#     print(file.read())
# except FileNotFoundError:
#   print("This file doesn't exist!")

# #use "w" to write and "a" to append
# with open("test1.txt", "w") as file:
#     file.write("what?")

#shutil.copyfile("test.txt", "test1.txt")

# source = "test.txt"
# destination = "C:\\Users\\noora\\Desktop\\test.txt"

# try:
#     if os.path.exists(destination):
#         print("There is already a file there!")
#     else:
#         os.replace(source, destination)
#         print(f"{source} was moved!")
# except FileNotFoundError:
#     print(f"{source} was not found :(")

path = "empty_folder"

try:
    os.remove(path)
    print(f"{path} was successfully removed")
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("access denied")

