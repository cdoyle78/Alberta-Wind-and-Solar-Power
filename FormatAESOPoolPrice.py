#AESO power price data can only be downloaded 2 years at a time.
#Also comes in a 1-24 hour date time format. 0-23 is needed for Pandas.
#This script changes the hours to 0-23 by subtracting 1 hour form each entry
#and consolidates the fixed data to newfile.csv

#note download files in one year increments and save as
#"PP0.csv,PP1.csv,PP2.csv" etc. 


import os.path

fout = open("PoolPricesAll.csv", 'w')
fout.write("Date, Price, 30Ravg, Demand") #write column headers
fout.write("\n")
    
#function to parse each csv line, extract the hour and subract one,
#then write the revised entry to newfile.csv

def addfile(file):
    count = 0
    fhand = open(file)
    

    for line in fhand:
        line = line.strip('"\n')
        line = line.replace('"','')
        data = line.split(',')
        if len(data) > 3:
            rest = data[1:4]
            date = data[0].split()
            if len(date[1]) == 2:
                date[1] = int(date[1]) - 1
                newdate = date[0] + " " + str(date[1])
                newline = [newdate] + rest[0:3]
                newline = str(newline).replace('\'','').strip('[]')
                fout.write(str(newline).strip('[]',))
                fout.write("\n")
                count +=1
                
    fhand.close()

#cycle through PP files in directory and add them
#to newfile.csv with addfile() funtion. 

cwd = os.getcwd()
for i in range(22):

    filepath = ''.join(['C:/Users/chris/OneDrive/Documents/Python/Alberta Power/Pool Prices','\\PP',str(i),'.csv'])
    
    if os.path.isfile(filepath) == True:
        print(filepath)
        addfile(filepath)
    else:
        print("File does not exist!")


fout.close()

    
