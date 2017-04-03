# pkg-mapnik
RPM packaging of Mapnik for Sailfish

## Howto build

* Clone this repository

* cd into it and run `./download.sh`

* cd into source directory

* build by running 
```
export SFARCH=armv7hl; mb2 -t SailfishOS-$SFARCH -s ../rpm/mapnik.spec build
```
in MER SDK. 

* RPMs are under RPMS directory.

Please let me know if there are some errors (missing dependencies, for
example) during building by opening an issue for this repository.

At present, beginning of Apr 2017, its impossible to build Mapnik for 
i486 target (possibly bugs in SDK).
