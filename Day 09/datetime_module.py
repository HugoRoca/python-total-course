# import datetime

# # work in 24 hours
# my_time = datetime.time(17, 35)
# print(my_time)
# print(my_time.minute)
# print(my_time.hour)

# my_other_date = datetime.date(2025, 10, 17)
# print(my_other_date)
# print(my_other_date.year)
# print(my_other_date.ctime())
# print(my_other_date.today())

###########################################

# from datetime import datetime

# my_date = datetime(2025, 5, 15, 22, 10, 15, 2500)
# print(my_date)

# my_date = my_date.replace(month = 11)
# print(my_date)

###########################################
from datetime import date

born = date(1995, 3, 5)
dead = date(2095, 6, 19)

live = dead - born

print(live)
print(live.days)
print(live.month)