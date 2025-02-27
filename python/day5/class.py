# class Student:
#     age = 18 #static variable...
    
#     def __init__(self, name, level, address): #constructor
#         print("Constructor called")
#         self.student_name = name
#         self.student_level = level
#         self.student_address = address
    
#     def displayStudentName(self):
#         print(self.student_name)
        
#     def displayStudentAddress(self):
#         print(self.student_address)
               
    
#     def add(self):
#         print("sum of 1 and 2 is ", 1+2)
        
# first_student = Student("rakesh", "9", "KTM")    #instance
# second_student = Student("Priya", "9", "KTM")    #instance
# print(first_student.age)
# print(first_student.student_name)

# print()

# # Student.add()
# first_student.add()


class Student:
    school_name = "TechnoSchool"
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
        # instance method
    def displayStudentDetail(self):
        print(self.id)
        print(self.name)
        pass    
    
    
student_one = Student(100, "radha")
student_one.displayStudentDetail()



class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def displayAnimalName(self):
        print(self.name)
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)    