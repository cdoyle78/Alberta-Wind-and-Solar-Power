import os.path
import os

#asset codes for wind and solar power producing assets

asset_nw = ["ARD1","BUL1","BUL2","BSR1","BTR1","CR1",
"CRR1","CRR2","WHT1","HAL1","CRE3","TAB1","NEP1","KHW1","AKE1","OWF1","RIV1","GWW1","IEW1","IEW2","SCR2","SCR3","SCR4","BSC1"]

#file to store wind and solar power data

fout = open("renewablesMV.csv", 'w')

#AESO only allows metered volumes to be downloaded one month at a time. addfile() funtion 
#takes each months file, strips out the hourly data for solar and wind assets and appends
#data to renewablesMV.csv

def addfile(file):
    count = 0
    fhand = open(file)

    for line in fhand:
        line = line.strip('"\n')
        line = line.replace('"','')
        line = line.replace(':',',')
        data = line.split(',')
        if len(data) < 2:        #skip header rows
        	continue
        elif data[0] in ["Report Date", "Pool Participant ID"]:  #skip header rows
            continue
        elif len(data) <= 3:     #write date line into file
        	fout.write(str(data).replace('\'','').strip('[]'))
        	fout.write("\n")
        else:                    #identify wind and solar assets and write data to file
        	if data[2] in asset_nw or data[2] == "-":
        		fout.write(str(data[2:]).replace('\'','').strip('[]'))
        		fout.write("\n")
        		count +=1
        ##	break        

    fhand.close()

# blacksping() takes reneablesMV.csv file created in addfiles() and creates a new file
# for each asset with a single time series of hourly power generation.

def blackspring(file):
	count = 0
	
	for asset in asset_nw:
		fout = open("C:/Users/chris/OneDrive/Documents/Python/Alberta Power/AssetFiles/" + asset + ".csv", 'w')
		fout.write("Date," + asset) 			#write column header
		fout.write("\n")
		fhand = open(file)
		for line in fhand:
			line = line.strip('"\n')
			line = line.replace(':',',')
			data = line.split(',')
			if len(data) < 3:
				daymonth = data[0]
				year = data[1]
			else:
				if data[0] == asset:
					if len(data) > 25:       #removes extra hour at daylight savings (25 hour day)
						data.pop(3)     
					n = 0
					for item in data:
						if not item == asset:
							time = "0" + str(n)
							newline = str(daymonth).strip() + ' ' + str(year).strip('.').strip() + ' ' + time[-2:] + ',' + str(item)
							fout.write(newline)
							fout.write("\n")
							n += 1
		fout.write("\n")
		fout.close()
		fhand.close()
		count +=1

#iterate through csv files in C:/Users/chris/OneDrive/Documents/Python/Alberta Power/Alberta MV and iterate them 
#through addfile()		
	
directory_in_str = "C:/Users/chris/OneDrive/Documents/Python/Alberta Power/Alberta MV"
directory = os.fsencode(directory_in_str)
    
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".csv"):
		print(str(directory).strip('b').replace('\'','') + '/' + filename) 
		addfile(str(directory).strip('b').replace('\'','') + '/' + filename)
		continue
	else:
		continue

fout.close()

#run renewables MV through blackspring()

blackspring("renewablesMV.csv")