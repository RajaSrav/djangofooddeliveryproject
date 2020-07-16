import sqlite3

# connected to the sqlite3
# db = mysqul.container.content()
db = sqlite3.connect('Registration')
# Created cursor from database registration
rs = db.cursor()
# created table name register and number is varchar
# rs.execute('''create table Register(name varchar(50), email varchar(100), passwd varchar(10))''')
# db.commit()
# add data in table
rs.execute(''' insert into Register values('Raja','@gmail.com','raja1234#')''')
db.commit()
rs.execute('select * from Register')
for i in rs:
    print(i)
