#Create database for beer fridge

import sqlite3
con = sqlite3.connect('beers.db') # Warning: This file is created in the current directory
con.execute("CREATE TABLE beer (id INTEGER PRIMARY KEY, brewer char(100) NOT NULL, beer char(100) NOT NULL, style char(100) NOT NULL, abv real NOT NULL, size real NOT NULL, amount INT NOT NULL, vtype char(100) NOT NULL)")
con.execute("INSERT INTO beer (brewer, beer, style, abv, size, amount, vtype) VALUES ('Sam Adams','Boston Lager','Lager', 5.4, 12, 12, 'Bottle')")
con.execute("INSERT INTO beer (brewer, beer, style, abv, size, amount, vtype) VALUES ('Dogfish Head','60 Minute IPA', 'IPA', 6.0, 12, 6, 'Bottle')")
con.execute("INSERT INTO beer (brewer, beer, style, abv, size, amount, vtype) VALUES ('Goose Island','BCBS', 'Stout', 12.0, 12, 4, 'Bottle')")
con.commit()