def yes_no(question):
    while True:
        reply = input(question).strip().lower()
        if reply.startswith('y'):
            return True
        elif reply.startswith('n'):
            return False
        else:
            print("Please enter 'yes' or 'no'.")

show_instructions = yes_no("Have you used the Area/Perimeter tool before ?: ")

if not show_instructions:
    print("**************************")
    print("        INSTRUCTIONS      ")
    print("**************************")
    print("1. Enter your name.")
    print("2. Choose a shape to calculate: triangle, square, rectangle, circle, or parallelogram.")
    print("3. Enter the required measurements for the selected shape.")
    print("4. Your calculations will be displayed in a table when you finish.")
    print("**************************")





  


    
  

    

   
   
