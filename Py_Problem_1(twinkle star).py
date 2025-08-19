"""Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are"""

string =  "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
split_str = string.split("!")
first_str = split_str[0]
second_str = split_str[1]

print(first_str[0:31])
secoffirst = first_str[31:34].rjust(10," ")
print(f"{secoffirst} {first_str[35:]}")
firstofsec = second_str[1:3].rjust(14," ")
print(f"{firstofsec} {second_str[4:28]}")
secofsec = second_str[29:33].rjust(16," ")
print(f'{secofsec} {second_str[34:55]}')
thirdofsec = second_str[56:86]
print(thirdofsec)
fourthofsec = second_str[87:90].rjust(10," ")
print(f"{secoffirst} {second_str[91:]}")

