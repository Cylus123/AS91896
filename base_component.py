# Define a function to get a yes or no response from the user
def yes_no(question):
    while True:
        reply = input(question).strip().lower()
        if reply.startswith('y'):
            # If the response starts with 'y', return True
            return True
        elif reply.startswith('n'):
            # If the response starts with 'n', return False
            return False
        else:
            # If the response is not 'yes' or 'no', prompt the user again
            print("Please enter 'yes' or 'no'.")

def calculate_area(shape):
    if shape.startswith('t'):
        # If the response starts with 't', that means they want a triangle
        print("The formula for Area of a triangle is A = 1/2 × base × height")
        base = float(input("Enter the base length: "))
        height = float(input("Enter the height: "))
        area = 0.5 * base * height
        return round(area, 2)
        
    elif shape.startswith('c'):
        # If the response starts with 'c', that means they want a circle
        print("The formula for Area of a circle is A = π × radius^2")
        radius = float(input("Enter the radius: "))
        area = 3.14159 * radius * radius
        return round(area, 2)
        
    elif shape.startswith('s'):
        # If the response starts with 's', that means they want a square
        print("The formula for Area of a square is A = side^2")
        side = float(input("Enter the side length: "))
        area = side * side
        return round(area, 2)
        
    elif shape.startswith('p'):
        # If the response starts with 'p', that means they want a parallelogram
        print("The formula for Area of a parallelogram is A = base × height")
        base = float(input("Enter the base length: "))
        height = float(input("Enter the height: "))
        area = base * height
        return round(area, 2)
        
    elif shape.startswith('r'):
        # If the response starts with 'r', that means they want a rectangle
        print("The formula for Area of a rectangle is A = length × width")
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        return round(area, 2)
        
    else:
        # If the response is not one of the recognized shapes, return None
        return None

# Define the main function to run the program
def main():
    # Get the user's response to whether they want to see instructions
    show_instructions = yes_no("Have you used the Area/Perimeter tool before? : ")

    # Check if the user's response is 'n' (no) and display instructions accordingly
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
    
    while True:
        # Ask the user to enter a shape for calculation
        reply = input("What shape would you like to calculate? : ").strip().lower()
    
        if reply != 'xxx':
            if not reply:
                # If the user didn't enter anything for the shape
                print("You did not enter a shape. Please enter a valid shape name or 'xxx' to exit.")
            elif reply.isalpha():
                # If the user entered a valid shape name, calculate the area
                area = calculate_area(reply)
                if area is not None:
                    print(f"The area of the {reply} is: {area}")
                else:
                    print("I apologize, but the Area/Perimeter tool only knows 5 shapes right now. Please enter one of the shapes provided.")
                break  # Break the loop if valid input is provided
            else:
                # If the user entered an invalid input
                print("Invalid input. Please enter a valid shape name.")
        else:
            # If the user entered 'xxx', exit the program
            print("Exiting the program.")
            break

# Call the main function to run the program
main()
