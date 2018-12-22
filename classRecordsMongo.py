# Creates a MongoDB of classes that I might take and their schedule information
# Michael Gallagher 12-4-18
from pymongo import MongoClient
from subprocess import call


def takeData():
    con = MongoClient()
    db = con.ClassRecords
    courseCollection = db.Courses
    check = True
    while (check):
        name = input("Please input course name - ")
        days = input("Please input course days - ")
        startTime = input("Please input course start time - ")
        endTime = input("Please input course end time - ")
        location = input("Please input course location - ")

        x = [name, days, startTime, endTime, location] #provides feedback so you can see entry mistakes
        print("You have inserted ")
        print(x)

        courseCollection.insert_one({"name": name,
                                     "days": days,
                                     "start time": startTime,
                                     "end time": endTime,
                                     "location": location})

        inputCheck: str = input("Do you have more to add y/n? ")
        if inputCheck == 'n':
            check = False
    call(['net stop MongoDB'])

def main():
    takeData()


if __name__ == '__main__':
    main()