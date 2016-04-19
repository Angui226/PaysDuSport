%if len(datas) > 0:
    <table id="info_equiepemnt_ville">
        <thead>
            <tr>
                <td>Nom complexe</td>
                <td>Equipement</td>
            </tr>
        </thead>
            
        <tbody>
        % for item in datas:
            <tr>
                <td>{{item.nom}}</td>
                <td>{{item.LibelleActivite}}</td>
            </tr>
        %end
        </tbdoy>
        
        <tfoot>
            <tr>
                <td>Nom complexe</td>
                <td>Equipement</td>
            </tr>
        </tfoot>
%else:
    <h1>Aucunes donnees</h1>
%end
