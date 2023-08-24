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

# Define a function to calculate the area of a given shape
def calculate_area(shape, measurements):
    if shape.startswith('t'):
        # If the response starts with 't', that means they want a triangle
        base = measurements[0]
        height = measurements[1]
        area = 0.5 * base * height
        return area
        
    elif shape.startswith('c'):
        # If the response starts with 'c', that means they want a circle
        radius = measurements[0]
        area = 3.14159 * radius * radius
        return area
        
    elif shape.startswith('s'):
        # If the response starts with 's', that means they want a square
        side = measurements[0]
        area = side * side
        return area
        
    elif shape.startswith('p'):
        # If the response starts with 'p', that means they want a parallelogram
        base = measurements[0]
        height = measurements[1]
        area = base * height
        return area
        
    elif shape.startswith('r'):
        # If the response starts with 'r', that means they want a rectangle
        length = measurements[0]
        width = measurements[1]
        area = length * width
        return area
        
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
                # If the user entered a valid shape name, prompt for measurements
                measurements = []
                for i in range(2):
                    measurement = float(input(f"Enter measurement {i+1} for the {reply}: "))
                    measurements.append(measurement)
                
                area = calculate_area(reply, measurements)
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


