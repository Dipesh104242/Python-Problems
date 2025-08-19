while 1:
    import math
    p = math.pi
    radius = float(input("Enter here your circle's radius\n"))
    if radius>=2:
        radius2 = pow(radius,2)
        print(f"Area = {p*radius2} cm\u00b2")
        print(f"Diameter = {radius*2} cm\u00b2")
        print(f"Circumference = {2*p*radius} cm\u00b2")
        exit()
    else:
        d = radius*radius
        print(f"Area = {p*d} cm\u00b2")
        print(f"Diameter = {radius*2} cm\u00b2")
        print(f"Circumference = {2*p*radius} cm\u00b2")
    replay = input("If you want to try this again so that type 'y' otherwise type 'no'").strip()
    while replay not in ['y','no']:
        print("Incorrect input!")
        replay = input("If you want to try this again so that type 'y' otherwise type 'no'").strip()

    if replay == 'y':
        continue
    else:
        break

