#!/usr/bin/env python

from datetime import datetime
import fnmatch
import os
from pathlib import Path
import subprocess

def merge_grib():
    current_date=datetime.now().strftime('%Y%m%d')
    # directory with the initial grib files
    initial_directory = '/home/kmnuser/Documents/Andrey/gh-137/gribs_additional'
    # directory with the output grib file
    final_directory = '/home/kmnuser/Documents/Andrey/gh-137/gribs_out/'+current_date+'_ecmwf_europe_modellevel.grib'

    # the command we will use from ecCodes
    ecCodes_command = 'grib_copy'
    # create a list with the ecCodes command as the first element
    file_list = [ecCodes_command]
    os.chdir(initial_directory)
    FILES=['z_out_scale.grib', 'cc.grib', 'clwc.grib', 'q.grib', 't.grib', 'u.grib', 'v.grib', 'w.grib'] # files that we will merge

    for file in FILES:
        file_list.append(file) 

    # final file
    grib_out = Path(final_directory)
    # create final file if not exist
    grib_out.touch(exist_ok=True)
    # add final file to the list,
    # so that you we then use this list as a bash command line in a python subprocess
    file_list.append(grib_out)
    
    subprocess.call(file_list)
    os.chdir('/home/kmnuser/Documents/Andrey/gh-137')

def move_to_smartmet():
    subprocess.call(['sh', 'move_to_smartmet.sh'])

   
if __name__ == '__main__':
    merge_grib()
    move_to_smartmet()
