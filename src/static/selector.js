$(function() {

  $("#town").change(function() {

    $.ajax({ /*une fois qu'une ville est selectionnÃ©e on lance une requete ajax pour recuperer les stations*/
               url: '/change',
               type: 'POST',
               data: {
                   "town": $("#town").val(),
               },
               success: function(data) {
                 $("#sport").empty();
                 $("#sport").append('<option value="empty">Selectionner une ville ou laisser vide pour tout avoir</option>')
                 $.each(data, function(i, item) {
                 $("#sport").append('<option value="'+item+'">'+item+'</option>')


                    })

               },
               error: function(resultat, statut, erreur) {
                   alert("erreur");
               },
           });

  });


});
