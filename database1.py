import sqlite3

def patient():
    conn = sqlite3.connect("meditract.db")
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS patients
    (id INTEGER Primary Key,
    name TEXT,
    age INTEGER,
    gender TEXT,
    disease TEXT);""")

    conn.commit()
    conn.close()

def addPatients(name,age,gender,disease):
    conn =sqlite3.connect("meditract.db")
    cur =conn.cursor()
    cur.execute("""INSERT INTO 
    patients (name,age,gender,disease)
    VALUES (?,?,?,?)""",
    (name,age,gender,disease))

    conn.commit()
    conn.close()

def getPatients():
    conn = sqlite3.connect("meditract.db")
    cur = conn.cursor()
    cur.execute("SELECT *FROM  patients")
    rows = cur.fetchall()
    conn.close()
    return rows

def searchPatients(name):
    conn =sqlite3.connect("meditract.db")
    cur =conn.cursor()
    cur.execute("Select *From patients Where name = ?",(name,))
    row =cur.fetchone()
    conn.close()
    return row

def updateDetails(name,new_age,new_disease):
    conn =sqlite3.connect("meditract.db")
    curr =conn.cursor()
    curr.execute("Update patients Set age =?,disease =? Where name =?",(new_age,new_disease,name))
    conn.commit()
    conn.close()