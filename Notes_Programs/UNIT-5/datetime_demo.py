"""
=========================================
DATETIME MODULE 
=========================================
"""

from datetime import datetime, date

# ------------------------------------------------------------
# 1. Print current date, time, day, month, year
# ------------------------------------------------------------

now = datetime.now()   # Get current local date & time

print("=== CURRENT DATE AND TIME ===")
print("Current Date:", now.date())      # Only date
print("Current Time:", now.time())      # Only time
print("Day:", now.day)                  # Day from date
print("Month:", now.month)              # Month number
print("Year:", now.year)                # Year
print()

"""
Sample Output:
===============
Current Date: 2025-12-08
Current Time: 11:22:45.987654
Day: 8
Month: 12
Year: 2025
"""

# ------------------------------------------------------------
# 2. Find number of days between two dates (user input)
# ------------------------------------------------------------

print("=== NUMBER OF DAYS BETWEEN TWO DATES ===")

# Taking input as "YYYY MM DD" and converting using map()
# map(int, ...) converts each part of string input → integer
y1, m1, d1 = map(int, input("Enter first date (YYYY MM DD): ").split())
y2, m2, d2 = map(int, input("Enter second date (YYYY MM DD): ").split())

# Create date objects
date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

# Subtract → timedelta
difference = date2 - date1

print("\nDate 1:", date1)
print("Date 2:", date2)
print("Difference:", difference)
print("Number of days:", difference.days)
print()

"""
Sample Output:
===============
Enter first date (YYYY MM DD): 2024 03 15
Enter second date (YYYY MM DD): 2025 01 10

Date 1: 2024-03-15
Date 2: 2025-01-10
Difference: 301 days, 0:00:00
Number of days: 301
"""

# ------------------------------------------------------------
# 3. Calendar of any month and year
# ------------------------------------------------------------

import calendar

print("=== CALENDAR OF A PARTICULAR MONTH ===")

year = int(input("Enter year (e.g., 2025): "))
month = int(input("Enter month (1-12): "))

print("\nCalendar for", calendar.month_name[month], year)
print(calendar.month(year, month))

"""
Sample Output:
===============
Enter year (e.g., 2025): 2025
Enter month (1-12): 12

Calendar for December 2025
   December 2025
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
"""
