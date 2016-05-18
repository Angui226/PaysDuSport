<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
</head>
    
    <link href="../static/specific_installation.css" rel="stylesheet" type="text/css">
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    
    <script src="/static/jquery.js" type="text/javascript"></script>
    <script src="/static/installation_specifique.js" type="text/javascript"></script>
    <script src="https://rawgit.com/HPNeo/gmaps/master/gmaps.js"></script>
    <script src="http://maps.google.com/maps/api/js?sensor=true&.js"></script>
    <script>
        var latitude = {{specific_installation[0][2]}}
        var longitude = {{specific_installation[0][3]}}
    </script>
<body>
<!-- NavBar -->
<nav class="navbar navbar-inverse navbar-default">
        <div class="container-fluid">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">Pays du sport</a>
          </div>
          
          <div id="navbar" class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
              <!-- <li class="active"><a href="#">Accueil</a></li> -->
            </ul>
            
            <!--<ul class="nav navbar-nav navbar-right">
              <li class="active"><a href="./">Default <span class="sr-only">(current)</span></a></li>
            </ul>-->
          </div><!--/.nav-collapse -->
        </div><!--/.container-fluid -->
      </nav>
<!-- Fin NavBar -->

<ul class="list-group" style ="width : 35%">
  <li class="list-group-item">Equipement : {{specific_installation[0][1]}}</li>
  <li class="list-group-item">Commune : {{specific_installation[0][5]}}</li>
  <li class="list-group-item">Rue : {{specific_installation[0][6]}}</li>
  <li class="list-group-item">Code postal : {{specific_installation[0][4]}}</li>
</ul>
  
    <div id="maps" style="height: 100%; position: relative; background-color: rgb(229, 227, 223); overflow: hidden;"></div>
  
  
  
</body>
</html>