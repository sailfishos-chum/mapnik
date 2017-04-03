#!/bin/bash

set -e

VERSION=v3.0.13

wget https://github.com/mapnik/mapnik/releases/download/v3.0.13/mapnik-$VERSION.tar.bz2
tar xvf mapnik-$VERSION.tar.bz2

cd mapnik-$VERSION

# https://github.com/mapnik/mapnik/issues/3384
patch < ../mapnik.issue3384.patch
