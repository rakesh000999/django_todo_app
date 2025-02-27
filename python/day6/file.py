import os

file = open("example.txt", "w")
content = file.read()
print(content)
file.close()

os.remove("example.txt")

print("---------------After Strip--------")

# file = open("example.txt", "r")
# for line in file:
#     print(line.strip())
# file.close()    