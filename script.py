import csv
import time
import calendar
import datetime as dt

#class starts

class Site:
	backUp=0
	code=None
	office=None
	occurredTime=None
	occurredDate=None
	appearDate=None
	appearTime=None

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



# with open('NAR.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for row in readCSV:
#     	if row[17]=='Site Down':
# 	        print(row)
# 	        #print(row[17])
# 	        print(row[0],row[1],row[17],)


s1 = Site('DHK_X4283','Gazipur','8/28/2018','2:37:31 PM')
#s1.addAppearTimeDate('8/30/2018',time.asctime( time.localtime(time.time()) ));
s1.addAppearTimeDate('8/30/2018','2:37:31 PM');
print(s1.office)
s1.display()

