
import os
"""file = input("Type here your file name with Extension for extract\n")
fileExtract = file.split(".")
print(f"Your File Extension is {fileExtract[len(fileExtract)-1]}")"""

files = [f for f in os.listdir() if os.path.isfile(f)]
print(files)
files_ext = []
files_root = []
for i in files:
    root, ex = os.path.splitext(i)
    files_ext.append(ex)
    files_root.append(root)
files_ext_set = set(set(files_ext))
print(f"Your file's total extensions {files_ext_set}")
user_input = input("If you want to which extension exist in which file so enter 'y'\notherwise if you want to exit so enter 'no'").strip()
while user_input not in ['y','no']:
    print("Invalid input Please type corecct input['y' or 'no']")
    user_input = input().strip()
if user_input == 'y':
    for i in range(len(files_ext)):
        print(f"{files_root[i]} extension is {files_ext[i]}\n")   
elif user_input == "no":
    exit()
