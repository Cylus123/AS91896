def yes_no(question):
    while True:
        reply = str(input(question)).lower().strip()
        if reply[0] == 'y':
            print("yes")
        elif reply[0] == 'n':
            print("no")
        else:
            return yes_no("Please enter yes or no input: ")


show_instructions = yes_no("Yes or no ?: ")
