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

def calculate_area():
    while True:
        reply = input("What shape would you like to calculate? (Enter 'xxx' to exit): ").strip().lower()

        if reply == 'xxx':
            print("Exiting the program.")
            break  # Exit the loop if the user enters 'xxx'

        if reply.isalpha():
            if reply.startswith('t'):
                # If the response starts with 't', that means they want a triangle
                print("The formula for Area of a triangle is A = 1/2 × b × h")

            elif reply.startswith('c'):
                # If the response starts with 'c', that means they want a circle
                print("The formula for Area of a circle is A = π × r^2")

            elif reply.startswith('s'):
                # If the response starts with 's', that means they want a square
                print("The formula for Area of a square is A = a^2")

            elif reply.startswith('p'):
                # If the response starts with 'p', that means they want a parallelogram
                print("The formula for Area of a parallelogram is A = b x h")

            elif reply.startswith('r'):
                # If the response starts with 'r', that means they want a rectangle
                print("The formula for Area of a rectangle is A = L x W")

            else:
                # If the response is not one of the recognized shapes, prompt the user again
                print("I apologize, but the Area/Perimeter tool only knows 5 shapes right now. Please enter one of the shapes provided.")
        else:
            print("Invalid input. Please enter a valid shape name.")

# Call the function to run it
calculate_area()
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
    print("4.Your calculations will be displayed in a table when you finish")

    print('If you decide that you are finished with all your calculations type in the code "xxx" and it will automaticlly exit you out of the program!')
    print("**************************")