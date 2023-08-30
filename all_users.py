import random
import string
from random_username.generate import generate_username

# Creating the random password function
characters = string.ascii_letters + string.digits 
# + string.punctuation

def get_random_password(length):
    password = ''.join(random.choice(characters) for i in range(length))
    return password
        
# Creating the users for the database     
users = {}
if users.get("admin") == None:
    users["admin"] = "samplepw"

for i in range(50):
    usr = generate_username()[0]
    if users.get(usr) == None:
        users[usr] = get_random_password(random.randint(8,40))
