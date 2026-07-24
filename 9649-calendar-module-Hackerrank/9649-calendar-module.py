# Enter your code here. Read input from STDIN. Print output to STDOUT
month,day,year=list(map(int,input().split()))
import calendar
print(calendar.day_name[calendar.weekday(year, month, day)].upper())


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna