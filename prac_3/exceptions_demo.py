"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the numerator and denominator are invalid numbers
2. When will a ZeroDivisionError occur?
Divide by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Use except function
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")