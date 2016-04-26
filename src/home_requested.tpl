<html>
<head>
<style type="text/css">


#info_equipement_ville{
padding-left : 10px;
border : 1px;
}


</style>
</head>
<body>
  <form action="/" method="post">
    Ville: <select name="town">
      <option value="empty">Selectionner un sport ou laisser vide pour tout avoir</option>
      % for option in list_town:
           <option value={{option[0]}}>{{option[0]}}</option>
      %end

    </select>
      Sport: <select name="sport">
        <option value="empty">Selectionner une ville ou laisser vide pour tout avoir</option>
        % for option in list_activities:
             <option value={{option[0]}}>{{option[0]}}</option>
        %end

      </select>
      <input value="Rechercher" type="submit" />

%if len(datas) > 0:
    <table id="info_equipement_ville" >
        <thead>
            <tr>
                <td>Adresse</td>
                <td>Ville</td>
                <td>Nom complexe</td>
                <td>Equipement</td>
            </tr>
        </thead>

        <tbody>
        % for item in datas:
             <tr>
                <td>{{item[1]}}</td>
                <td>{{item[2]}}</td>
                <td><a href = "./{{item[0]}}">{{item[3]}}</a></td>
                <td>{{item[4]}}</td>
            </tr>
        %end
        </tbody>

        <tfoot>
            <tr>
                <td>Nom complexe</td>
                <td>Equipement</td>
            </tr>
        </tfoot>
%else:
    <h1>Aucunes donnees</h1>
%end
</body>
</html>
