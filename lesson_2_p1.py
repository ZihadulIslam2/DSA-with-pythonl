# class User:
#     def __init__(self,username, name, email):
#         self.username = username
#         self.name = name 
#         self.email = email

# class user_database: 
#     def __init__(self):
#         self.users = []
    
#     def insert (self,User):
#         i = 0
#         while i < len(self.users):
#             if self.users[i].username > user.username:
#                 break
#         i += 1
#         self.users.insert(i,User)
        
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

class UserDatabase: 
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        # Find the correct position to insert the new user
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        # Insert the user at the found position
        self.users.insert(i, user)
        
    def display_users(self):
        for user in self.users:
            print(f"Username: {user.username}, Name: {user.name}, Email: {user.email}")

# Create an instance of UserDatabase
user_db = UserDatabase()

# Insert some user data
user_db.insert(User("alice", "Alice Johnson", "alice@example.com"))
user_db.insert(User("bob", "Bob Smith", "bob@example.com"))
user_db.insert(User("charlie", "Charlie Brown", "charlie@example.com"))

# Display the users in the database
user_db.display_users()