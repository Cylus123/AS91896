while True:
    reply = input("What shape would you like to calculate ?: ").strip().lower()
    if reply.startswith('t'):
        # If the response starts with 't', that means they want triangle
      print("The formula for Area of a triangle is A = 1/2 × b ×  h"  )         
      triangle_formula_base = int(input("What would you like to enter for B(base)"))
      triangle_formula_base2 = int(input("What would you like to enter for H(height)"))
      
    elif reply.startswith('c'):
      print("The formula for Area of a circle is A = π × r^2"  )              
      circle_formula_radius = int(input("What would you like to enter for R(radius)"))

    elif reply.startswith('s'):
      print("The formula for Area of a square is A = a^2"  )              
     square_formula_area = int(input("What would you like to enter for A()"))
     elif reply.startswith('p'):
      print("The formula for Area of a parallelogram is A = b x h"  )              
       parallelogram_formula_base = int(input("What would you like to enter for B(base)"))
      parallelogram_formula_base2 = int(input("What would you like to enter for H(height)"))

     elif reply.startswith('r'):
      print("The formula for Area of a parallelogram is A = L x W"  )              
       parallelogram_formula_base = int(input("What would you like to enter for L(length)"))
      parallelogram_formula_base2 = int(input("What would you like to   enter for W(width)"))


        # If the response starts with 'n', 
        
    else:
        # If the response is not 'yes' or 'no', prompt the user again
        print("I apoligise but the Area/Perimeter tool only knows 5 shapes right now, please enter one of the shapes provided: ")
