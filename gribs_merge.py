#!/usr/bin/env python

from datetime import datetime
import fnmatch
import os
from pathlib import Path
import subprocess

# the list of the meteorogical parameters 
param=['cc', 'clwc', 'lnsp', 'q', 't', 'u', 'v', 'w', 'z']

# directory with the initial grib files
initial_directory = '/home/kmnuser/Documents/Andrey/gh-137/gribs_additional'

# the command we will use from ecCodes
ecCodes_command = 'grib_copy'

def merge_grib():
    os.chdir(initial_directory)
    
    for params in param:
        # directory with the output grib files
        final_directory = '/home/kmnuser/Documents/Andrey/gh-137/gribs_additional/'+params+'.grib'

        # create a list with the ecCodes command as the first element,
        # so that you we then use this list as a bash command line in a python subprocess
        file_list = [ecCodes_command] 
                                    
        for files in os.listdir(initial_directory):
            if fnmatch.fnmatch(files, '*'+params+'.grib'):
                if os.path.isfile(os.path.join(initial_directory, files)):
                        # add grib files in the folder to the list
                        file_list.append(files) 
        
        # the final file
        grib_out = Path(final_directory)
        # create final file if not exist
        grib_out.touch(exist_ok=True)
        # add final file to the list,
        # so that you we then use this list as a bash command line in a python subprocess  
        file_list.append(grib_out)
        # the ecCodes command from the python list as the bash command in the subprocess 
        subprocess.call(file_list)

    final_directory_2 = '/home/kmnuser/Documents/Andrey/gh-137/gribs_additional/'

    # create tq_ml.grib and zlnsp_ml.grib and to use its in compute_geopotential_on_ml_00.py programm
    file_list = [ecCodes_command, 't.grib', 'q.grib', final_directory_2+'tq_ml.grib'] 
    subprocess.call(file_list)

    file_list = [ecCodes_command, 'z.grib', 'lnsp.grib', final_directory_2+'zlnsp_ml.grib']
    subprocess.call(file_list)
    subprocess.call(['python3', '/home/kmnuser/Documents/Andrey/gh-137/compute_geopotential_on_ml_00.py',
                    initial_directory+'/zlnsp_ml.grib', initial_directory+'/tq_ml.grib', '-o',
                    initial_directory+'/z_out.grib', '-l', 'all', '-d', initial_directory])

def remove_files():
    os.chdir(initial_directory)
    for files in os.listdir(initial_directory):
        if os.path.isfile(files):
            print('Deleting file:', files)
            os.remove(files)

    
if __name__ == '__main__':
    merge_grib()
    remove_files()
