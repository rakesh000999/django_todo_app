student = {
    "name" : "Rakesh Joshi",
    "address" : "KTM",
    0: "this is zero"
}

# print(student["name"])

# print(student[0])
# student[0] = "haha zero is changed!"
# print(student[0])

for i in student:
    print(i[0])
    
del student["name"]
print(student[0])    