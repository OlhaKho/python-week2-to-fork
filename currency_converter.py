print("Welcome to the Currency Converter!")
choice="yes"
while choice == "yes" :
    print("1. Dollar \n2. Euro\n3. Pound\n4. Yen")
    currency=int(input ("Select initial currency(enter the number):"))
    if currency==1:
        num1=float(input("Enter the amount of money(enter the number):"))
        print("Choose currency for conversion: \n1. Euro \n2. Pound\n3. Yen\n4. Dollar")
        num2=int(input("Choose the currency (enter the number): "))
        if num2==1:
            result1=num1*0.91 
            print("Result:",round(result1, 2),"euros")
        elif num2==2:
            result2=num1*0.78 
            print("Result:",round(result2, 2),"pounds")
        elif num2==3:
            result3=num1*140.79 
            print("Result:",round(result3, 2),"yens")
        else:
            print("Error: No such currency")
    elif currency==2:
        num1=float(input("Enter the amount of money(enter the number):"))
        print("Choose currency for conversion: \n1. Dollar \n2. Pound\n3. Yen")
        num2=int(input("Choose the currency (enter the number):"))
        if num2 ==1:
         result1=num1*1.10 
         print("Result:",round(result1, 2),"dollars")
        elif num2 ==2:
         result2=num1*0.86 
         print("Result:",round(result2, 2),"pounds")
        elif num2 ==3:
         result3=num1*155.27 
         print("Result:",round(result3, 2),"yens")
        else:
         print("Error: No such currency")
    elif currency==3:
        num1=float(input("Enter the amount of money(enter the number):"))
        print("Choose currency for conversion: \n1. Euro \n2. Dollar\n3. Yen")
        num2=int(input("Choose the currency (enter the number):"))
        if num2 ==1:
         result1=num1*1.17 
         print("Result:",round(result1, 2),"euros")
        elif num2 ==2:
         result2=num1*1.29 
         print("Result:",round(result2, 2),"dollars")
        elif num2 ==3:
         result3=num1*181.17 
         print("Result:",round(result3, 2),"yens")
        else:
         print("Error: No such currency")    
    elif currency==4:
        num1=float(input("Enter the amount of money(enter the number):"))
        print("Choose currency for conversion: \n1. Euro \n2. Pound\n3. Dollar")
        num2=int(input("Choose the currency (enter the number):"))
        if num2 ==1:
         result1=num1*0.0064 
         print("Result:",round(result1, 2),"euros")
        elif num2 ==2:
         result2=num1*0.0055 
         print("Result:",round(result2, 2),"pounds")
        elif num2 ==3:
         result3=num1*0.0071 
         print("Result:",round(result3, 2),"dollars")
        else:
         print("Error: No such currency")
    else:
        print("Error: No such initial currency")       
    choice = input("Do you want to continue? (yes/no)")
print("Thank you for using the Currency Converter. Goodbye!")