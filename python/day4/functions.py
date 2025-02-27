def add():
    print(1+2)
    
add()    

def sum(num1, num2):
    print(num1, num2)
    sum = num1 + num2
    print(sum)
    
sum(num2=3 , num1=2)  

# DRY
def take_input():
    return int(input("Enter a number:"))

# a = take_input()  
# b = take_input()  

# print(a+b)


def calculate():
    sum = a + b
    difference = a + b
    product = a + b
    return sum, difference, product
a = take_input()
b = take_input()

sum, difference, product = calculate()
print("Sum", sum)