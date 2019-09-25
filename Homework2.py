
import pymysql

db = pymysql.connect("localhost","testuser","test123","TESTDB" )

cursor = db.cursor()

sql = "SELECT *
FROM film f
WHERE (title LIKE "zo%")
JOIN film_actor fa
ON f.film_id = fa.film_id
JOIN actor a
ON a.actor_id = fa.actor_id"

cursor.execute(sql)
results = cursor.fetchall()

print (f.title, f.description, a.first_name, a.last_name \
         (title, description, fname, lname ))

db.close()

