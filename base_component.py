import tabulate

# Create an empty list to store user information
user_info = []

# Define a function to display the user information in a table


def display_user_info(info):
    # Create a table to display user information with headers
    headers = ["Name", "Shape", "Units", "Area"]
    table = []
    for entry in info:
        table.append([entry["name"], entry["shape"], entry["units"], entry["area"]])
    print("\nUser Information:")
    print(tabulate.tabulate(table, headers=headers, tablefmt="fancy_grid"))

# Define a function to get a "yes" or "no" response from the user


def yes_no(question):

  
    while True:
        # Get user input and convert to lowercase for case-insensitivity
        reply = input(question).strip().lower()
        if reply.startswith('y'):
            return True
        elif reply.startswith('n'):
            return False
        else:
            print("Please enter 'yes' or 'no'.")

# Define a function to get a user's name


def get_name():
    while True:
        print("")
        # Prompt the user to enter their name
        name = input("Enter your name : ")
        # Check for invalid name inputs
        if any(char.isdigit() for char in name):
            print("Invalid input. Name cannot contain numbers.")
        elif name.strip() == "":
            print("Invalid input. Name cannot be blank.")
        else:
            return name

# Define a function that calculates the area with user-defined units


def calculate_area(shape, units, name):
    if shape.startswith('tri'):
        print("\n")
        print("The formula for Area of a triangle is A = 1/2 × base × height")
        print("\n")
        # Get user input for base and height with validation
        base = max_min_input(f"Enter the base length in {units} : ", 0.01, 100)  
        height = max_min_input(f"Enter the height in {units} : ", 0.01, 100)
        area = 0.5 * base * height
        print("\n*************************************************")
        print(f"The area of the {shape} is: {area} {units}^2") 
        print("*************************************************\n")
        # Store user information in a dictionary and append it to the list
        user_info.append({"name": name, "shape": shape, "units": units, "area": f"{area} {units}^2"})
        
    # ... (similar comments for other shapes)

    else:
        print("I apologize, but the Area/Perimeter tool only knows 5 shapes right now.")

# Define a function to get a valid numeric input within a specified range


def max_min_input(prompt, min_value, max_value):
    while True:
        try:
            # Get user input and validate it as a numeric value within the specified range
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Define the main function to become a base component in the base component 


def main():
    # Ask if the user has used the Area/Perimeter tool before
    show_instructions = yes_no("Have you used the Area/Perimeter tool before? : ")

    if not show_instructions:
        print("**************************")
        print("        INSTRUCTIONS      ")
        print("**************************")
        print("")
        print("1. Enter your name.")
        print("2. Choose a shape to calculate: triangle, square, rectangle, circle, or parallelogram.")
        print("3. Enter the required measurements for the selected shape.")
        print("4. Your calculations will be displayed in a table when you finish.")
        print("")  
        print("--------------------------")
        print('PS. If you decide that you are finished with all your calculations, type in the code "xxx" to exit the program.')
        print("--------------------------")
        print("")
        print("**************************")

    while True:
        user_name = get_name()  # Ask for the user's name
        print(f"\nHello {user_name}!\n")

        while True:
            reply = input("What shape would you like to calculate? ('xxx' to exit): ").strip().lower()

            if reply == 'xxx':
                print("Exiting the program.")
                display_user_info(user_info)  # Display user information in a table
                return  # Exit the program

            shape_mapping = {
                'tri': 'triangle',
                'squ': 'square',
                'rec': 'rectangle',
                'cir': 'circle',
                'par': 'parallelogram'
            }

            shape = shape_mapping.get(reply, reply)

            if shape in ['triangle', 'square', 'rectangle', 'circle', 'parallelogram']:
                while True:
                    units = input("Enter the units you'd like to use: ").strip()
                    if not any(char.isdigit() for char in units) and units != "":
                        break
                    else:
                        print("Invalid input. Units cannot be empty or contain numbers.")

                calculate_area(shape, units, user_name)
                
                # Ask if the user wants to use the Area/Perimeter tool again
                repeat = yes_no("Would you like to use the Area/Perimeter tool again? : ")
                print("")
                if not repeat:
                    print("Exiting the program.")
                    display_user_info(user_info)  # Display user information in a table
                    return  # Exit the program
            else:
                print("Invalid input. Please enter a shape that the Area/Perimeter tool knows.")

# Call the main function to run the program
main()
