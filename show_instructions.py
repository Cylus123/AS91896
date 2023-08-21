# Define a function to get a yes or no response from the user
def yes_no(question):
    while True:
        # Prompt the user and convert their response to lowercase and strip whitespace
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

# Get the user's response to whether they want to see instructions
show_instructions = yes_no("Do you want to see instructions? ")

# Check if the user's response is 'n' (no) and display instructions accordingly
if not show_instructions:
    print("**************************")
    print("        INSTRUCTIONS      ")
    print("**************************")
    print("1. Enter your name.")
    print("2. Choose a shape to calculate: triangle, square, rectangle, circle, or parallelogram.")
    print("3. Enter the required measurements for the selected shape.")
    print("4. Your calculations will be displayed in a table when you finish.")
    print("**************************")






  


    
  

    

   
   
