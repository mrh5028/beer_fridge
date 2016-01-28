import sqlite3
import os
import time

def total_vessel():
	conn = sqlite3.connect('beers.db') #connect
	c = conn.cursor()
	c.execute("SELECT amount FROM beer WHERE amount > 0;") #only want beers we have
	result = c.fetchall()
	c.close()
	
	t_vessel = sum([pair[0] for pair in result])

	return t_vessel


def total_volume():
	conn = sqlite3.connect('beers.db') #connect
	c = conn.cursor()
	c.execute("SELECT amount, size FROM beer WHERE amount > 0;") #only want beers we have
	result = c.fetchall()
	c.close()
	
	t_volume = sum(tuple(a*b for a, b in result))
	return t_volume