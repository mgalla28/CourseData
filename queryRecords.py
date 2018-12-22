# Queries the database to get info on classes
# Michael Gallagher 12-20-18

from pymongo import MongoClient

con = MongoClient()
db = con.ClassRecords
col = db.Courses

start = input("What is the start of your free time? ")
end = input("When is the end? ")

x = col.find({})[0]
print(x)
