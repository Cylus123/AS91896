while True:
    reply = input("What shape would you like to calculate?: ").strip().lower()
    
    if reply.startswith('tri'):
        # If the response starts with 'tri', that means they want a triangle
        print("The formula for Area of a triangle is A = 1/2 × b × h")
      
    elif reply.startswith('cir'):
        # If the response starts with 'cir', that means they want a circle
        print("The formula for Area of a circle is A = π × r^2")
        
    elif reply.startswith('squ'):
        # If the response starts with 'squ', that means they want a square
        print("The formula for Area of a square is A = a^2")
        
    elif reply.startswith('par'):
        # If the response starts with 'par', that means they want a parallelogram
        print("The formula for Area of a parallelogram is A = b x h")
        
    elif reply.startswith('rec'):
        # If the response starts with 'rec', that means they want a rectangle
        print("The formula for Area of a rectangle is A = L x W")
        
    else:
        # If the response is not one of the recognized shapes, prompt the user again
        print("I apologize, but the Area/Perimeter tool only knows 5 shapes right now. Please enter one of the shapes provided.")

