import sqlite3
con = sqlite3.connect('beers.db') # Warning: This file is created in the current directory
con.execute("CREATE TABLE beer (id INTEGER PRIMARY KEY, brewer char(100) NOT NULL, beer char(100) NOT NULL, amount INT NOT NULL)")
con.execute("INSERT INTO beer (brewer,beer,amount) VALUES ('Sam Adams','Boston Lager',12)")
con.execute("INSERT INTO beer (brewer,beer,amount) VALUES ('Dogfish Head','60 Minute IPA',6)")
con.execute("INSERT INTO beer (brewer,beer,amount) VALUES ('Goose Island','BCBS',6)")
con.commit()