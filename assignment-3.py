# Task-1
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

number = int(input("Enter the number: "))
print("The factorial of", number, "is:", factorial(number))



# task-2
import math
num = float(input("Enter a number: "))
sqrt_val = math.sqrt(num)
log_val = math.log(num)
sin_val = math.sin(num)
print("Square root of", num, "is:", sqrt_val)
print("Natural log of", num, "is:", log_val)
print("Sine of", num, "is:", sin_val)
