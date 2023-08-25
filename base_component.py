# Define a function to get a yes or no response from the user
def yes_no(question):
    while True:
        reply = input(question).strip().lower()
        if reply.startswith('y'):
            return True
        elif reply.startswith('n'):
            return False
        else:
            print("Please enter 'yes' or 'no.")

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
def calculate_area(shape, units):
    if shape.startswith('t'):
        print(f"The formula for Area of a triangle is A = 1/2 × base × height")
        base = float(input(f"Enter the base length in {units}: "))
        height = float(input(f"Enter the height in {units}: "))
        area = 0.5 * base * height
        return round(area, 2)
        
    elif shape.startswith('c'):
        print(f"The formula for Area of a circle is A = π × radius^2")
        radius = float(input(f"Enter the radius in {units}: "))
        area = 3.14159 * radius * radius
        return round(area, 2)
        
    elif shape.startswith('s'):
        print(f"The formula for Area of a square is A = side^2")
        side = float(input(f"Enter the side length in {units}: "))
        area = side * side
        return round(area, 2)
        
    elif shape.startswith('p'):
        print(f"The formula for Area of a parallelogram is A = base × height")
        base = float(input(f"Enter the base length in {units}: "))
        height = float(input(f"Enter the height in {units}: "))
        area = base * height
        return round(area, 2)
        
    elif shape.startswith('r'):
        print(f"The formula for Area of a rectangle is A = length × width")
        length = float(input(f"Enter the length in {units}: "))
        width = float(input(f"Enter the width in {units}: "))
        area = length * width
        return round(area, 2)
        
    else:
        return None

# Define the main function to run the program
def main():
    show_instructions = yes_no("Have you used the Area/Perimeter tool before? : ")

    if not show_instructions:
        print("**************************")
        print("        INSTRUCTIONS      ")
        print("**************************")
        print("1. Enter your name.")
        print("2. Choose a shape to calculate: triangle, square, rectangle, circle, or parallelogram.")
        print("3. Enter the required measurements for the selected shape.")
        print("4. Your calculations will be displayed in a table when you finish.")
        print('If you decide that you are finished with all your calculations, type in the code "xxx" to exit the program.')
        print("**************************")
    
    units = input("Enter the units you'd like to use (e.g., meters, centimeters, inches): ")
    
    while True:
        reply = input("What shape would you like to calculate? : ").strip().lower()
    
        if reply != 'xxx':
            if not reply:
                print("You did not enter a shape. Please enter a valid shape name or 'xxx' to exit.")
            elif reply.isalpha():
                area = calculate_area(reply, units)
                if area is not None:
                    print(f"The area of the {reply} is: {area} {units}^2")  # Display the result with user-defined units
                else:
                    reply = input("I apologize, but the Area/Perimeter tool only knows 5 shapes right now. Please enter one of the shapes provided.")
                break
            else:
                print("Invalid input. Please enter a valid shape name.")
        else:
            print("Exiting the program.")
            break

# Call the main function to run the program
main()

