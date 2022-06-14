import config
import sqlite3
def dataConnect():
    conn = sqlite3.connect(config.dir+'data.db')
    c = conn.cursor()
    return conn, c
    
def add_m(link):
	conn, c = dataConnect()
	c.execute(f'INSERT INTO monitoring (link) VALUES(?)', [link])
	conn.commit()
	c.close()
	conn.close()

def get_m():
	conn, c = dataConnect()
	table = c.execute('SELECT * FROM monitoring').fetchall()
	c.close()
	conn.close()
	return table

def detele_monitoring(link):
	conn, c = dataConnect()
	c.execute(f"DELETE FROM monitoring WHERE link=='{link}'")
	conn.commit()
	c.close()
	conn.close()
