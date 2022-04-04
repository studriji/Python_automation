import sqlite3

connect = sqlite3.connect("database.db")
cursor = connect.cursor()


#create table

query = """CREATE TABLE IF NOT EXISTS
PYTHON (TOPIC_ID INTEGER PRIMARY KEY,TOPIC_NAME TEXT)"""
cursor.execute(query)

#add values to database
add_query = """INSERT INTO python values(10,'automation'),
(20,'web scrapping')"""
cursor.execute(add_query)

#see the table results
result_query = """SELECT * FROM python"""
cursor.execute(result_query)
table_data = cursor.fetchall()
print(table_data)

#update
update_query = """UPDATE python
SET TOPIC_NAME = 'game development'
WHERE topic_id = 20"""
cursor.execute(update_query)

result_query = """SELECT * FROM python"""
cursor.execute(result_query)
table_data = cursor.fetchall()
print(table_data)

#Delete
delete_query = """DELETE FROM PYTHON
where topic_name = 'automation'"""
cursor.execute(delete_query)

result_query = """SELECT * FROM python"""
cursor.execute(result_query)
table_data = cursor.fetchall()
print(table_data)