age = int(input("Enter your age: "))

is_adult = age >= 18

print("Is adult:", is_adult)

if is_adult:
    print("Adult ticket price: KSh 500")
else:
    print("Child ticket price: KSh 250")