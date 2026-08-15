print("Calculator Program")
print("Enter any operator + - * % /")
user_operator=input("Enter any operator from above for calculation : ")
num1=int(input("Enter 1st number for calculation : "))
num2=int(input("Enter 2nd number for calculation : "))

if(user_operator=='+'):
    print(f"Addition of {num1} and {num2} is {num1+num2}")
elif(user_operator=='-'):
    print(f"Subtraction of {num1} and {num2} is {num1-num2}")
elif(user_operator=='*'):
    print(f"Multiplication of {num1} and {num2} is {num1*num2}")
elif(user_operator=='/'):
    if(num2==0):
        print("Division by zero Error")
    else:
        print(f"Division of {num1} and {num2} is {num1/num2}")
elif(user_operator=='%'):
    if(num2==0):
            print("Division by zero Error")
    else:
        print(f"Modulo Division of {num1} and {num2} is {num1%num2}")
else:
    print("Invalid choice")