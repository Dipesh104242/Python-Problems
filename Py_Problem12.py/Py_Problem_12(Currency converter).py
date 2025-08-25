#directory change
import os
os.chdir(r"C:\Users\pc\Documents\python_problems\Py_Problem12.py")
#Open file
with open("data.txt") as f:
    lines = f.readlines()

currencydict = {}
#create a currency dictionary with money name
for line in lines:
    parsed = line.strip().split('\t')
    if len(parsed) >= 2:
        currencydict[parsed[0]] = parsed[1]
#print(currencydict)
amount = int(input("Enter amount:\n"))
print("enter the nme of currency you want to convert this amount to: Availble Opetions:\n")
[print(item) for item in currencydict.keys()]
currency = input("Please enter one of these values:\n")

#Last output
print(f"{amount} INR is equal to {amount*float(currencydict[currency])} {currency}")
    