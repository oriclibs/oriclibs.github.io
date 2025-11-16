---
hide:
  - navigation
  - toc
---
#<div class=""><div class="content-left">socketlib 2025.4
Socket management
=== "Readme"
    
    ## Documentation
    
    ## Repository
    
    ## Dependencies
    
    ## behavior
    
    Each calls to connect will allocate source port from 170 to 170 + $FF. Each time a connect is performed, source port = source port ++
    
    Because when we connect to same host, we are trying to connect to same source port from Orix and the remote computer won't accept a connexion from a source port when connection is still closing.
    

=== "Versions"

    !!! abstract "[socketlib : 2025.2](../2025.2)"

=== "Dependencies"

    !!! abstract "[inetlib 2024.4](../../inetlib/2024.4 )"
    !!! abstract "[ch395lib 2024.4](../../ch395lib/2024.4 )"

=== "Dependents"
</div>
<div class="content-right"><h1>Metadata</h1><br><b>Version :</b> 2025.4<br><br><b>Install under Orix:</b><br><br><br>download tgz : [http://repo.orix.oric.org/dists/2025.4/tgz/6502/socketlib.tgz](socketlib.tgz v2025.4)<br><i><br><br><b>Install as library (for development purposes)</b><br>Use the following bpm command in your project directory:<br><p class="encadre">bpm add socketlib@2025.4</p><br><b>Documentation :</b> [https://orix-software.github.io/socketlib/api/](https://orix-software.github.io/socketlib/api/)<br><br><b>Repository : </b>[https://github.com/orix-software/socketlib](https://github.com/orix-software/socketlib)<br><br><b>Authors:</b> Jede, <br><b>Minimum kernel version required : </b> 2025.2><br>
</div>
</div>
