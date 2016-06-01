<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />

  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <link href="../static/specific_installation.css" rel="stylesheet" type="text/css">
    <script src="/static/jquery.js"></script>
    <script src="/static/selector.js"></script>

<style type="text/css">


#info_equipement_ville{
padding-left : 10px;
border : 1px;
}

.right_nav{
     margin-top : 8px !important;
}
</style>
</head>
<body>

<!-- NavBar -->
<nav class="navbar navbar-default">
        <div class="container-fluid">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="../"><span id="titre">Pays du sport</span></a>
          </div>

          <div id="navbar" class="navbar-collapse collapse">
          <form  action="/" method="post">

              <!-- <li class="active"><a href="#">Accueil</a></li> -->

              <span class="col-md-1 navbar-right right_nav";""><input class="btn btn-primary" value="Rechercher" type="submit" /></span>

              <span class="col-md-3 navbar-right right_nav">
                    <table><tr><td>Sport:</td><td><select id="sport" class="form-control" name="sport">
               <option value="empty">Selectionner une ville ou laisser vide pour tout avoir</option>
               % for option in list_activities:
                    <option value="{{option[0]}}">{{option[0]}}</option>
               %end
               </select></td></tr></table></span>

              <span class="col-md-3 navbar-right right_nav">
               <table><tr><td>Ville:</td><td><select id="town" class="form-control" name="town">
               <option value="empty">Selectionner un sport ou laisser vide pour tout avoir</option>
               % for option in list_town:
                    <option value="{{option[0]}}">{{option[0]}}</option>
               %end
               </select></td></tr></table></span>

            </form>

            <!--<ul class="nav navbar-nav navbar-right">
              <li class="active"><a href="./">Default <span class="sr-only">(current)</span></a></li>
            </ul>-->
          </div><!--/.nav-collapse -->
        </div><!--/.container-fluid -->
      </nav>
<!-- Fin NavBar -->


%if len(datas) > 0:
    <table class="table" id="info_equipement_ville" >
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
