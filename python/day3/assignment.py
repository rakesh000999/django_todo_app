# list = range(1,100)

# function to calculate even numbers:
# def even_number(list):
#     numbers = []
#     for i in list:
#         if i % 2 == 0:
#             numbers.append(i)
#     return ' '.join(map(str, numbers))

# even = even_number(list)
# print(even)

# 1. Write a program that takes a list of numbers and prints "Odd" if the number is odd and "Even" if the number is even.
# for i in list:
#     if i % 2 == 0:
#         print(i , "Even")
#     else:
#         print(i , "Odd")    


# 2. Write a program that takes a list of numbers and finds the sum of all even numbers in the list.
# def sum_of_even_numbers(list):
#     sum = 0
    
#     for i in list:
#         if i % 2 == 0:
#             sum += i
#     return sum        
        
# total_sum = sum_of_even_numbers(list)        
# print(f"The sum of even numbers:{total_sum}")        

# 3. Write a program that takes a list of numbers and counts how many numbers are greater than 50.
# def greaterThan(list):
#     count = 0
#     for i in list:
#         if i > 50:
#             count+=1
#     return count    
        
# print(f"There are {greaterThan(list)} numbers greater 50")            

# 4. Write a program that takes a list of numbers and prints the prime numbers from the list.
# list = range(1,100)
# count = 0
# for i in list:
#     for j in range(1,i+1):
#         if i % j == 0:
#             count+=1
#     if count == 2:
#         print(i)   
        
        
   # numbers = [2, 13, 17, 19, 22, 33]
# new_list = []

list = list(range(5,20))
prime=[]
for each in list:
    
    if each < 2:
        continue
    else:
        count = 0
        for i in range(2,each):
            if each % i == 0:
                count += 1
                break
        if(count==0):
            prime.append(each)
            print(each)
print(prime)     
        
        
             
# 5. Write a program that takes a list of numbers and finds and prints the largest number in the list.
# 6. Write a program that takes a list of numbers and filters out and prints only the positive numbers in the list.
# 7. Write a program that takes a list of numbers and prints the list in reverse order.
# 8. Write a program that takes a list of numbers and prints the numbers that are divisible by 3.
# 9. Write a program that takes a list of numbers and prints True if all numbers are positive, otherwise False.
# 10. Write a program that takes a list of numbers and a target number as input and counts how many times the target number appears in the list.

# assume list = list(range(1,100))