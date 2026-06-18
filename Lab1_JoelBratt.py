import math
import circle as c
import rectangle as r
"""
Geomtery Calc
Joel Bratt
Calculates Circle Area and Circumference as well as retangle Area and Perimiter
6/17/2026
"""

#Aliases are used in the case of both files sharing a function name so the program knows which one to use.

selection = 0
while selection != 5:
    print("Geometry Calculator \n" \
    "------------------------------------ \n" \
    "1. Calculate Circle Area \n" \
    "2. Calculate Circle Circumference \n" \
    "3. Calculate Retangle Area \n" \
    "4. Calculate Retangle Perimiter \n" \
    "5. Exit \n"  )

    selection = int(input("Enter your selection 1-5 "))

    print(f"{selection} Great Choice!")
    
    if selection == 1:
        radius = float(input("Input radius: "))
        circle_area = c.circle_area(radius)
        print(f"Circle area is {circle_area:.2f} .")
    
    elif selection == 2:
        radius = float(input("Input radius: "))
        circle_circumference = c.circle_circumference(radius)
        print(f'Circle circumference is {circle_circumference:.2f}')
    
    elif selection == 3:
        width = float(input("Input width: "))
        height = float(input("input height: "))
        rectangle_area = r.rectangle_area(width, height)
        print(f'Rectangle area is {rectangle_area:.2f}')

    elif selection == 4:
        width = float(input("Input width: "))
        height = float(input("input height: "))
        rectangle_perimeter = r.rectangle_perimeter(width, height)
        print(f'Rectangle perimeter is {rectangle_perimeter:.2f}')


    







