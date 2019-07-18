# print("hello world")


# Program make a simple calculator that can add, subtract, multiply and divide using functions
# number_1 = input("Enter your first number")
# number_2 = input("Enter your second number")


# #Addition operator
# number_1 = int(input("enter your first number"))
# number_2 = int(input("enter your second number"))
# print(number_1 + number_2)


# #subtraction operator
# number_1 = int(input("enter your first number"))
# number_2 = int(input("enter your second number"))
# print(number_1 - number_2)

# #multiplication operator
# number_1 = int(input("enter your first number"))
# number_2 = int(input("enter your second number"))
# print(number_1 * number_2)

# #division operator
# number_1 = int(input("enter your first number"))
# number_2 = int(input("enter your second number"))
# print(number_1 / number_2)



# Part 2: Making the Calculator more User-friendly

print("***Welcome to Our Calculator***")


number_1 = int(input("enter your first number"))
number_2 = int(input("enter your second number"))

def add(number_1, number_2):
    operation = number_1+number_2
    return operation
print("The sum of your two numbers is", end= " ") 
print(add(number_1,number_2))

   
def subtract(number_1, number_2):
    operation = number_1-number_2
    return operation
print("The difference of your two numbers is", end= " ") 
print(subtract(number_1,number_2))
    
def multiply(number_1, number_2):
    operation = number_1*number_2
    return operation
print("The product of your two numbers is", end= " ") 
print(multiply(number_1,number_2)) 

def divide(number_1, number_2):
    operation = number_1/number_2
    return operation
print("The quotient of your two numbers is", end= " ") 
print(divide(number_1,number_2))






















