#Basic calculator program

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
operator = input("Choose an operator '+' '-' '*' '/': ")

if (operator == '+'):
    print(number1 + number2)
elif(operator == '-'):
    print(number1 - number2)
elif(operator == '*'):
    print(number1 * number2)
else:
    print(number1 / number2)
    
