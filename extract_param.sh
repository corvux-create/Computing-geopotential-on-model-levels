#!/bin/bash

cd /home/kmnuser/Documents/Andrey/gh-137

dir='gribs'
dir_additional='gribs_additional'

source gh_env/bin/activate

wget -q -nd -nH -N -c -R $dir -P gribs ftp://ecmwf-lv:siaMet-1019@meteoftp.lvgm$

LEVELIST="all"

if [ "$(ls -A $dir/)" ]; then # check if the folder is not empty to avoid errors
    for files in $dir/*; do
        filename=$(basename -- "$files") # file name without path
        grib_filter -o $dir_additional/$filename-[shortName].grib - $files <<EO$
        write;
EOF
    done
fi

rm -rf $dir/* # delete files in the directory

cmnd="python3 gribs_merge.py"
echo $cmnd
eval $cmnd
