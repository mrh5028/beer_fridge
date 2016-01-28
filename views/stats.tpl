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
	<link href="//cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.2/jquery-ui.css" rel="stylesheet"/>
	<!--CSS-END-->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
	<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
	<script src="//cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.2/jquery-ui.js"></script>
	<script src="/static/js/validator.js"></script>
	<script src="/static/js/styles.js"></script>

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
	      <a class="navbar-brand" href="/display">Beer Fridge</a>
	    </div>

	    <!-- Collect the nav links, forms, and other content for toggling -->
	    <div class="collapse navbar-collapse" id="main-nav">
	      <ul class="nav navbar-nav">
	        <li><a href="/display">View Beers</a></li>
	        <li><a href="/new">Add Beer</a></li>
	        <li><a href="/manage">Manage Beers</a></li>
			<li class="active"><a href="/stats">Stats<span class="sr-only">(current)</span></a></li>
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
		<h1>Total Beers: {{vessels}} vessels<h1>

		<h1>Total Volume: {{volume}} oz<h1>

	</div>
</body>
</body>