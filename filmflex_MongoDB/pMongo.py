from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://sumairaasad12:@cluster0.uy7anfw.mongodb.net/")

#sample_training is the mongodb database
mongoDB = client['leisurecenter']#   client.leisurecenter
 
#leisurecenter is is the mongodb collection
mongoColl = mongoDB['members']   #mongoDB.members  #['members']
docs = mongoColl.find_one()
pprint(docs)
print("\nAll documents\n")
#use find method to retrieve all documents from the members collection
docs =mongoColl.find()
for aDoc in docs:
    pprint(aDoc)

print("\nMethod 2\n")
dbMongoClient = client["leisurecenter"]['lessons'] 
# coll = dbMongoClient.find_one({'CourseID':42})
# pprint(coll)

print("\nLooping through multiple documents\n") 
# coll = dbMongoClient.find()
# for aDoc in coll:
#     pprint(aDoc)

print("\n Inser single doc\n")
# addDoc =dbMongoClient.insert_one({"LessonID": 340,"CourseID": 110,
#   "MemberID": 190})
# pprint(addDoc.inserted_id)

print("\n Insert multiple documents\n")
documents = [ 
    {'CourseID':133, 'MemberID':110},
    {'CourseID':210, 'MemberID':110},
    {'CourseID':212, 'MemberID':102}]
addDocs = dbMongoClient.insert_many(documents)
print(addDocs.inserted_ids)
    
    #client.close() #close the connection

print ("\nupdate single document\n")
updateDoc = dbMongoClient.update_one({'CourseID':212,},{'$set':{"MembersID":2500}})
print(updateDoc.modified_count)

print ("\nupdate multiple documents\n")
updateDoc = dbMongoClient.update_many({'MemberID':19,},{'$set':{'CourseID':211}})
print(f"The number of update documents:{updateDoc.modified_count}")

print("\nDelete single document\n")
# deleteOne = dbMongoClient.delete_one({'CourseID': 270})
# print(f"Deleted {deleteOne.deleted_count} document")

print("\nDelete Multiple document\n")
# print("\nDelete Multiple documents\n")
# deletemany = dbMongoClient.delete_many({'MemberID': 14})
# print(f"Deleted {deletemany.deleted_count} document")
