import sqlite3

# Connect to your SQLite database file
conn = sqlite3.connect('here_example.db') #connect the file
conn.row_factory = sqlite3.Row # to use column name
cursor = conn.cursor() # component to send query
cursor.execute('''
SELECT count(*) AS no_english
FROM song_details
WHERE language <> 'English'
''')
# Execute a query
results = cursor.fetchall()
list_result = [tuple(row) for row in results]
for row in list_result:
    print(row)

cursor.execute('''
SELECT count(*)
FROM eurovision_winners
WHERE country = host_country
''')
results2 = cursor.fetchall()
list_result2 = [tuple(row) for row in results2]
for row in list_result2:
    print(row)
# Close the connection
conn.close()
