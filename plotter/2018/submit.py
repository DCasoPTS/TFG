import os
import shutil
import glob


for myfile in glob.glob("jobs/send_*sh"):

    subcom = 'sbatch -o logfile.log -e errfile.err --qos=gridui_medium --partition=cloudcms ' + myfile
    os.system(subcom)


 
 


                    


