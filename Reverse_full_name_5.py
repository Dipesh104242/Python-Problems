user_name = input("Enter here your full name with title:\n")
user_name2 = user_name.split(" ")
#print(user_name2)
for i in range(len(user_name2)//2):
    user_name2[i],user_name2[len(user_name2)-1-i] = user_name2[len(user_name2)-1-i],user_name2[i]
#print(user_name2)
print(f"Your Reversal Name is {' '.join(user_name2)}")