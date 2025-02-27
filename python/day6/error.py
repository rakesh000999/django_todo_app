

# isvalid = False

# while (isvalid == False):
#     integer = input("Enter a valid number: ")
#     try:
#         integer_2 = int(integer)
#     except ValueError    
        
        
        
list = [1,2,3,4,5]
    
try:       
    print(list[5])   
except IndexError as e:
    print("Index error")    