#this is my hand written programme

# import datetime
# print("This is Exam date Calculator\n")
# print("Just give it some input correctly then\nit will give you exam date and how many days left for your exam")

# date = int(input("Date:\n"))
# while date>31:
#     print("Incorrect input Please type valid!(1-31)")
#     date = int(input("Date:\n"))
# month =  int(input("Month\n"))
# while month>12:
#     print("Incorrect input Please type valid!(1-12)")
#     month = int(input("Month:\n"))
# year = list(input("Year(Please type 4 digit date)\n"))
# while len(year) != 4:
#     print("Incorrect! Please type year with 4 digit number\n")
#     year = list(input("Year(Please type 4 digit date)\n"))

# print("Please type correct exact time of you exam when from start this exam\n")
# hour = input("Hour:\n")
# while int(hour)>12 and int(hour)<0:
#     print("Sorry this programme don't use train time so type")
#     hour = input("Hour:\n")
# minute = input("Minute:\n")
# while int(minute) > 60 and int(minute)<0:
#     print("Invalid! input\n")
#     minute = input("Minute:\n")

# year = "".join(year)
# exam_st_date = str(f"{year}-{month}-{date} {hour}:{minute}")    

# current_date = str(datetime.datetime.today())
# current_date_time_seperate = current_date.split(" ")
# current_date_seperate = current_date_time_seperate[0].split("-")
# strptime = datetime.datetime.strptime(exam_st_date,"%Y-%m-%d %H:%M")
# seperate_of_time_date = str(strptime).split(" ")
# seperate_date = seperate_of_time_date[0].split('-')
# left_year = int(seperate_date[0])-int(current_date_seperate[0])
# if int(current_date_seperate[0])>=int(seperate_date[0]):
#     left_year == 0
# left_month = int(seperate_date[1])-int(current_date_seperate[1])
# if int(current_date_seperate[1])>=int(seperate_date[1]):
#     left_month = 0
# left_days = int(seperate_date[2])-int(current_date_seperate[2])
# if int(current_date_seperate[2])>=int(seperate_date[2]):
#     left_days = 0

# curract_time_left = f"{left_year} year, {left_month} month, and {left_days} days"

# print("Your exam date is:", strptime)

# user_check = input("If you want to print how many days left from this exam so print 'y'\notherwise if you want to quite so type 'q'")
# while user_check not in ['y','q']:
#     print("Invalid! please type correct('y','q')")
#     user_check  = input()
# if user_check == 'y':
#     print(f"Your time left for exam is: ",curract_time_left)
# elif user_check == 'q':
#     exit()

#this is grok programme
import datetime

def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def validate_date(year, month, date):
    """Validate if the date is valid for the given month/year."""
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        days_in_month[1] = 29
    return 1 <= date <= days_in_month[month - 1]

def get_input(prompt, validator=None, error_msg="Invalid input!"):
    """Helper to get validated input."""
    while True:
        try:
            value = input(prompt)
            if validator and not validator(value):
                print(error_msg)
                continue
            return value
        except ValueError:
            print(error_msg)

def main():
    print("This is an Improved Exam Date Calculator")
    print("Enter details correctly to get your exam date and time left.")

    while True:  # Loop for multiple exams
        # Get year
        year_str = get_input("Year (4-digit, e.g., 2025):\n", 
                             validator=lambda y: len(y) == 4 and y.isdigit() and int(y) >= datetime.datetime.now().year,
                             error_msg="Invalid year! Must be 4 digits and current or future year.")
        year = int(year_str)

        # Get month
        month_str = get_input("Month (1-12):\n", 
                              validator=lambda m: m.isdigit() and 1 <= int(m) <= 12,
                              error_msg="Invalid month! Must be 1-12.")
        month = int(month_str)

        # Get date with validation
        def date_validator(d):
            return d.isdigit() and 1 <= int(d) <= 31 and validate_date(year, month, int(d))
        date_str = get_input("Date (1-31, depending on month):\n", 
                             validator=date_validator,
                             error_msg="Invalid date! Check days in month or leap year.")
        date = int(date_str)

        print("Enter exam start time (24-hour format, e.g., 14:30 for 2:30 PM).")
        
        # Get hour (24-hour)
        hour_str = get_input("Hour (0-23):\n", 
                             validator=lambda h: h.isdigit() and 0 <= int(h) <= 23,
                             error_msg="Invalid hour! Must be 0-23.")
        hour = int(hour_str)

        # Get minute
        minute_str = get_input("Minute (0-59):\n", 
                               validator=lambda m: m.isdigit() and 0 <= int(m) <= 59,
                               error_msg="Invalid minute! Must be 0-59.")
        minute = int(minute_str)

        # Create exam datetime
        exam_datetime = datetime.datetime(year, month, date, hour, minute)
        print(f"Your exam date is: {exam_datetime}")

        # Calculate time left
        now = datetime.datetime.now()
        if exam_datetime < now:
            print("This exam is in the past! Time has already passed.")
            time_left_str = "Exam over"
            total_days_left = 0
        else:
            delta = exam_datetime - now
            total_seconds = int(delta.total_seconds())
            total_days_left = delta.days
            weeks_left = total_days_left // 7
            days_left = total_days_left % 7
            hours_left = (total_seconds // 3600) % 24
            minutes_left = (total_seconds // 60) % 60

            # Approximate years and months (rough, since months vary)
            years_left = (exam_datetime.year - now.year)
            months_left = (exam_datetime.month - now.month) + (years_left * 12)
            if months_left < 0:
                months_left = 0
            if exam_datetime.day < now.day:
                months_left -= 1
            years_left = months_left // 12
            months_left %= 12

            time_left_str = f"{years_left} year{'s' if years_left != 1 else ''}, " \
                            f"{months_left} month{'s' if months_left != 1 else ''}, " \
                            f"{days_left} day{'s' if days_left != 1 else ''}, " \
                            f"{hours_left} hour{'s' if hours_left != 1 else ''}, " \
                            f"{minutes_left} minute{'s' if minutes_left != 1 else ''}"
            
            print(f"Time left for exam: {time_left_str}")
            print(f"Total days left: {total_days_left}")
            print(f"Approximate weeks left: {weeks_left}")

            # Study reminder
            if total_days_left < 7:
                print("Study tip: Start revising intensively now!")
            elif total_days_left < 30:
                print("Study tip: Make a study plan and stick to it.")
            else:
                print("Study tip: Begin with light preparation and build up.")

        # Ask for more actions
        choice = get_input("Enter 'y' to see time left again, 'n' for new exam, 'q' to quit:\n", 
                           validator=lambda c: c.lower() in ['y', 'n', 'q'],
                           error_msg="Invalid! Enter 'y', 'n', or 'q'.")
        choice = choice.lower()
        if choice == 'q':
            break
        elif choice == 'y' and time_left_str != "Exam over":
            print(f"Time left: {time_left_str}")

if __name__ == "__main__":
    main()