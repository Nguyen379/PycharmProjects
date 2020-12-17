import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()
# method such as CREATE, INSERT, SELECT are capitalized for readability
# even if uncapitalized they still work
# execute only
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")

''' Long way
c.execute("INSERT INTO employees VALUES ('Corey', 'Schafer', 5000)")
c.execute("INSERT INTO employees VALUES ('Nguyen', 'Le', 1000)")
c.execute("INSERT INTO employees VALUES ('kaboom', 'hi', 10000)")
'''

'Short way'
name_list = [('Corey', 'Schafer', 5000), ('Nguyen', 'Le', 1000), ('kaboom', 'hi', 10000)]
c.executemany("INSERT INTO employees VALUES(?,?,?)", name_list)


# In order to print out a value, you need to select it first
t = ('Nguyen',)
# use tuple since string operations are prone to errors
c.execute("SELECT * FROM employees where first=?", t)
# ? is where you want to place, where to specify what value to take
print(c.fetchone())

c.execute("SELECT * FROM employees")
print(c.fetchall())


conn.commit()

conn.close()
