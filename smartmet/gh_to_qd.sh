#!/bin/bash
CNF=/smartmet/run/data/ecmwf/cnf
CURRENTTIME=$(date +"%Y%m%d")
OUT_PATH=/smartmet/data/ecmwf/europe/modellevel_new/querydata
IN_PATH=/smartmet/data/incoming/Andrey_incoming
FILENAME=${CURRENTTIME}_ecmwf_europe_modellevel

gribtoqd -H 472 -t -c $CNF/ecmwf.cnf -o $OUT_PATH/${FILENAME}.sqd $IN_PATH/${FILENAME}.grib
#rm $IN_PATH/${FILENAME}
