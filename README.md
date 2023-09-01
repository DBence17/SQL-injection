# SQL-injection

## DOWNLOADS

The postgreSQL database should be already installed and run locally.
Additionally you will need the postgres app or psql commandline client.

Postgres app: https://postgresapp.com

Also install the psycopg2 python module with the command: 
```bash
pip install psycopg2-binary
pip install random_username
```

## CREATE THE DATABASE

### GUI on Mac
Open up the postgres app and you will see 3 databases there by default.
Make sure the server is running, if not press the start button.
Click on any one of them.
It will navigate to an sql shell.

In the shell run the following command: 
```bash
CREATE DATABASE test;
```

If successful 'CREATE DATABASE' will appear in the shell after the command.

Then you can run 
```bash
\l
```
in the shell to see all the databases on your server, but that's only to check whether the creation didn't fail.
After you created the test database you can navigate inside it in the postgres app, however that's optional.

### Cli (on Ubuntu)
* Add the postgres user to your personal user group, to enable for the postgres user to see your files (checked out from github). We assume here, that your user and group name is 'dev'.
* Create the database as postgres user 

```bash
sudo usermod -a -G postgres dev
id postgres

sudo -u postgres -s <<EOF_SUDO
pip install psycopg2-binary
pip install random_username
echo "create database test; \l" | psql
EOF_SUDO
```

if successful, 'CREATE DATABASE' and the database list will appear in the shell.

## LAST STEP

Everything should work with the steps above, you only have to run 
```bash
chmod +x main.py
sudo -u postgres ./main.py
```