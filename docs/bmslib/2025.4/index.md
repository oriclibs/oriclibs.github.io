---
hide:
  - navigation
  - toc
---
#<div class=""><div class="content-left">bmslib 2025.4
banking management https://orix-software.github.io/bmslib/api/
=== "Readme"
    
    [Documentation](https://orix-software.github.io/bms/)
    
    Lib for bank uses
    
    manage only 1 bank
    
    16000 bytes max can be stored
    
    ## Provide
    
    ### C
    
    * void *bms_create(size_t length, unsigned char flags);
    * unsigned char bms_free(bms *bms);
    * unsigned int bms_seek(bms *bms, unsigned int offset, unsigned char whence);
    * unsigned int bms_read_write(bms *bms, unsigned int length, void *data, unsigned char mode);
    * unsigned char bms_error();
    * unsigned char bms_version();
    
    ### Usage in assembly language
    
    * bms_create
    * bms_free
    * bms_seek
    * bms_read_write
    * bms_error
    * bms_version
    
    ## Extras
    
    use [bpm](https://github.com/orix-software/bpm) to build
    
    ![Arrays](mkdocs/docs/imgs/arrays.png)

=== "Versions"


=== "Dependencies"

    !!! abstract "[orixsdk 2023.3](../../orixsdk/2023.3 )"

=== "Dependents"
</div>
<div class="content-right"><h1>Metadata</h1><br><b>Version :</b> 2025.4<br><br><b>Install under Orix:</b><br><br>download tgz : <a href=http://repo.orix.oric.org/dists/2025.4/tgz/6502/bmslib.tgz class=md-typeset color=#4051b5>bmslib.tgz v2025.4</a><br><i><br><br><b>Install as library (for development purposes)</b><br><br>Use the following bpm command in your project directory:<br><p class="encadre">bpm add bmslib@2025.4</p><br><b>Documentation :</b> <a href=https://orix-software.github.io/bmslib/ class=md-typeset color=#4051b5>https://orix-software.github.io/bmslib/</a><br><br><b>Repository : </b><a href=https://github.com/orix-software/bmslib class=md-typeset color=#4051b5>https://github.com/orix-software/bmslib</a><br><br><b>Authors:</b> jede, <br><br><b>Minimum kernel version required : </b> 2024.1<br>
</div>
</div>
