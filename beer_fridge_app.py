import sqlite3
from bottle import Bottle, route, run, debug, template, request, static_file, error, post, redirect

app = Bottle()

@app.route('/')
@app.route('/display', method=['GET', 'POST'])
def display():
	conn = sqlite3.connect('beers.db') #connect
	c = conn.cursor()
	c.execute("SELECT id, brewer, beer, amount FROM beer WHERE amount > 0;") #only want beers we have
	result = c.fetchall()
	c.close()
	
	add = request.POST.get('Add') #grab add value
	sub = request.POST.get('Sub') #grab subtract value
	b_id = request.POST.get('beer_id') #get beer id
	
	if add is not None: #if add was clicked
		conn = sqlite3.connect('beers.db') #connect
		c = conn.cursor()
		c.execute("UPDATE beer SET amount = amount + 1 WHERE id = ?;", (b_id)) #add a beer
		conn.commit() #commit the chage
		c.close()
		
		redirect("/display") #refresh the page
	
	elif sub is not None: #if subtract was clicked
		conn = sqlite3.connect('beers.db') #connect
		c = conn.cursor()
		c.execute("UPDATE beer SET amount = amount - 1 WHERE id = ?;", (b_id)) #remove a beer
		conn.commit()
		c.close()
		
		redirect("/display") #refresh the page

	else:
		output = template('display', rows=result) #otherwise just display
		return output

@app.route('/new', method='GET')
def new_beer():
	
	if request.GET.get('save', '').strip():
		new_brewer = request.GET.get('brewer').strip()
		new_beer = request.GET.get('beer').strip()
		new_amount = request.GET.get('amount').strip()
		conn = sqlite3.connect('beers.db')
		c = conn.cursor()
		
		c.execute("INSERT INTO beer (brewer,beer,amount) VALUES (?,?,?)", (new_brewer, new_beer, new_amount))
		new_id = c.lastrowid
		conn.commit()
		c.close()
		
		return '<p>The new beer was inserted into the database, the ID is %s</p>' % new_id
		
	else:
		return template('new_beer.tpl')
		
run(app, host='localhost', port=8080)