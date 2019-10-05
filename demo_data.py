import sqlite3

conn = sqlite3.connect(r'C:\Users\anika\Desktop\AnikaDS\Unit_3_Lambda\DS-Unit-3-Sprint-2-SQL-and-Databases\Sprint Challenge\demo_data.db')
cursor = conn.cursor()
#cursor.execute("CREATE TABLE demo([s] text, [x] integer, [y] integer)")


list = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]
# cursor.executemany("INSERT INTO demo VALUES (?, ?, ?)", list)
# conn.commit()

'''Count how many rows you have'''
q1 = cursor.execute("SELECT COUNT(*) FROM demo").fetchall()

'''How many rows are there where both x and y are at least 5?'''
q2 = cursor.execute("SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5").fetchall()

'''How many unique values of y are there?'''
q3 = cursor.execute("SELECT DISTINCT COUNT(*) y FROM demo").fetchall()

'''Output: 3, 2, 3'''

if __name__ == '__main__':
    print(q1, q2, q3)
