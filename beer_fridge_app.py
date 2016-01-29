import sqlite3
from bottle import Bottle, route, run, debug, template, request, static_file, error, post, redirect, get
import os
import time
import statgen

app = Bottle()

#Static Routes
@app.route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

#Main App
#Main page and display 
@app.route('/')
@app.route('/display', method=['GET', 'POST'])
def display():
	conn = sqlite3.connect('beers.db') #connect
	c = conn.cursor()
	c.execute("SELECT id, brewer, beer, amount FROM beer WHERE amount > 0;") #only want beers we have
	result = c.fetchall()
	c.close()
	
	add = request.POST.get('add') #grab add value
	sub = request.POST.get('sub') #grab subtract value
	info = request.POST.get('info') #grab info value
	b_id = request.POST.get('beer_id') #get beer id
	
	if add is not None: #if add was clicked
		conn = sqlite3.connect('beers.db') #connect
		c = conn.cursor()
		c.execute("UPDATE beer SET amount = amount + 1 WHERE id = ?;", (b_id,)) #add a beer
		conn.commit() #commit the chage
		c.close()
		
		redirect("/display") #refresh the page
	
	elif sub is not None: #if subtract was clicked
		conn = sqlite3.connect('beers.db') #connect
		c = conn.cursor()
		c.execute("UPDATE beer SET amount = amount - 1 WHERE id = ?;", (b_id,)) #remove a beer
		conn.commit()
		c.close()
		
		redirect("/display") #refresh the page

	elif info is not None: #if info button was clicked
		redirect("/info/%s" %b_id)

	else:
		output = template('display', rows=result) #otherwise just display
		return output

#Info for one beer
@app.route('/info/<b_id>', method='GET')
def info(b_id):
	conn = sqlite3.connect('beers.db') #connect
	c = conn.cursor()
	c.execute("SELECT id, brewer, beer, style, abv, size, amount, vtype FROM beer WHERE id = ?;", (b_id,)) #only want info for one beer
	result = c.fetchall()
	c.close()

	output = template('info', rows=result)
	return output
	
#Add new beer
@app.route('/new', method='GET')
def new_beer():
	if request.GET.get('save', '').strip():
		new_brewer = request.GET.get('brewer').strip()
		new_beer = request.GET.get('beer').strip()
		new_style = request.GET.get('style').strip()
		new_abv = request.GET.get('abv').strip()
		new_size = request.GET.get('size').strip()
		new_amount = request.GET.get('amount').strip()
		new_vtype = request.GET.get('vtype').strip()
		
		conn = sqlite3.connect('beers.db')
		c = conn.cursor()
		c.execute("INSERT INTO beer (brewer, beer, style, abv, size, amount, vtype)VALUES (?,?,?,?,?,?,?)", (new_brewer, new_beer, new_style, new_abv, new_size, new_amount, new_vtype))
		new_id = c.lastrowid
		conn.commit()
		c.close()
		
		return ' <META http-equiv="refresh" content="2;URL=/new"> <p>The new beer was inserted into the database, the ID is %s</p>' % new_id

	else:
		return template('new_beer.tpl')

#Manage
@app.route('/manage', method=['GET', 'POST'])
def manage():
		conn = sqlite3.connect('beers.db') #connect
		c = conn.cursor()
		c.execute("SELECT id, brewer, beer, style, abv, size, amount, vtype FROM beer;") #get all beers
		result = c.fetchall()
		c.close()
		
		del_beer = request.POST.get('del_beer') #grab delete value
		b_id = request.POST.get('beer_id') #get beer id
		
		if del_beer is not None: #if delete was clicked
			conn = sqlite3.connect('beers.db') #connect
			c = conn.cursor()
			c.execute("DELETE from beer WHERE id = ?;", (b_id,)) #delete beer
			conn.commit() #commit the chage
			c.close()
			
			redirect("/manage") #refresh the page
			
		else:
			output = template('manage', rows=result)
			return output
		

#Stats Page
@app.route('/stats', method=['GET', 'Post'])
def stats():
	volume = statgen.total_volume()
	vessels = statgen.total_vessel()
	
	output = template('stats', volume=volume, vessels=vessels)
	return output
		
run(app, host='0.0.0.0', port=8080, debug=True)