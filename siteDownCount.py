import csv
import os


narFiles=[]
netCodes=[]
counts=[]
narRowCounter=0

narFiles.append('2018.csv')


for narFile in narFiles:

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
			        if row[1] in netCodes:
			        	arrIndex=netCodes.index(row[1])
			        	counts[arrIndex]+=1
			        else:
			        	netCodes.append(row[1])
			        	counts.append(1)

i=0
with open('site_down_count.csv', 'wb') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    	wr.writerow(["site","counts"])
    	while i<len(netCodes):
	    	print(netCodes[i])
	    	print(counts[i])
	    	wr.writerow([str(netCodes[i]),str(counts[i])]) 
	    	i=i+1