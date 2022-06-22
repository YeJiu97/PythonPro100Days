num = int(input("Please enter a number here: "))

rem_year = 90-num  # years

rem_mon = rem_year*12
rem_week = rem_year*52
rem_day = rem_year*365

print("You have",rem_day,"days,", rem_week, "weeks, and", rem_mon,"months left.")