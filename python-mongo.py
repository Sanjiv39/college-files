# 1. install mongo
# 2. install python
# 3. install pip curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python get-pip.py
# 4. Open Cmd
# 5. C:\Users\SCMS\AppData\Local
# . python -m pip install pymongo
# . check by pip freeze
# 6. Open idle
# 7. import pymongo
# 8. Open file save into folder

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
print("db connected")
mycol = mydb["test1"]
print("collection connected")

#inserted
mydict = { "name": "Sunita", "age": 60 }
x = mycol.insert_one(mydict)
print("inserted")

#updated
myquery = { "name": "Sunita" }
newvalues = { "$set": { "age": 100 } }
mycol.update_many(myquery, newvalues)
print("updated")

#deleted
myquery = { "name": "Sunita" }
mycol.delete_many(myquery)
print("deleted")

#Select data
for x in mycol.find():
    print(x)