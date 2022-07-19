def factorial(num1):
    temp = 1
    temp0 = num1
    while num1>0:
        temp = temp*num1
        num1 -= 1
    print(f"Factorial of given number {temp0} is {temp}")

num = int(input("Enter the number: "))
factorial(num)

