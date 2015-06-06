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
	<link href="/static/css/bootstrap-responsive.css" rel="stylesheet" type="text/css"/>
	<!--CSS-END-->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
	<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>


</head>
<body>

<p>Add a new beer to the beer list:</p>
<form action="/new" method="GET">
Brewer <input type="text" size="25" maxlength="100" name="brewer"><br>
Beer <input type="text" size="25" maxlength="100" name="beer"><br>
Amount <input type="text" size="25" maxlength="100" name="amount"><br>
<input type="submit" name="save" value="save">
</form>