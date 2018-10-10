import csv
import time
import calendar
import datetime as dt
import os
import datetime

narFiles=[]
netCodes=[]
counts=[]
dates=[]
narRowCounter=0

outputFileName='Power_outage_per_site_per_day_May_2018.csv' #all the results will be stored here

narFiles.append('monthly/May_2018.csv')	#input files


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

	return datetime.datetime(year, month, day,hour,minute,00)


for narFile in narFiles:

	with open(narFile,'rU') as csvfileForRow:
	    readCSV = csv.reader(csvfileForRow, delimiter=',')
	    csvfileForRow.next()
	    total_row_count_nar = len(list(readCSV))

	os.system('cls')

	print('fetching from: '+narFile)

	with open(narFile,'rU') as csvfile:
	    readCSV = csv.reader(csvfile, delimiter=',')
	    csvfile.next()
	    for row in readCSV:
			narRowCounter=narRowCounter+ 1   
		    	if row[19]=='Site Down' and row[16]=='Power' and row[14]!= ' ' and row[14]!= '0':

			    	print(str(narRowCounter)+"row fetched out of: "+str(total_row_count_nar)+'from: '+narFile)
			        if row[1] in netCodes:
			        	arrIndex=netCodes.index(row[1])
			        	counts[arrIndex]+=float(row[15])
			        else:
			        	netCodes.append(row[1])
			        	counts.append(float(row[15]))
			

i=0
with open(outputFileName, 'wb') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    	wr.writerow(["site","counts"])
    	while i<len(netCodes):
	    	print(netCodes[i])
	    	netCount=counts[i]/(60*4*30)
	    	print(netCount)
	    	wr.writerow([str(netCodes[i]),str(netCount)]) 
	    	i=i+1