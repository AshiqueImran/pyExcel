import csv
import time
import calendar
import datetime as dt
import os
import datetime

total_row_count_nar=0
narRowCounter=0
narFile='2018.csv'
powerAlarm1='Power Alarm_W33_2018.csv'
objNar=[]

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

#class starts

class Site:
	backUp=0
	code=None
	office=None
	occurredTime=None
	occurredDate=None
	appearDate=None
	appearTime=None
	ceasedDate=None
	ceasedtime=None

	def __init__(self, code,office,occurredDate,occurredTime): #constructor
	        self.code = code
	        self.office = office
	        self.occurredDate = str(occurredDate)
	        self.occurredTime = str(occurredTime)


	def display(self): #Object Methods
	    print("code: "+str(self.code)+", office: "+str(self.office)+", occurredDate: "+str(self.occurredDate)+", occurredTime: "+str(self.occurredTime)+", backUp: "+str(self.backUp))


	def addAppearTimeDate(self,appearDate,appearTime):
		if self.appearDate == None:
			self.appearDate=appearDate
		if self.appearTime == None:
			self.appearTime=appearTime
			#mytime = dt.datetime.strptime(appearTime,'%H%M%S').time()
	def getBackupTime(self,appearDate,appearTime,ceasedDate,ceasedtime):
		TotalAppareTime=strToDateTime(appearDate,appearTime)
		TotalCeasedTime=strToDateTime(ceasedDate,ceasedtime)
		TotalOccurredTime=strToDateTime(self.occurredDate,self.occurredTime)
		loadShedding=TotalCeasedTime-TotalAppareTime
		onBettary=TotalOccurredTime-TotalAppareTime
		#print('loadshheddign: '+str( loadShedding))
		#print('onbattery: '+str(onBettary))
		if TotalAppareTime<=TotalOccurredTime and TotalCeasedTime>=TotalOccurredTime:
			approxBackUp=onBettary
		else:
			#approxBackUp=loadShedding 		#if I take load sheddind as back up time
			approxBackUp=datetime.timedelta(0)
		if self.backUp==None:
			self.backUp=approxBackUp
		elif approxBackUp>datetime.timedelta(self.backUp):
			self.backUp=approxBackUp

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
	    		os.system('cls')
		        #print(row)
		        #print(row[17])
		       	#print(row[0],row[1],row[17], row[14])
		        #print(str(narRowCounter)+"row fetched out of: "+str(total_row_count_nar))
		        objNar.append(Site(row[1],row[3],row[8],row[9]))
		if narRowCounter>200:
		    break
flag=1;
with open(powerAlarm1,'rU') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	csvfile.next()
	for row in readCSV:
		print(flag)
		flag=flag+1
		if row[12]=='MAINS FAIL' and row[10]!='0':	
			#print(row[0],row[1],row[12])
			for obj in objNar:
				if obj.code==row[0]:
					obj.getBackupTime(str(row[6]),str(row[7]),str(row[8]),str(row[9]))
					#print(row[0],row[1],row[6],row[7],row[8],row[9],row[12])
					#break


# s1 = Site('DHK_X4283','Gazipur','8/4/2018','16:00')
#s1.addAppearTimeDate('8/30/2018',time.asctime( time.localtime(time.time()) ));
#s1.addAppearTimeDate('8/30/2018','2:37:31 PM')
#print(s1.office)
# s1.getBackupTime('8/1/2018','14:00','8/1/2018','17:00');
# s1.display()


#objNar.append(Site('DHK_X4283','Gazipur','8/28/2018','2:37:31 PM'))
# objNar.append(Site('raj_X4283','Gazipur','8/28/2018','2:37:31 PM'))

for obj in objNar:
    print (obj.code,obj.office,obj.occurredDate,obj.occurredTime,obj.backUp)