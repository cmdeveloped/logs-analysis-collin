import psycopg2

DBNAME="news"

db = psycopg2.connect(database=DBNAME)
c = db.cursor()
query1 = ("SELECT title, count(*) as views FROM articles a, log l WHERE a.slug = substring(l.path, 10) GROUP BY title ORDER BY views DESC LIMIT 3;")
c.execute(query1)
rows = c.fetchall()

print "\n 1. What are the most popular three articles of all time?"
print "Show me the data for #1! \n"
for row in rows:
    print " ", row[0], "-", row[1], "views"
db.close()

db = psycopg2.connect(database=DBNAME)
c = db.cursor()
query2 = ("SELECT au.name, sum(v.views) as views FROM article_views v JOIN articles a on v.title = a.title JOIN authors au on a.author = au.id GROUP BY au.name ORDER BY sum(v.views) DESC;")
c.execute(query2)
rows = c.fetchall()

print "\n 2. Who are the most popular article authors of all time?"
print "Show me the data for #2! \n"
for row in rows:
    print " ", row[0], "-", row[1], "views"
db.close()

db = psycopg2.connect(database=DBNAME)
c = db.cursor()
query3 = ("SELECT to_char(a.date, 'Mon DD, YYYY'), round( cast(a.percent as numeric), 3) FROM percent_error a;")
c.execute(query3)
rows = c.fetchall()

print "\n 3. On which days did more than 1% of requests lead to errors?"
print "Show me the data for #3! \n"
for row in rows:
    print " ", row[0], "-", row[1], "%"
db.close()
