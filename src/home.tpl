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
          Ville: <select name="ville">
            <option value="vide">Selectionner un sport ou laisser vide pour tout avoir</option>
            % for option in list_town:
                 <option value={{option[0]}}>{{option[0]}}</option>
            %end

          </select>
            Sport: <select name="sport">
              <option value="vide">Selectionner une ville ou laisser vide pour tout avoir</option>
              % for option in list_activities:
                   <option value={{option[0]}}>{{option[0]}}</option>
              %end

            </select>
            <input value="Rechercher" type="submit" />
        </form>

</body>
</html>
