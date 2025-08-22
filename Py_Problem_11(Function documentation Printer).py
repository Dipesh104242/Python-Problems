import inspect
while 1:
    user_input = input("Enter here Python's built-in function name to print it's documentation\n\n").strip()
    if user_input:
        long_or_short = input("Type 1 for long doc\nType 2 for short doc\n")
        if long_or_short == "1":
         print(inspect.getdoc(user_input)) 
        elif long_or_short  == "2":
           print(f"{user_input.__doc__}")
    replay = input("Type 'y' to continue and type 'q' to quite from this programe\n")
        

