print("Type conversion")

a = 10
b = 4.67
print(a+b)          #10.0+4.67
print(type(a))
print(type(b))

print("-------------------------------------------------------")

print("Type Casting")

c = int("50")
d = 20
print(type(c))
print(c+d)  


""" the type conversion is done automatically but the type casting is done
    manually by the programmer . 1st int is converted into float
    and in the 2nd we give some instruction  variable = type(value)
      """

# input in python
print("Input in Python")
name = input("Enter your name : ")
age = input("Enter your age : ")

print("Welcome" , name)
print("Age : ", age)

print(type(age))

val = int(input("Enter the value : "))
print(val)
print(type(val))
