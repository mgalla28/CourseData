#Creates a csv of classes that I might take and their schedule information
#Michael Gallagher 12-3-18
import csv



csvfile =  open('classTimes.csv','a')

classWriter = csv.writer(csvfile)


courseList = []
check = True
while(check):
    name = input("Please input course name - ")
    days = input("Please input course days - ")
    time = input("Please input course time - ")
    location = input("Please input course location - ")

    x = [name,days,time,location]
    print(x)
    
    classWriter.writerow(x)

    inputCheck = input("Do you have more to add y/n? ")
    if( inputCheck == 'n'):
        check = False
        

csvfile.close()
