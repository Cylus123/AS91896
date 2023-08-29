import tabulate  # Import the tabulate library to create a table

# Create an empty list to store user information
user_info = []

# Define a function to display the user information in a table
def display_user_info(info):
    headers = ["Name", "Shape", "Units", "Area"]
    table = []
    for entry in info:
        table.append([entry["name"], entry["shape"], entry["units"], entry["area"]])
    print("\nUser Information:")
    print(tabulate.tabulate(table, headers=headers, tablefmt="fancy_grid"))

# Define a function to get a "yes" or "no" response from the user
def yes_no(question):
    while True:
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
        name = input("Enter your name: ")
        if any(char.isdigit() for char in name):
            print("Invalid input. Name cannot contain numbers.")
        elif name.strip() == "":
            print("Invalid input. Name cannot be blank.")
        else:
            return name

# Define a function that calculates the area with user-defined units
def calculate_area(shape, units, name):
    if shape.startswith('t'):
        print(f"The formula for Area of a triangle is A = 1/2 × base × height")
        base = max_min_input(f"Enter the base length in {units}: ", 0.01, 100)  # Minimum and maximum values
        height = max_min_input(f"Enter the height in {units}: ", 0.01, 100)  # Minimum and maximum values
        area = 0.5 * base * height
        print(f"The area of the {shape} is: {area} {units}^2")  # Display the result with user-defined units
        user_info.append({"name": name, "shape": shape, "units": units, "area": f"{area} {units}^2"})
        
    elif shape.startswith('c'):
        print(f"The formula for Area of a circle is A = π × radius^2")
        radius = max_min_input(f"Enter the radius in {units}: ", 0.01, 100)  # Minimum and maximum values
        area = 3.14159 * radius * radius
        print(f"The area of the {shape} is: {area} {units}^2")  # Display the result with user-defined units
        user_info.append({"name": name, "shape": shape, "units": units, "area": f"{area} {units}^2"})
        
    elif shape.startswith('s'):
        print(f"The formula for Area of a square is A = side^2")
        side = max_min_input(f"Enter the side length in {units}: ", 0.01, 100)  # Minimum and maximum values
        area = side * side
        print(f"The area of the {shape} is: {area} {units}^2")  # Display the result with user-defined units
        user_info.append({"name": name, "shape": shape, "units": units, "area": f"{area} {units}^2"})
        
    elif shape.startswith('p'):
        print(f"The formula for Area of a parallelogram is A = base × height")
        base = max_min_input(f"Enter the base length in {units}: ", 0.01, 100)  # Minimum and maximum values
        height = max_min_input(f"Enter the height in {units}: ", 0.01, 100)  # Minimum and maximum values
        area = base * height
        print(f"The area of the {shape} is: {area} {units}^2")  # Display the result with user-defined units
        user_info.append({"name": name, "shape": shape, "units": units, "area": f"{area} {units}^2"})
        
    elif shape.startswith('r'):
        print(f"The formula for Area of a rectangle is A = length × width")
        length = max_min_input(f"Enter the length in {units}: ", 0.01, 100)  # Minimum and maximum values
        width = max_min_input(f"Enter the width in {units}: ", 0.01, 100)    # Minimum and maximum values
        area = length * width
        print(f"The area of the {shape} is: {area} {units}^2")  # Display the result with user-defined units
        user_info.append({"name": name, "shape": shape, "units": units, "area": f"{area} {units}^2"})
        
    else:
        print("I apologize, but the Area/Perimeter tool only knows 5 shapes right now.")

# Define a function to get a valid numeric input within a specified range
def max_min_input(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Define the main function to first ask for the shape and then ask for the units
def main():
    while True:
        show_instructions = yes_no("Have you used the Area/Perimeter tool before? : ")

        if not show_instructions:
            print("**************************")
            print("        INSTRUCTIONS      ")
            print("**************************")
            print("1 Enter your name. ")
            print("2. Choose a shape to calculate: triangle, square, rectangle, circle, or parallelogram.")
            print("2. Enter the required measurements for the selected shape.")
            print("3. Your calculations will be displayed in a table when you finish.")
            print("---------------------------")
            print('If you decide that you are finished with all your calculations even after you say yes ')
            print("---------------------------")
            print("**************************")

        while True:
            user_name = get_name()  # Ask for the user's name
            print(f"Hello, {user_name}!")

            while True:
                reply = input("What shape would you like to calculate? : ").strip().lower()

                if reply != 'xxx':
                    if not reply:
                        print("You did not enter a shape. Please enter a valid shape name or 'xxx' to exit.")
                    elif reply.isalpha():
                        while True:
                            units = input("Enter the units you'd like to use:  ").strip()
                            if units:
                                if not any(char.isdigit() for char in units):
                                    break
                                else:
                                    print("Invalid input. Units cannot contain numbers.")
                            else:
                                print("Invalid input. Please enter the units.")
                        calculate_area(reply, units, user_name)
                        
                        # Ask if the user wants to use the Area/Perimeter tool again
                        repeat = yes_no("Would you like to use the Area/Perimeter tool again?: ")
                        if not repeat:
                            print("Exiting the program.")
                            display_user_info(user_info)  # Display user information in a table
                            return  # Exit the program
                    else:
                        print("Invalid input. Please enter a valid shape name.")
                else:
                    print("Exiting the program.")
                    display_user_info(user_info)  # Display user information in a table
                    return  # Exit the program

# Call the main function to run the program
main()





