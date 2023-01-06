#function who insert a element in a sql db
import sqlite3
def insert_element(table,key,element):
    if type(element) == str:
        element = element
    elif type(element) == list:
        element = ",".join(element)
    else :
        element = str(element)
    con = sqlite3.connect('train.db')
    c = con.cursor()
    c.execute("INSERT INTO ? (?) VALUES (?)", (table,key,element))
    con.commit()
    con.close()