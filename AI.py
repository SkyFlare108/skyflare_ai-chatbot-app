import os
from pathlib import Path

current_directory = os.path.dirname(os.path.abspath(__file__))

print("\n*Welcome to SkyFlare ChatApp*\n")
user = input("Account Username: ")

file_name = "{}.txt".format(user)
file_path = os.path.join(current_directory, file_name)

if os.path.exists(file_path):
    with open(file_name, "a") as file:
        print("Account Exists")
        first_line = next(open("{}.txt".format(user)))
        passWord = input("Account Password: ")
        
        # while passWord != first_line:
        #     passWord = input("Try Again: ")

        print(">>>Welcome to your Data<<<")
else:
    with open(file_path, "w") as file:
        print("Account Doesn't exist\nCreating...")
        passWord = input("Create account Password: ")
        file.write("{}\n".format(passWord))

