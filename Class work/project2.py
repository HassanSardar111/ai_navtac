age = int(input("Enter your age"))
height = int(input("Enter your height"))
edu = int(input("Enter your education"))
if (age >= 18 or edu >= 12 and height >= 5):
    print("Congralutions! you have passed")
else:
    print("You have failed")