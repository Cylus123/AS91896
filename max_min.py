while True:
    try:
        user_input = float(input("Please enter a number : "))
        if 0 < user_input <= 100:
            break
        else:
            print("Please enter a number between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number between 0 and 100.")

print("You entered:", user_input)
