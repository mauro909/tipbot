import sqlite3
import config

conn = sqlite3.connect(config.database_name)
db = conn.cursor()
data = db.execute("SELECT * FROM users").fetchall()
data = db.execute("SELECT * FROM depositRequests").fetchall()
data = db.execute("SELECT * FROM withdrawRequests").fetchall()
data = db.execute("SELECT * FROM usedAddresses").fetchall()
input("")
