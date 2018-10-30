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
# print(str(strToDateTime(string,time)-strToDateTime('8/1/2018','23:11')))
# print(str(type(strToDateTime(string,time)-strToDateTime('8/1/2018','23:11'))))
subTimes=strToDateTime('2-Aug-18','21:00')-strToDateTime('8/2/2018','01:00')

print(subTimes)


dates=[]

class date1:
		ResultCode=None
		ResultBackUp=None

		def __init__(self,name,netBackUps):
			self.ResultCode=name
			self.ResultBackUp=netBackUps

# dates.append(strToDateTime(string,time)-strToDateTime('8/1/2018','23:11'))
# dates.append(strToDateTime(string,time)-strToDateTime('8/1/2018','23:10'))
# dates.append(strToDateTime(string,time)-strToDateTime('8/2/2018','23:11'))

# print(max(dates))
# print(dates.index(strToDateTime(string,time)-strToDateTime('8/1/2018','23:11')))


# if 'hello' in dates :
# 	print(dates.index('hello'))
# else:
# 	print('does not exist')


# for i in range(10):
# 	dates.append(i+100)

# if 109 in dates :
# 	print(dates.index(109))
# 	dates[dates.index(109)]=8888

# dates.append(date1("ananda",41))
# dates.append(date1("ashik",100))
# dates.append(date1("imran",433))
# dates.append(date1("ashik",133))
# dates.append(date1("imran",403))
# dates.append(date1("sazzed",44))
# dates.append(date1("sazzed",41))
# dates.append(date1("sazzed",46))
# dates.append(date1("sazzed",44))
# dates.append(date1("rahman",44))
# dates.append(date1("ananda",100))
# dates.append(date1("sazzed",44))

# netCodes=[]
# netBackUps=[]
# for i in dates:
# 	for j in dates:
# 		if i.ResultCode== j .ResultCode:
# 			if i.ResultCode in netCodes:
# 				arrIndex=netCodes.index(i.ResultCode)
# 				if netBackUps[arrIndex]<=j.ResultBackUp:
# 					netBackUps[arrIndex]=j.ResultBackUp					
# 			else:
# 				netCodes.append(i.ResultCode)
# 				netBackUps.append(i.ResultBackUp)

# for i in dates:
# 	if i.ResultCode in netCodes:
# 		arrIndex=netCodes.index(i.ResultCode)
# 		if netBackUps[arrIndex]<=i.ResultBackUp:
# 			netBackUps[arrIndex]=i.ResultBackUp
# 	else:
# 		netCodes.append(i.ResultCode)
# 		netBackUps.append(i.ResultBackUp)

#dates.pop(2)

# i=0
# while i<len(netCodes):
# 	print(netCodes[i])
# 	print(netBackUps[i])
# 	i=i+1

# for i in dates:
# 	print[i]
# i=0
# with open('Date.csv', 'wb') as myfile:
# 	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     	wr.writerow(["site","backup"])
#     	while i<len(netCodes):
# 	    	print(netCodes[i])
# 	    	print(netBackUps[i])
# 	    	wr.writerow([str(netCodes[i]),str(netBackUps[i])]) 
# 	    	i=i+1






