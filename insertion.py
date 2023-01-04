#function who insert a element in a sql db
import sqlite3
def insert_element(table,element):
    con = sqlite3.connect('train.db')
    c = con.cursor()
    c.execute("INSERT INTO (?) VALUES (?)", (table,element))
    con.commit()
    con.close()