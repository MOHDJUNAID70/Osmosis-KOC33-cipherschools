#                                                Scientific Calculator
import math
print("\nWELCOME :)\n")
print("Type 'a' for addition")
print("Type 's' for subtraction")
print("Type 'm' for multiply")
print("Type 'd' for divide")
print("Type 'mod' for remainder")
print("Type 'sq' for Square Root")
print("Type 'exp' for Exponent(Power(a,b))")
print("Type 'sin' for Sine Function")
print("Type 'cos' for Cosine Function")
print("Type 'tan' for Tangent Function")
print("Type 'rad' to Change from Radian to Degree")
print("Type 'deg' to Change from Degree to Radian")
print("Type 'exit' to take Exit From Program")

while True:

    choice = str(input("\nYour Choice: "))
    if choice=='a':
        n=int(input("How many Numbers you want to add: "))
        s=0
        for i in range(1,n+1):
            add=float(input("Number: "))
            s+=add
        print("Sum is: ",s)
    elif choice=='s':
        num1= float(input("Num1: "))
        num2= float(input("Num2: "))
        print("Subtraction of Entered Number is: ",num1-num2)
    elif choice=='m':
        m=int(input("How many Numbers You Want to Multiply: "))
        s=1
        for i in range(1,m+1):
            mul=float(input("Number: "))
            s*=mul
        print("Multiplication of Entered Number is: ",s)
    elif choice=='d':
        numerator=float(input("Numerator: "))
        denominator=float(input("Denominator: "))
        print("Divison of Entered Number is: ",numerator/denominator)
    elif choice=='mod':
        numerator=float(input("Enter Numerator : "))
        denominator=float(input("Enter Denominator : "))
        print("Remainder is: ",numerator%denominator)
    elif choice=='sq':
        num=float(input("Enter Number of which you want to find Square Root: "))
        print("Square root is: ",math.sqrt(num))
    elif choice=='exp':
        num1=float(input("Exponent: "))
        num2=float(input("Power: "))
        print("Result: ", num1**num2)
    elif choice=='sin':
        val=float(input("Value(Sin_): "))
        print("Result ", math.sin(val))
    elif choice=='cos':
        val=float(input("Value(Cos_): "))
        print("Result ", math.cos(val))
    elif choice=='tan':
        val=float(input("Value(Tan_): "))
        print("Result ", math.tan(val))
    elif choice=='rad':
        val=float(input("Radian: "))
        print("Degree", math.degrees(val))
    elif choice=='deg':
        val=float(input("Degree: "))
        print("Radian", math.radians(val))
    elif choice=='exit':
        break
    else:
        print("\nInvalid Input!")
print("\nThank You :)")