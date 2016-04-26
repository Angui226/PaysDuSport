<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
</head>
    <script src="/static/jquery.js" type="text/javascript"></script>
    <script src="/static/installation_specifique.js" type="text/javascript"></script>
    <script src="https://rawgit.com/HPNeo/gmaps/master/gmaps.js"></script>
    <script src="http://maps.google.com/maps/api/js?sensor=true&.js"></script>
    <script>
        var latitude = {{specific_installation[0][2]}}
        var longitude = {{specific_installation[0][3]}}
    </script>
<body>

  <p>{{specific_installation[0][1]}}</p><br/><br/>
  
  <p>Commune : {{specific_installation[0][5]}}</p><br/>
  <p>Rue : {{specific_installation[0][6]}}</p><br/>
  <p>Code postal : {{specific_installation[0][4]}}</p><br/>  
  
    <div id="maps" style="height: 100%; position: relative; background-color: rgb(229, 227, 223); overflow: hidden;"></div>
  
  
  
</body>
</html>