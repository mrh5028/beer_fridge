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
	
def total_vessel_type():
	conn = sqlite3.connect('beers.db') #connect
	c = conn.cursor()
	c.execute("SELECT amount, vtype FROM beer WHERE amount > 0;") #only want beers we have
	result = c.fetchall()
	c.close()
	t_bottle = 0
	t_can = 0
	
	for item in result:
		if item[1] == "Bottle": #find total bottles
			t_bottle = t_bottle + item[0]
	
		else: #rest is cans
			t_can = t_can +item[0]
	
	return (t_bottle, t_can) #return
	
