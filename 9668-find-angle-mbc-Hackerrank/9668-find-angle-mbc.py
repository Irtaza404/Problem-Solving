# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab=float(input())
bc=float(input())
angle_radians = math.atan2(ab, bc)
angle_degrees = math.degrees(angle_radians)
print(f"{round(angle_degrees)}{chr(176)}")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna