import connection

# Main functions to be executed

def login():
    print(f'For the explained injection methods use either {injection_queries[0]} or {injection_queries[1]} as username!')
    _username = input('Username: ')
    _pwd = input('Password: ')
    selection_statement = "SELECT * FROM users WHERE username = '" + _username + "' AND password = '" + _pwd + "';" 
    try : 
        connection.cursor.execute(selection_statement)
        account = connection.cursor.fetchall()
        if account != []:
            print('Succesful login!')
        else: 
            print("Could not find user with the specified login info! Try again!")
            login()
            return
    except: print("Login error!")
    print('To try the methods again or in a different way type 1. Otherwise you will need to restart the whole tutorial to do so.')
    again_ = input('')
    if again_ == '1':
        login()
    
def display():
    for i in range(len(lines)):
        print(lines[i])
        input('')    


# Creating the data to display

injection_queries = ["admin'--","admin'OR'1'='1"]

method1 = [injection_queries[0],'anything']
method2 = [injection_queries[1],'anything']

standard_query = "SELECT * FROM table WHERE username = 'something' AND password = 'something';"
standard_query_fix1 = f"SELECT * FROM table WHERE username = '{method1[0]}' AND password = '{method1[1]}';"
standard_query_fix2 = f"SELECT * FROM table WHERE username = '{method2[0]}' AND password = '{method2[1]}';"

lines = [
    'Welcome to SQL injection tutorial!',
    'A lot of websites and applications use SQL queries to check whether the user with the given username and password exists in their database.',
    f'When you hit enter/log in a query similar to the the following gets executed: {standard_query}',
    '''The method with which the query gets executed is that first it evaluates the given input and on the condition that both the username and password exists 
and are in correlation, because of the \'AND\' keyword, it returns a \'true\' boolean value.''',
    'If the conditions return \'true\' you get logged in. Otherwise, in the event of \'false\' evaluation, the log in will fail.',
    '''The tricky part is if the website is vulnerable to SQL injection you can break out of the string 
and customize the query so that the conidtions return \'true\' and the log in process becomes successful.''',
    'Hackers can steal your user info using this technique.',
    f'To break out of the string you can give the following usernames: {injection_queries[0]} or {injection_queries[1]}.',
    'Note: In both cases the apostrophe after admin is required to break out of the string.',
    'The first case: ',
    'In any programming language you can leave comments in your code which will not get executed.',
    'Comments have a special syntax.',
    'In SQL everything after the \'--\' is treated as a comment therefore it gets ignored by the compiler.',
    f'By using this method the query which gets executed will look like this: {standard_query_fix1}',
    'So if everything after \'--\' is ignored, the only condition is that there needs to be someone with \'admin\' as username, which is quite common.',
    'Also you can pass anything instead of \'admin\', if that username exists.',
    'The second case: ',
    'By putting \'OR\' and an expression after that always evaluates to \'true\' in the query, you always achieve succesful log in.',
    'That is because of the precendance of the operators.',
    '\'AND\' preceeds \'OR\'.',
    'Thus SQL will first evaluate the \'AND\' condition which will, of course return \'false\' without the correct username and password.',
    'However, after \'AND\' comes the evaluation of the \'OR\' operator.',
    'If you pass something like \'1\'=\'1, which will always be true, after the \'OR\', the statement  will always return \'true\'.',
    f'The query will be: {standard_query_fix2}',
    'A lot of companies are vulnerable to SQL injection although it is a common technique and can be avoided easily.',
    'For example you can use prepared statements with preparameterized queries or escape user input before putting it in a query.',
    '''To conclude, SQL injection is a very dangerous, yet easily defendable threat.
SQL injection can be done with a myriad of other methods, which are usually much more complicated.''',
    'Now you can try these out!'
]
