import csv
import time
import calendar
import datetime as dt
import os

total_row_count_nar=0
narRowCounter=0
narFile='2018.csv'
objNar=[]

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
	        self.occurredDate = occurredDate
	        self.occurredTime = occurredTime


	def display(self): #Object Methods
	    print("code: "+str(self.code)+", office: "+str(self.office)+", occurredDate: "+str(self.occurredDate)+", occurredTime: "+str(self.occurredTime)+", appearDate: "+str(self.appearDate)+", appearTime: "+str(self.appearTime))


	def addAppearTimeDate(self,appearDate,appearTime):
		if self.appearDate == None:
			self.appearDate=appearDate
		if self.appearTime == None:
			self.appearTime=appearTime
			#mytime = dt.datetime.strptime(appearTime,'%H%M%S').time()
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
	    	if row[17]=='Site Down' and row[14]=='Power':
	    		os.system('cls')
		        #print(row)
		        #print(row[17])
		       	#print(row[0],row[1],row[17], row[14])
		        print(str(narRowCounter)+"row fetched out of: "+str(total_row_count_nar))
		        objNar.append(Site(row[1],row[3],row[8],row[9]))
		if narRowCounter>100:
		    break



# s1 = Site('DHK_X4283','Gazipur','8/28/2018','2:37:31 PM')
# #s1.addAppearTimeDate('8/30/2018',time.asctime( time.localtime(time.time()) ));
# s1.addAppearTimeDate('8/30/2018','2:37:31 PM')
# print(s1.office)
# s1.display()

# objNar.append(Site('DHK_X4283','Gazipur','8/28/2018','2:37:31 PM'))
# objNar.append(Site('raj_X4283','Gazipur','8/28/2018','2:37:31 PM'))

for obj in objNar:
    print (obj.code,obj.office,obj.occurredDate,obj.occurredTime)