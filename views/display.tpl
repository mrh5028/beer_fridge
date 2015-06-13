<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<title>Beer Fridge</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta name="description" content="" />
	<meta name="author" content="" />

	<!--CSS-START-->
	<link href="/static/css/bootstrap.css" rel="stylesheet" />
	<link href="/static/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
	<!--CSS-END-->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
	<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>


</head>
<body>

	<nav class="navbar navbar-default">
	  <div class="container-fluid">
	    <!-- Brand and toggle get grouped for better mobile display -->
	    <div class="navbar-header">
	      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#main-nav">
	        <span class="sr-only">Toggle navigation</span>
	        <span class="icon-bar"></span>
	        <span class="icon-bar"></span>
	        <span class="icon-bar"></span>
	      </button>
	      <a class="navbar-brand" href="#">Beer Fridge</a>
	    </div>

	    <!-- Collect the nav links, forms, and other content for toggling -->
	    <div class="collapse navbar-collapse" id="main-nav">
	      <ul class="nav navbar-nav">
	        <li class="active"><a href="/display">View Beers<span class="sr-only">(current)</span></a></li>
	        <li><a href="/new">Add Beer</a></li>
	      </ul>
	      <form class="navbar-form navbar-left" role="search">
	        <div class="form-group">
	          <input type="text" class="form-control" placeholder="Search">
	        </div>
	        <button type="submit" class="btn btn-default">Submit</button>
	      </form>
	    </div><!-- /.navbar-collapse -->
	  </div><!-- /.container-fluid -->
	</nav>

<div class="container-fluid">	
		
<h2>The available beers are:</h2>
<table class="table table-striped">
	<tr>
		<td><h4>ID</h4></td>
		<td><h4>Brewery</h4></td>
		<td><h4>Name</h4></td>
		<td><h4>Amount</h4></td>
		<td><h4>Info</h4></td>
		<td><h4>Add</h4></td>
		<td><h4>Subtract</h4></td>
%for row in rows:
    <tr>
    <!-- Grab beer id-->
    %p_id = row[0] 
    %for col in row:
        <td>{{col}}</td>
    %end
        <form action="/display" method="POST">
            <!-- input type hidden, and value is the ID of the beer -->
            <input type = "hidden" name ="beer_id" value= "{{p_id}}">
			<td><button type ="submit" name="info" class="btn btn-success"><span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span></button></td>
            <td><button type ="submit" name="add" class="btn btn-primary"><span class="glyphicon glyphicon-plus" aria-hidden="true"></span></button></td>
            <td><button type ="submit" name="sub" class="btn btn-primary"><span class="glyphicon glyphicon-minus" aria-hidden="true"></span></button></td>
        </form>
    </tr>
%end
</table>
</div>
</body>
</html>

