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







  


    
  

    

   
   
