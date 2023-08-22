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




