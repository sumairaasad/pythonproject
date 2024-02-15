from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://sumairaasad12:@cluster0.uy7anfw.mongodb.net/")
 
#sample_training is the mongodb database
mongoDB = client['leisurecenter']#   client.leisurecenter
 
#members is the mongodb collection
mongoColl = mongoDB['members']   #mongoDB.members  #['members']
 
#use the find one method to retrieve a single document from the members collection
docs = mongoColl.find()
for aDoc in docs:
    pprint(aDoc)
#print(aDoc)
    
print("\nAll documents\n")
#use the find method to retrieve all documents from the members collection
docs = mongoColl.find()
for aDoc in docs:
    pprint(aDoc)
    # print(aDoc)
#     print("\nMethod 2\n\n")
 # "Method 2"
dbMongoClient = client["leisurecenter"]['lessons']
coll = dbMongoClient.find_one({'CourseID':11})
pprint(coll)
print("\Looping through multiple documents\n")
coll = dbMongoClient.find()
for aDoc in coll:
    pprint(aDoc)
 
# print("\Insert multiple documents\n")
addDoc = dbMongoClient.insert_one({"CourseID": 50,"MemberID": 1900})
print(addDoc.inserted_id)

print("\Insert Single document\n")
documents = [
{'CourseID': 290, 'MemberID': 190 },
{'CourseID': 230, 'MemberID': 220},
{'CourseID': 270, 'MemberID': 282},
{'CourseID': 1000, 'MemberID': 201}
]
 
# addDocs = dbMongoClient.insert_many(documents)
# print(addDocs.inserted_ids)
       
print("\nUpdate document\n")
updateDoc = dbMongoClient.update_one({'CourseID': 4}, {'$set':{"MemberID":4000}})
print(updateDoc.modified_count)
    
# print("\nUpdate Multiple documents\n")
# updateDocs = dbMongoClient.update_many({'MemberID': 14}, {'$set':{"CourseID":2111}})
# print(f"The number of updated documents: {updateDocs.modified_count}")

# print("\nDelete single document\n")
# deleteOne = dbMongoClient.delete_one({'CourseID': 270})
# print(f"Deleted {deleteOne.deleted_count} document")
 
# print("\nDelete Multiple documents\n")
# deletemany = dbMongoClient.delete_many({'MemberID': 14})
# print(f"Deleted {deletemany.deleted_count} document")














