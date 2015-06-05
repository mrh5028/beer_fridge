%#template for the form for a new beer
<p>Add a new beer to the beer list:</p>
<form action="/new" method="GET">
Brewer <input type="text" size="25" maxlength="100" name="brewer"><br>
Beer <input type="text" size="25" maxlength="100" name="beer"><br>
Amount <input type="text" size="25" maxlength="100" name="amount"><br>
<input type="submit" name="save" value="save">
</form>