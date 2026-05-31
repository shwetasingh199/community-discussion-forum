from database.mongodb import users

print(users.count_documents({}))