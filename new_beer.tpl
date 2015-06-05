%#template for the form for a new task
<p>Add a new task to the beer list:</p>
<form action="/new" method="GET">
<input type="text" size="100" maxlength="100" name="brewer">
<input type="text" size="100" maxlength="100" name="beer">
<input type="text" size="100" maxlength="100" name="amount">
<input type="submit" name="save" value="save">
</form>