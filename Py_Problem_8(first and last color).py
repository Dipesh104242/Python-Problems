#First and Last Colors

colors = input("Enter here your all color\n")
while "," not in colors:
        print("Please type your colors names with commas")    
        colors = input("Enter here your all color\n")
try:
        colors_list = colors.split(',')
        print(colors_list[0])
        print(colors_list[len(colors_list)-1])

except Exception as e:
        print(e)
