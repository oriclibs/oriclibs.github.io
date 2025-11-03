#<div class=""><div class="content-left">socketlib 2025.2
Socket management
=== "Readme"
    
    ## Documentation
    
    ## Repository
    
    ## Dependencies
    
    ## behavior
    
    Each calls to connect will allocate source port from 170 to 170 + $FF. Each time a connect is performed, source port = source port ++
    
    Because when we connect to same host, we are trying to connect to same source port from Orix and the remote computer won't accept a connexion from a source port when connection is still closing.
    

=== "Versions"
=== "Dependencies"
    inetlib 2024.4    ch395lib 2024.4
=== "Dependencies"

=== "Dependents"
</div>
<div class="content-right"><h1>Metadata</h1><br><b>Version :</b> 2025.2<br><br><b>Install:</b><br><br>Add the following bpm command in your project directory:<br><p class="encadre">bpm add socketlib@2025.2</p><br><b>Documentation :</b> https://orix-software.github.io/socketlib/api/<br><br><b>Repository : </b><br><br><b>Authors:</b> nobody@nobody.fr, 
</div>
</div>
