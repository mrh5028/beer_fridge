<p>The available beers are:</p>
<table border="1">
%for row in rows:
    <tr>
    <!-- Here you grab the beer's ID that you'll use later -->
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

