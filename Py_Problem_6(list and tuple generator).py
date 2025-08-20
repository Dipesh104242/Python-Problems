user_input = (input("Enter here your some numbers\n"))
user_input2 = list(user_input)
list_of_input = []
tuple_of_input = list()
for i in list(user_input):
    if i == ",":
        user_input2.remove(",")
for i in user_input2:
    
    str(i)
    list_of_input.append(i)
    tuple_of_input.append(i)
tuple_of_input2 = tuple(tuple_of_input)
print(list_of_input)
print(tuple_of_input2)