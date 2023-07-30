print("Welcome to the calculator!")
choice="yes"
while choice == "yes" :
 a=float(input("Enter the first number:"))
 b=float(input("Enter the second number:"))
 print("Menu\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
 num=int(input("Choose an operation (enter the number):")) 
 if num==1:
     result = a+b
     print("Result:",result)
 elif num ==2:
     result = a-b
     print("Result:",result)
 elif num ==3:
     result = a*b
     print("Result:",result)
 elif num ==4:
     result = a/b
     print("Result:",result)
 else:
     print("Error: No such operation")
 choice = input("Do you want to continue? (yes/no)")
print("Thank you for using the Currency Converter. Goodbye!")
