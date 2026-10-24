#Number Analyzer

x = int(input("Enter a number: "))

#Odd or Even
if x % 2 == 0:
    print(f"The number {x} is even!")
else:
    print(f"The number {x} is odd!")

#Positive, Negative or Zero
if x > 0:
    print(f"The number {x} is positive!")
elif x < 0:
    print(f"The number {x} is negative!")
else:
    print(f"The number {x} is zero!")

#Divisible by 3
if x % 3 == 0:
    print(f"The number {x} is divisible by 3!")
else:
    print(f"The number {x} is not divisible by 3!")

#Divisible by 5
if x % 5 == 0:
    print(f"The number {x} is divisible by 5!")
else:
    print(f"The number {x} is not divisible by 5!")

#Perfect Square
if x >= 0:
    root = x ** 0.5
    if int(root) ** 2 == x:
        print(f"The number {x} is a perfect square!")
    else:
        print(f"The number {x} is not a perfect square!")
else:
    print(f"The number {x} is negative and its roots are complex/imaginary!")