from datetime import datetime, date, time

year = 0
month = 0
day = 0
pregnancy = 40   # a pregnancy lasts 40 weeks


def week_converter(year, month, day):
	
	week = date(year, month, day).isocalendar()[1]
	print week

	if week < pregnancy:
		new_week = 52 + (week - pregnancy)
		year = year - 1
		return new_week, year 

	else:
		new_week = week - pregnancy
		return new_week



print week_converter(2016, 4, 28)
print year



	



