import csv
import time
import calendar
import datetime as dt
import os



import datetime

# s = "8 March, 2017"
# d = datetime.strptime(s, '%d %B, %Y')
# print(d.strftime('%Y-%m-%d'))

# x = datetime.datetime(2020, 5, 17)
# print(x)

def strToDateTime(dateString,timeString):
	if '-' in dateString:
		dateParts=dateString.split('-')
		if dateParts[1].lower()=='jan':
			month=1
		elif dateParts[1].lower()=='feb':
			month=2
		elif dateParts[1].lower()=='mar':
			month=3
		elif dateParts[1].lower()=='apr':
			month=4
		elif dateParts[1].lower()=='may':
			month=5
		elif dateParts[1].lower()=='jun':
			month=6
		elif dateParts[1].lower()=='jul':
			month=7
		elif dateParts[1].lower()=='aug':
			month=8
		elif dateParts[1].lower()=='sep':
			month=9
		elif dateParts[1].lower()=='oct':
			month=10
		elif dateParts[1].lower()=='nov':
			month=11
		elif dateParts[1].lower()=='dec':
			month=12
		year=int(dateParts[2])
		year+=2000
		day=int(dateParts[0])

	elif '/' in dateString:
		dateParts2=dateString.split('/')
		year=int(dateParts2[2])
		day=int(dateParts2[1])
		month=int(dateParts2[0])

	if ':' in timeString:
		timeParts=timeString.split(':')
		hour=int(timeParts[0])
		minute=int(timeParts[1])
	return datetime.datetime(year, month, day,hour,minute)


string='8/2/2018'
time='23:12'
# f_type_parts = string.split('-')
# print(f_type_parts);
# print(f_type_parts[0]);
# print(f_type_parts[1]);
# print(f_type_parts[2]);
#print(str(strToDateTime(string,time)-strToDateTime('8/1/2018','23:11')))

dates=[]

# dates.append(strToDateTime(string,time)-strToDateTime('8/1/2018','23:11'))
# dates.append(strToDateTime(string,time)-strToDateTime('8/1/2018','23:10'))
# dates.append(strToDateTime(string,time)-strToDateTime('8/2/2018','23:11'))

# print(max(dates))
# print(dates.index(strToDateTime(string,time)-strToDateTime('8/1/2018','23:11')))


# if 'hello' in dates :
# 	print(dates.index('hello'))
# else:
# 	print('does not exist')


for i in range(10):
	dates.append(i+100)

if 109 in dates :
	print(dates.index(109))
	dates[dates.index(109)]=8888

for i in dates:
	print[i]



