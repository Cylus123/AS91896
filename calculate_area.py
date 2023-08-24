def calculate_area(shape):
    if shape.startswith('t'):
        print("The formula for Area of a triangle is A = 1/2 × b × h")
        base = float(input("Enter the base length: "))
        height = float(input("Enter the height: "))
        area = 0.5 * base * height
        return area
        
    elif shape.startswith('c'):
        print("The formula for Area of a circle is A = π × r^2")
        radius = float(input("Enter the radius: "))
        area = 3.14159 * radius * radius
        return area
        
    elif shape.startswith('s'):
        print("The formula for Area of a square is A = a^2")
        side = float(input("Enter the side length: "))
        area = side * side
        return area
        
    elif shape.startswith('p'):
        print("The formula for Area of a parallelogram is A = b × h")
        base = float(input("Enter the base length: "))
        height = float(input("Enter the height: "))
        area = base * height
        return area
        
    elif shape.startswith('r'):
        print("The formula for Area of a rectangle is A = l × w")
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        return area
        
    else:
        return None

while True:
    shape = input("What shape would you like to calculate? : ").lower().strip()
    
    if shape.lower() == 'exit':
        break
    
    area = calculate_area(shape)
    
    if area is not None:
        print(f"The area of the {shape} is {area}")
    else:
        print("Sorry, I don't recognize that shape.")
