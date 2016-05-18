<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <script src="/static/jquery.js"></script>
    <script src="/static/selector.js"></script>

<style type="text/css">


#info_equipement_ville{
padding-left : 10px;
border : 1px;
}


</style>
</head>
<body>
  <form action="/" method="post">
    Ville: <select id="town" name="town">
      <option value="empty">Selectionner un sport ou laisser vide pour tout avoir</option>
      % for option in list_town:
           <option value="{{option[0]}}">{{option[0]}}</option>
      %end

    </select>
      Sport: <select id="sport" name="sport">
        <option value="empty">Selectionner une ville ou laisser vide pour tout avoir</option>
        % for option in list_activities:
             <option value="{{option[0]}}">{{option[0]}}</option>
        %end

      </select>
      <input value="Rechercher" type="submit" />

%if len(datas) > 0:
    <table id="info_equipement_ville" >
        <thead>
            <tr>
                <th>Adresse</th>
                <th>Ville</th>
                <th>Nom complexe</th>
                <th>Equipement</th>
            </tr>
        </thead>

        <tbody>
        % for item in datas:
             <tr>
                <td>{{item[1]}}</td>
                <td>{{item[2]}}</td>
                <td><a href = "./detail/{{item[0]}}">{{item[3]}}</a></td>
                <td>{{item[4]}}</td>
            </tr>
        %end
        </tbody>

        <tfoot>
            <tr>
                <th>Adresse</th>
                <th>Ville</th>
                <th>Nom complexe</th>
                <th>Equipement</th>
            </tr>
        </tfoot>
%else:
    <h1>Aucunes donnees</h1>
%end
</body>
</html>
