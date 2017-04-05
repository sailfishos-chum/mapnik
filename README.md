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

Due to the bug in SDK, for i486 target, you have to install libraries that are not recognized as 
shared libraries by SDK separately from sb2 after they are installed via mb2/sb2:

```
[mersdk@SailfishSDK ~]$ sb2 -t SailfishOS-i486 ldd /usr/lib/libboost_regex.so.1.51.0
        not a dynamic executable
[...]
[mersdk@SailfishSDK ~]$ sudo zypper in boost-regex
[mersdk@SailfishSDK ~]$ sb2 -t SailfishOS-i486 ldd /usr/lib/libboost_regex.so.1.51.0
        linux-gate.so.1 =>  (0x6f758000)
        libsb2.so.1 => /usr/lib/libsb2/libsb2.so.1 (0x6f5fb000)
        libicuuc.so.52 => /usr/lib/libicuuc.so.52 (0x6f48b000)
        libicui18n.so.52 => /usr/lib/libicui18n.so.52 (0x6f282000)
        libicudata.so.52 => /usr/lib/libicudata.so.52 (0x6dc16000)
        libstdc++.so.6 => /usr/lib/libstdc++.so.6 (0x6db2e000)
        libm.so.6 => /lib/libm.so.6 (0x6dae6000)
        libgcc_s.so.1 => /lib/libgcc_s.so.1 (0x6dacd000)
        libc.so.6 => /lib/libc.so.6 (0x6d907000)
        libdl.so.2 => /lib/libdl.so.2 (0x6d902000)
        libpthread.so.0 => /lib/libpthread.so.0 (0x6d8e6000)
        /lib/ld-linux.so.2 (0x6f759000)
[...]
```

Libraries that were affected by the bug: boost-regex, harfbuzz, boost-program-options, libtiff, and libjpeg-turbo 
