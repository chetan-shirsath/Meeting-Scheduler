'''
 A team meeting schedular on the first Monday of every month.
'''
from datetime import date
import calendar

#Take input from user
start_month = int(input("Enter your first month number to start the meetings : "))
end_month = int(input("Enter your last month number to start the meetings : "))

#open the file with file name and the action which we want to do
f = open("Meeting_Schedular.txt", "w+")
f.write("Team meetings for %s to %s will be on : \r\n" % (calendar.month_name[start_month], calendar.month_name[end_month - 1]))

for mon in range(start_month, end_month):
    # returns an array of weeks that represent the month
    cal = calendar.monthcalendar(date.today().year, mon)
    # The first monday has to be within the first two weeks
    first_week = cal[0]
    second_week = cal[1]
    if first_week[calendar.MONDAY] != 0:
        meetday = first_week[calendar.MONDAY]
    else:
        # if the first monday isn't in the first week, it must be in the second
        meetday = second_week[calendar.MONDAY]
    #writing data to the file
    f.write("%2d %1s, MONDAY At 10am \r\n" % (meetday, calendar.month_name[mon]))

#Close the file
f.close()