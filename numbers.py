while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a valid number.")

print(f"You entered: {x}")