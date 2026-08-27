from utils import square, is_even, celsius_to_fahrenheit, greet


name = input("Enter your name: ")
number = float(input("Enter a number: "))

print(greet(name))
print("Square:", square(number))

if is_even(number):
    print("Even")
else:
    print("Odd")

print("Fahrenheit:", celsius_to_fahrenheit(number))