from pathlib import Path

print("Welcome to SkyFlare Bot. This test project will attempt to answer your questions and store answers specific to your conditions.");
name = input("What is your name");

file_name = Path("/Users/skyflare108/Desktop/AI Proj/{name}.txt");

if file_name.is_file():
    print("We were able to access your file");
else:
    print("We were not able to access your file");
    # file = open("{name}.txt", "a")
    # file.write("Now the file has more content!")
    # file.close()

# f = open("{name}.txt", "r")
# print(f.read())

