import csv
import time
import calendar
import datetime as dt
import os
import datetime

total_row_count_nar=0
narRowCounter=0
narFile='2018.csv'
powerAlarm1='Power Alarm_W32_2018.csv'
powerAlarm2='Power Alarm_W33_2018.csv'
powerAlarm3='Power Alarm_W34_2018.csv'
powerAlarm4='Power Alarm_W35_2018.csv'
objNar=[]
resultSites=[]

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

def getBackupTime(occurredDate,occurredTime,appearDate,appearTime,ceasedDate,ceasedtime):
	TotalAppareTime=strToDateTime(str(appearDate),str(appearTime))
	TotalCeasedTime=strToDateTime(str(ceasedDate),str(ceasedtime))
	TotalOccurredTime=strToDateTime(str(occurredDate),str(occurredTime))
	loadShedding=TotalCeasedTime-TotalAppareTime
	onBettary=TotalOccurredTime-TotalAppareTime
	# print('loadshheddign: '+str( loadShedding))
	# print('onbattery: '+str(onBettary))
	if TotalAppareTime<=TotalOccurredTime and TotalCeasedTime>=TotalOccurredTime:
		print("works")
		print("works")
		print("works")
		return onBettary
	else:
		return loadShedding 		#if I take load sheddind as back up time

defaultTimeZero=strToDateTime('8/1/2018','23:11')-strToDateTime('8/1/2018','23:11') #To get zero time for initial backUp value in class 

#class starts
class ResultSite:
	ResultBackUp=defaultTimeZero
	ResultCode=None
	ResultOffice=None
	ResultOccurredDateTime=None
	ResultAppearDateTime=None
	ResultCeasedDateTime=None

	def __init__(self, code,office,occurredDateTime,appearDateTime,ceasedDateTime,backUpTime): #constructor
	        self.ResultBackUp = backUpTime
	        self.ResultCode = code
	        self.ResultOffice = office
	        self.ResultOccurredDateTime = occurredDateTime
	        self.ResultAppearDateTime = appearDateTime
	        self.ResultCeasedDateTime = ceasedDateTime

	def displayResult(self): #Object Methods
	    print("code: "+str(self.ResultCode)+", appearDateTime: "+str(self.ResultAppearDateTime)+", occurredDateTime: "+str(self.ResultOccurredDateTime)+", ceasedDateTime: "+str(self.ResultCeasedDateTime)+", backUp: "+str(self.ResultBackUp))

class Site:
	backUp=defaultTimeZero
	code=None
	office=None
	occurredTime=None
	occurredDate=None
	appearDateTime=None
	ceasedDateTime=None

	def __init__(self, code,office,occurredDate,occurredTime): #constructor
	        self.code = code
	        self.office = office
	        self.occurredDate = str(occurredDate)
	        self.occurredTime = str(occurredTime)


	def display(self): #Object Methods
	    print("code: "+str(self.code)+", appear Date Time: "+str(self.appearDateTime)+", occurredDate: "+str(self.occurredDate)+", occurredTime: "+str(self.occurredTime)+", ceased Date Time: "+str(self.ceasedDateTime)+", backUp: "+str(self.backUp))


#class ends

with open(narFile,'rU') as csvfileForRow:
    readCSV = csv.reader(csvfileForRow, delimiter=',')
    csvfileForRow.next()
    total_row_count_nar = len(list(readCSV))


with open(narFile,'rU') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    csvfile.next()
    for row in readCSV:
		narRowCounter=narRowCounter+ 1   
	    	if row[17]=='Site Down' and row[14]=='Power' and row[12]!= ' ' and row[12]!= '0':
	    		#os.system('cls')
		        #print(row)
		        #print(row[17])
		       	#print(row[0],row[1],row[17], row[14])
		        print(str(narRowCounter)+"row fetched out of: "+str(total_row_count_nar))
		        objNar.append(Site(row[1],row[3],row[8],row[9]))
		# if narRowCounter>2000:
		#     break

#os.system('cls')
flag=1
with open(powerAlarm1,'rU') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	csvfile.next()
	for row in readCSV:
		#os.system('cls')
		print(powerAlarm1+": "+str(flag)+" code- "+str(row[0]))
		flag=flag+1
		if row[12]=='MAINS FAIL' and row[10]!='0':	
			# print(row[0],row[1],row[6],row[7],row[8],row[9],row[12])
			for obj in objNar:
				if obj.code==row[0]:
					#print(powerAlarm1+": "+str(flag)+" code- "+str(row[0]))
					# print(row[0],row[1],row[6],row[7],row[8],row[9],row[12])
					backUpTime=getBackupTime(obj.occurredDate,obj.occurredTime,str(row[6]),str(row[7]),str(row[8]),str(row[9]))
					occurredDateTime=strToDateTime(obj.occurredDate,obj.occurredTime)
					appearDateTime=strToDateTime(str(row[6]),str(row[7]))
					ceasedDateTime=strToDateTime(str(row[8]),str(row[9]))
					resultSites.append(ResultSite(obj.code,obj.office,occurredDateTime,appearDateTime,ceasedDateTime,backUpTime))


# for obj in objNar:
#     obj.display()

# for obj in resultSites:
#     obj.displayResult()

# with open('Date.csv', 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(["code","office","occurredDateTime","appearDateTime","ceasedDateTime","backUpTime"]) #heading

#     for obj in resultSites:
#     	wr.writerow([obj.ResultCode,obj.ResultOffice,ResultOccurredDateTime,ResultAppearDateTime,ResultCeasedDateTime,ResultBackUp]) #rows after heading


netCodes=[]
netBackUps=[]

for i in resultSites:
	if i.ResultCode in netCodes:
		arrIndex=netCodes.index(i.ResultCode)
		if netBackUps[arrIndex]<=i.ResultBackUp:
			netBackUps[arrIndex]=i.ResultBackUp
	else:
		netCodes.append(i.ResultCode)
		netBackUps.append(i.ResultBackUp)
	print("fetching the maximum value of each site ... ")

i=0
while i<len(netCodes):
	print(netCodes[i])
	print(netBackUps[i])
	i=i+1

print(len(objNar))
print(len(resultSites))
