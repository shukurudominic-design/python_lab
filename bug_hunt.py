# BUG: The welcome message was missing the closing quotation mark, so I added it.
print("Welcome to the Bug Hunt!")

name = input("What is your name? ")

# BUG: The name variable was misspelled and was inside a string, so I changed it to use the name variable.
print("Nice to meet you,", name)

# BUG: The age from input was a string, so I converted it to an integer before adding 1.
age = int(input("How old are you? "))

print("Next year you will be " + str(age + 1))