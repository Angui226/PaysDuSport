<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

  <!-- Optional theme -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

  <!-- Latest compiled and minified JavaScript -->
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
  <script src="/static/jquery.js"></script>
  <script src="/static/selector.js"></script>
<style type="text/css">


#info_equipement_ville{
padding-left : 10px;
border : 1px;
}


body{
  background-color: #FFFADC;
}


</style>
</head>
<body>
        <form action="/" method="post">
          Ville: <select id="town" class="form-control" name="town">
            <option value="empty">Selectionner un sport ou laisser vide pour tout avoir</option>
            % for option in list_town:
                 <option value="{{option[0]}}">{{option[0]}}</option>
            %end

          </select>
            Sport: <select id="sport" class="form-control" name="sport">
              <option value="empty">Selectionner une ville ou laisser vide pour tout avoir</option>
              % for option in list_activities:
                   <option value="{{option[0]}}">{{option[0]}}</option>
              %end

            </select>
            <input class="btn btn-primary" value="Rechercher" type="submit" />
        </form>

</body>
</html>
