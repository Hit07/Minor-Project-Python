import pandas as pd
import sqlite3

df = pd.read_csv('movies.csv')
conn = sqlite3.connect('demo.db')
df.to_sql('top_netflix_shows', conn, if_exists='replace', index=False)
cur = conn.cursor()

# Q1: Delete rows with NULL values in RATING or VOTES columns
cur.execute('''
            DELETE FROM top_netflix_shows WHERE RATING IS NULL OR VOTES IS NULL
            ''')

# Q2: Count the number of rows in the table
cur.execute('''
            SELECT COUNT(*) FROM top_netflix_shows
            ''')

print(cur.fetchall())



# Q2
cur.execute('''
            SELECT COUNT(DISTINCT MOVIES) FROM top_netflix_shows;
            ''')
print(cur.fetchall())
#
# Q3
cur.execute('''
            SELECT COUNT(*) FROM top_netflix_shows WHERE GENRE LIKE '%Action%' AND GENRE LIKE '%Crime%';
            ''')
print(cur.fetchall())

# Q4
cur.execute('''
            SELECT MOVIES, AVG(STARS) AS avg_score
            FROM top_netflix_shows
            GROUP BY MOVIES
            ORDER BY avg_score DESC
            LIMIT 5;
            ''')
print(cur.fetchall())
#
# # Q5
# cur.execute('''
#             SELECT MAX(VOTES) AS max_votes, MIN(VOTES) AS min_votes
#             FROM top_netflix_shows
#             WHERE GENRE LIKE '%Comedy%';
#             ''')
# print(cur.fetchall())
conn.commit()  # Don't forget to commit the changes
conn.close()