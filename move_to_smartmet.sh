#!/bin/bash

data=$(date +%Y%m%d);
gribs_out='gribs_out'
file_name=$data'_ecmwf_europe_modellevel.grib'
smartmet_in='/mnt/disk_S/data/incoming/Andrey_incoming'

cp $gribs_out/$file_name $smartmet_in/$file_name
