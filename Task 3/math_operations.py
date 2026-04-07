import math

def calculate_square_root(num):
    try:
        result = math.sqrt(num)
        print("Square Root:", result)
    except ValueError:
        print("Error: Cannot calculate square root of negative number")

def divide_numbers(a, b):
    try:
        result = a / b
        print("Division Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")