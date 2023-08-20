def yes_no(question):
    while True:
        reply = input(question).strip().lower()
        if reply.startswith('y'):
            return True
        elif reply.startswith('n'):
            return False
        else:
            print("Please enter 'yes' or 'no'.")

show_instructions = yes_no("Yes or no? ")

if not show_instructions:
    print("**************************")
    print("        INSTRUCTIONS      ")
    print("**************************")
    print("1. Enter your name.")
    print("2. Enter the shape you'd like to calculate (Choose from either a triangle, square, rectangle, circle, or parallelogram).")
    print("3. Enter the numbers into the showen formula.")
    print("4. You will recive your calculations on a table when you wish to be finished with all your calculations ")
    print("**************************")





  


    
  

    

   
   
