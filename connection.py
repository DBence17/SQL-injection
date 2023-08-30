import psycopg2
import all_users 

# Connecting to database

try:
    connection = psycopg2.connect("dbname=test user=postgres")
except: print('Unable to connect to database')

cursor = connection.cursor()

# Creating the users table
try: 
    cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id SERIAL, username VARCHAR( 50 ) UNIQUE NOT NULL, password VARCHAR( 50 ) UNIQUE NOT NULL);")
except:
    print('Can\'t create table')

# Feeding the table input data
admin_query="INSERT INTO users (username, password) SELECT 'admin', 'samplepw' WHERE NOT EXISTS ( SELECT username FROM users WHERE username = 'admin');"
cursor.execute(admin_query)
for i in range(1,len(all_users.users)):
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s) ON CONFLICT DO NOTHING",
    (list(all_users.users.keys())[i], list(all_users.users.values())[i]))
    
connection.commit()
