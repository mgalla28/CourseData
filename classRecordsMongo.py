#Creates a csv of classes that I might take and their schedule information
#Michael Gallagher 12-4-18
from pymongo import MongoClient

con = MongoClient()
db = con.ClassRecords
courseCollection = db.Courses
check = True
while(check):
    name = input("Please input course name - ")
    days = input("Please input course days - ")
    time = input("Please input course time - ")
    location = input("Please input course location - ")

    x = [name,days,time,location]
    print(x)
    

    courseCollection.insert_one({"name": name,
                                 "days": days,
                                 "time" : time,
                                 "location": location})


    inputCheck = input("Do you have more to add y/n? ")
    if( inputCheck == 'n'):
        check = False
        
