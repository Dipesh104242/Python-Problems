
while True:
    import sys
    import pkg_resources
    import importlib

        # Get list of built-in module names
    list_of_builtin = list(sys.builtin_module_names)
    builtin = []
    builtin2 = []
    external_module = [d.project_name for d in pkg_resources.working_set]

    # Process built-in modules (remove underscores)
    for i in range(len(list_of_builtin)):
        v = list(list_of_builtin[i])
        if "_" not in v:
            builtin.append(v)
        elif "_" in v:
            v.remove("_")
            builtin.append(v)

    # Convert character lists back to strings
    for i in builtin:
        g = "".join(i)
        builtin2.append(g)

    print("Welcome to 'Version Checker'")
    print("i. If you want to see 'Python Version' so enter '1'.\nii. If you want to module's version so enter '2'")
    user_y = input().strip()

    # Validate user input
    while user_y not in ['1', '2']:
        print("Please type correct input (1 or 2)\n")
        user_y = input().strip()

    if user_y == '1':
        print(f"Your Python's version is {sys.version}")
    elif user_y == '2':
        module_name = input("Type here your module name\n").strip()
        
        # Normalize module name for comparison
        while module_name not in builtin2 and module_name not in external_module:
            print("Incorrect input sir!\nI think you entered a wrong module name or this module doesn't exist in your system.\nPlease try again:\n")
            module_name = input("Type here your module name\n").strip()

        if module_name in builtin2:
            print(f"Sorry sir, {module_name} is a built-in module that comes with Python.\n"
                f"So this module's version is the same as your Python version.\n"
                f"Your Python version: {sys.version}")
        elif module_name in external_module:
            try:
                # Import the module
                module = importlib.import_module(module_name)
                # Try to get the version
                version = getattr(module, '__version__', None)
                if version:
                    print(f"Your module's version is {version}")
                else:
                    print(f"The module {module_name} does not have a '__version__' attribute.")
            except ImportError:
                print(f"Failed to import module {module_name}. It may not be installed or the module name may be incorrect.")
            except Exception as e:
                print(f"An error occurred while checking the version of {module_name}: {str(e)}")

    replay = input("If you want check again so type 'y' or 'yes' otherwise if you want to quite so that type 'q'\n").strip()
    while replay not in ['y','yes','q']:
        print("Incorrect input\n"
        "Please type correct (y, yes, or q)")
    if replay in ['y', 'yes']:
        continue
    elif replay == 'q':
        break
    