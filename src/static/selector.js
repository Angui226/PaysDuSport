$(function() {

  $("#town").change(function() {

    $.ajax({ /*une fois qu'une ville est selectionnÃ©e on lance une requete ajax pour recuperer les stations*/
               url: '/change',
               type: 'POST',
               data: {
                   "town": $("#town").val(),
               },
               success: function(data) {


               },
               error: function(resultat, statut, erreur) {
                   alert("erreur");
               },
           });

  });


});
