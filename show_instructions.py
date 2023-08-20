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
    print("2. Enter your age.")
    print("3. Make the payment (cash or credit).")
    print("4. You will be entered into the draw to win a prize.")
    print("5. If your name is called out, please come to collect your prize.")
    print("**************************")





  


    
  

    

   
   
