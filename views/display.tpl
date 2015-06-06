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

<div class="container-fluid">	
<h2>The available beers are:</h2>
<table class="table table-striped">
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
            <td><input type ="submit" name="Add" value="Add"></td>
            <td><input type ="submit" name="Sub" value="Subtract"></td>
        </form>
    </tr>
%end
</table>
</div>
</body>
</html>

