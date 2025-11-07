ops = input("Enter the operation you want to perform (+, -, *, /) = ")
num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))
if ops == "+":
    print("The sum is = ", num1 + num2)     
elif ops == "-":
    print("The difference is = ", num1 - num2)
elif ops == "*":
    print("The product is = ", num1 * num2)
elif ops == "/":
    print("The quotient is = ", num1 / num2)
else :
    print("wrong operator ")
    
        
