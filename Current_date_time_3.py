import datetime
#import time
# print(datetime.datetime.now())
# print(datetime.datetime.today())
# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

today = input("Enter to know current time")
if today == '':
    print(f"Current date and time:\n{datetime.datetime.now()}")
