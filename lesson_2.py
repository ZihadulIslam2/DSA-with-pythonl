# Lesson 2 - Binary Search Trees, Traversals and Recursion
# rootforce method


# Define the User class
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

# Define the user_database class
class user_database:
    def __init__(self):
        self.users = []

    # Insert users in sorted order based on username
    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    # Find user by username
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None  # Return None if the user isn't found

    # Update a user's information
    def update(self, user):
        target = self.find(user.username)
        if target:  # Only update if the user exists
            target.name, target.email = user.name, user.email

    # List all users
    def list_all(self):
        return self.users


# Create user instances
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
tusher = User('Tusher', 'Zihadul Islam Tusher', 'tusher@gmail.com')

# Instantiate the user database
database = user_database()

# Insert users into the database
database.insert(aakash)
database.insert(biraj)
database.insert(hemanth)
database.insert(jadhesh)
database.insert(siddhant)
database.insert(sonaksh)
database.insert(vishal)
database.insert(tusher)

# Find a user
found_user = database.find('Tusher')
if found_user:
    print(f"Found: Username: {found_user.username}, Name: {found_user.name}, Email: {found_user.email}")
else:
    print("User not found!")

# Update a user's information
database.update(User(username='siddhant', name='Siddhant ', email='siddhantu@example.com'))

# List all users in the database
for user in database.list_all():
    print(f"Username: {user.username}, Name: {user.name}, Email: {user.email}")
