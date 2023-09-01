import connection
import resources

# !PLEASE ALWAYS PRESS ENTER AFTER EACH STATEMENT TO ADVANCE!

resources.display()

resources.login()


# You can comment out the lines below until the specified line, however that is optional, it only deletes the table
delete_table = "DROP TABLE users;"
connection.cursor.execute(delete_table)
connection.connection.commit()
# Until here

connection.connection.close()
connection.cursor.close()