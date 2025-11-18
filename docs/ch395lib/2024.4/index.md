---
hide:
  - navigation
  - toc
---
#<div class=""><div class="content-left">ch395lib 2024.4
ch395 low hardware routines. Use socket lib for socket management under Orix
=== "Readme"
    
    ## Documentation
    
    https://orix-software.github.io/ch395lib/api/
    
    ## Repository
    
    ## Dependencies
    
    ca65 syntax
    
    If you set a mac address maybe will refuse to attribute a mac address
    
    ## Informations complémentaires sur le chip
    
    * Même quand le cable est déconnecté, il est possible de lire le buffer quand on a déjà récupéré de la data.
    * Quand le cable est débranché, l'ip est persistante dans la stack. En revanche, les serveurs DNS fournis par le dhcp smeblent être eux resettés quand le cable est débranché.
    * Quand on teste le cable, il est toujours déconnecté après l'initialisation de la stack. Il faut faire une boucle avec des compteurs sur le get_phy_status pour vraiment détecter si oui on non le cable est débranché
    * Il ne faut pas fermer une socket quand la connexion TCP est toujours en established. Il faut attendre le disconnect TCP (et bien tcp, et non pas le statut de la socket en SUCCESS) avant d'envoyer l'ordre de stop de la socket
    * Si le cable est branché, mais le ch395 n'est pas initialisé, jamais le cable apparaitra branché sur le ch395

=== "Versions"


=== "Dependencies"


=== "Dependents"
</div>
<div class="content-right"><h1>Metadata</h1><br><b>Version :</b> 2024.4<br><br><b>Install under Orix:</b><br><br>download tgz : <a href=http://repo.orix.oric.org/dists/2024.4/tgz/6502/ch395lib.tgz class=md-typeset>ch395lib.tgz v2024.4</a><br><i><br><br><b>Install as library (for development purposes)</b><br><br>Use the following bpm command in your project directory:<br><p class="encadre">bpm add ch395lib@2024.4</p><br><b>Documentation :</b> No documentation provided.<br><br><b>Repository : </b><br><br><b>Authors:</b> nobody@nobody.fr, <br><br><b>Minimum kernel version required : </b> No minimal kernel version provided.<br>
</div>
</div>
