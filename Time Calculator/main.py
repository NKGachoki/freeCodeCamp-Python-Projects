# Program to calculate added time in 12hr clock format.

from time_calculator import add_time

print(add_time("12:56 PM", "546:12", "SATURDAY"))
print(add_time("1:39 AM", "24:10"))
print(add_time("6:00 PM", "5678:04", "Tuesday"))
print(add_time("7:16 AM", "15:00"))
print(add_time("5:21 PM", "15:40", "WeDnEsDaY"))
print(add_time("11:17 AM", "10000:50", "Monday"))