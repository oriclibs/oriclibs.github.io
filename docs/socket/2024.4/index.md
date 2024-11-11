#<div class="main-content"><div class="content-left"># socket
=== "Readme"
    
    ## Documentation
    
    ## Repository
    
    ## Dependencies
    
    ## behavior
    
    Each calls to connect will allocate source port from 170 to 170 + $FF. Each time a connect is performed, source port = source port ++
    
    Because when we connect to same host, we are trying to connect to same source port from Orix and the remote computer won't accept a connexion from a source port when connection is still closing.
    
=== "Dependencies"
    inet 2024.4    ch395 2024.4</div>
<div class="content-right"><h1>Metadata</h1>
8 days ago
v1.61.0
MIT OR Apache-2.0
272 KiB
Install
Run the following Cargo command in your project directory:
cargo add syn
Or add the following line to your Cargo.toml:
syn = "2.0.87"
Documentation
fixme
Repository
FIXME
Owners\FIXME
FIXME
Categories
FIXME
FIXME

</div>
</div>
