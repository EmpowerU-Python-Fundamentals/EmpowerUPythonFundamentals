import json

x = '{ "name":"Liubov", "age":25, "city":"Lviv"}'
user = json.loads(x)
print(type(user), user)
with open("lessons/lesson14/user.json") as file:
    user2 = json.load(file)
print(type(user2), user2)


from models import User, UserCRUD
manager = UserCRUD()
for i in range(5):
    manager.create("Ihor", f"rest_{i}@g,ail.com", i)

with open("lessons/lesson14/users.json", "w") as file:
    json.dump([user.to_dict() for user in manager.read_all()], file, indent=4)
s = json.dumps([user.to_dict() for user in manager.read_all()], indent=4)
print(s)
