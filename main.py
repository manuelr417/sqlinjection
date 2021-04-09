import psycopg2

pg_config = {
    'user' : 'manuel',
    'password' : 'manuel1',
    'dbname' : 'db1',
    'dbport' : 8083
}

connection_url = "dbname=%s user=%s password=%s port=%s host='localhost'" %(pg_config['dbname'], pg_config['user'],
                                                                  pg_config['password'], pg_config['dbport'])
conn = psycopg2.connect(connection_url)

print("Welcome to the users program.")
uname = input("Enter user name: ")
print("Value entered " + str(uname))
upasswd = input("Enter password: ")
print("Value entered " + str(upasswd))
#now build a query string - this is bad practice due to SQL Injection"
query = "select * from users where username = '%s' and password = '%s';" %(uname, upasswd)
print("Query: ", query)
# prepare a query
cur = conn.cursor()

cur.execute(query)
#iterate over the valuee
try:
    if cur.fetchone():
        print("Login successful")
    else:
        print("Wrong credentials. Login failed.")
except Exception as e:
    print("DB Error.")

