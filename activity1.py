#1
num1=int(input("Enter the first number")) 
num2=int(input("Enter the second number")) 
sum =num1+num2
print("The sum of two numbers is", sum) 
product=num1*num2
print("The product of two numbers is",product)

#2
num=int(input("Enter the  number")) 

square =num*num
print("The square of the number is", square) 
cube=num*num*num
print("The cube of num is", cube)
#3
num=int(input("Enter the  number")) 
if num>0:
    
    print("the number is positive ") 
elif num<0:
    print(" The number is negative ") 
else:
    print("The number is zero")
#4
num=int(input("Enter the  number")) 
if num%2==0:
    print("the number is even ")  
else:
    print(" The number is odd")
#5
    base=int(input("Enter the base")) 
height=int(input("Enter the height")) 
area =1/2*(base*height)
print("The area of the triangle is", area)
#6
name=input("Enter the name") 
age=int(input("Enter the age")) 
city=string(input("Enter the city")) 
print("\nThe name of the person is", name) 
print("\nThe age of the person is", age)
print("\nThe city where the person lives is", city)
