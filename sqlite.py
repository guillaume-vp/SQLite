import sqlite3
con = sqlite3.connect('CTmovies.db')

cur = con.cursor()

#Retrieve all records
cur.execute("SELECT * FROM Movie")
con.commit()
print(cur.fetchall())

#Retrieve records for a single movie
cur.execute("SELECT * FROM Movie WHERE id = 1;")
con.commit()
print(cur.fetchall())

#Update a single record
cur.execute("UPDATE Movie SET releaseYear=2002 where id=1;")
cur.execute("SELECT * FROM Movie WHERE id = 1;")
con.commit()
print(cur.fetchall())

#Update 20 records
cur.execute("UPDATE Movie SET releaseYear=releaseYear+1 WHERE id<=20;")
cur.execute("SELECT * FROM Movie")
con.commit()
print(cur.fetchall()) 

#Delete 10 records
cur.execute("DELETE FROM Movie WHERE id<=10;")
cur.execute("SELECT * FROM Movie;")
con.commit()
print(cur.fetchall())

con.close()