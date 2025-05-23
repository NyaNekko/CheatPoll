from pymongo import MongoClient
from CheatPollBot import DB_URL

mongo = MongoClient(DB_URL)

users = mongo['cheatpoll']['users']
groups = mongo['cheatpoll']['groups']

def already_db(user_id):
        user = users.find_one({"user_id" : str(user_id)})
        if not user:
            return False
        return True

def already_dbgc(chat_id):
        group = groups.find_one({"chat_id" : str(chat_id)})
        if not group:
            return False
        return True

def add_user(user_id):
    in_db = already_db(user_id)
    if in_db:
        return
    return users.insert_one({"user_id": str(user_id)}) 

def remove_user(user_id):
    in_db = already_db(user_id)
    if not in_db:
        return 
    return users.delete_one({"user_id": str(user_id)})
    
def add_group(chat_id):
    in_db = already_dbgc(chat_id)
    if in_db:
        return
    return groups.insert_one({"chat_id": str(chat_id)})

def all_users():
    user = users.find({})
    usrs = len(list(user))
    return usrs

def all_groups():
    group = groups.find({})
    grps = len(list(group))
    return grps

def all_users_ids():
    user_documents = users.find({}, {"user_id": 1, "_id": 0})
    user_ids = [user["user_id"] for user in user_documents]
    return user_ids


def all_groups_ids():
    chat_documents = groups.find({}, {"chat_id": 1, "_id": 0})
    chat_ids = [chat["chat_id"] for chat in chat_documents]
    return chat_ids
