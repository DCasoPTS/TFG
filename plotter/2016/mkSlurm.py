import os, sys, stat
import ROOT as r
from array import array
import numpy as np
import glob

# python mkSlurm.py /gpfs/users/dcaso/CMSSW_11_1_0/src /gpfs/users/dcaso/TFG/plotter/2016/

templateSlurm = """#!/bin/bash
cd CMSSWRELEASE
eval `scramv1 runtime -sh`
cd WORKINGPATH
python fillHistograms.py --samples SAMPLE --variables variables.py --cuts cuts.py --outputFile OUTNAME
"""

########################## Main program #####################################
if __name__ == "__main__":

    cmsswRelease = sys.argv[1]
    workingpath = sys.argv[2]

    samples = {}
    sampleFile = open('samples.py', 'r')
    exec(sampleFile)

    # Create directory for the jobs files
    dirName = 'jobs'
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        
    for sample, obj in samples.iteritems():
        for files in samples[sample]['files']:
            for myfile in glob.glob(files):

                n = str(myfile)

                template = templateSlurm
                template = template.replace('CMSSWRELEASE', cmsswRelease)
                template = template.replace('WORKINGPATH', workingpath) 
                template = template.replace('SAMPLE', myfile)
                template = template.replace('OUTNAME', n[n.find('nanoLatino_')+len('nanoLatino_'):n.rfind('.root')])
                
                f = open('jobs/send_' + n[n.find('nanoLatino_')+len('nanoLatino_'):n.rfind('.root')] + '.sh', 'w')
                f.write(template)
                f.close()
                os.chmod('jobs/send_' + n[n.find('nanoLatino_')+len('nanoLatino_'):n.rfind('.root')] + '.sh', 0755)













     

