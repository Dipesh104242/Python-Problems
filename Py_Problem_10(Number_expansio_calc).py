while 1:

    try:
        user_input = float(input("Enter here your integer inputs\n"))

        user_output = user_input+(user_input*user_input)+(user_input*user_input*user_input)
        print(f"Sampale input of n  is {int(user_input)}")
        print(f"Expected Result : {int(user_output)}")
    except Exception as e:
        print("Invalid. Please press integer or float", e) 
        
    re_start = input('If you want to replay this again so type "y" otherwise type "n"\n').strip()
    while re_start not in ["y" , 'n']:
        print("This is invalid please type valid input [y or n]")
        re_start = input("Enter here:\n")
    if re_start == 'y':
        continue
    elif re_start == "n":
        break        