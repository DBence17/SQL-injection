# SQL-injection

DOWNLOADS

The database runs on a local postgres server.
For it to work you need to have postgreSQL and the postgres app. 
Postgres app: https://postgresapp.com
Also install the psycopg2 python module with the command: pip install psycopg2-binary

CREATE THE DATABASE

Open up the postgres app and you will see 3 databases there by default.
Make sure the server is running, if not press the start button.
Click on any one of them.
It will navigate to an sql shell.
In the shell run the following command: CREATE DATABASE test;
If successful 'CREATE DATABASE' will appear in the sell after the command
Then you can run \l in the shell to see all the databases on your server, but that's only to check whether the creation didn't fail.
After you created the test database you can navigate inside it in the postgres app, however that's optional.


LAST STEP

Everything should work with the steps above, you only have to run main.py