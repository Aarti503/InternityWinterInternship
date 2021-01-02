import pymongo

from bson import ObjectId
#to conncet with the localhost
connection = pymongo.MongoClient('localhost',27017)
#create your databse
database = connection['myDatabase']
print("Collection Created..")
#create your collection
collection = database['myCollection']
print("Database Connected..")

def insert_data(data):
    document = collection.insert_one(data)
    return document.inserted_id

def update_or_create(document_id, data):
    # TO AVOID DUPLICATES - THIS WILL CREATE NEW DOCUMENT IF SAME ID NOT EXIST
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data}, upsert=True)
    return document.acknowledged

def get_single_data(document_id):
    data = collection.find_one({'_id': ObjectId(document_id)})
    return data

def get_multiple_data():
    data = collection.find()
    return list(data)

def update_existing(document_id, data):
    #Update existing document data by document ID
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data})
    return document.acknowledged


def remove_data(document_id):
    document = collection.delete_one({'_id': ObjectId(document_id)})
    return document.acknowledged


# CLOSE DATABASE
connection.close()

data = {'Name':"Siya",'Gender':"Female",'Location':"Delhi"}
data2 = {'Name':"Aman",'Gender':"Male",'Location':"Chennai"}
data3 = {'Name':"Samar",'Gender':"Male",'Location':"Mumbai"}
data4 = {'Name':"Mehak",'Gender':"FeMale",'Location':"Manali"}
# #add data to your collection
# insert_data(data)
# insert_data(data2)
# insert_data(data3)

data_retrieved = get_single_data("5fefe1ffeb44f9822e6f1fc2")
print("Single data",data_retrieved)
# updated_data = update_or_create("5fefe1ffeb44f9822e6f1fc2",data4)
# print("Updated data:",updated_data)
multiple_data = get_multiple_data()
print("List of data is retreived",multiple_data)
data_removed = remove_data("5fefe1ffeb44f9822e6f1fc2")
print("Data is removed",data_removed)