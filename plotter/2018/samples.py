""" File to especify the samples that are going to be processed 

>> The structure should appear as follows:
We have a variable dict: samples = {}
samples['process'] = {'name' : 'name',
                      'files':['root file 1',
                               'root file 2',
                                ...] }

"""

# BACKGROUNDS

# samples['WWTo2L2Nu'] = {'name' : 'WWTo2L2Nu',
#                         'files' : ['/gpfs/projects/cms/data/LatinosSkims/nanoAOD/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__monoHSkim2016/*WWTo2L2Nu__part0*']}

samples['WWTo2L2Nu'] = {'name' : 'WWTo2L2Nu',
                        'files' : ['/gpfs/projects/cms/data/LatinosSkims/nanoAOD/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__monoHSkim2016/*WWTo2L2Nu__*']}

samples['TTTo2L2Nu'] = {'name' : 'TTTo2L2Nu',
                        'files' : ['/gpfs/projects/cms/data/LatinosSkims/nanoAOD/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__monoHSkim2016/*TTTo2L2Nu__*']}

samples['ggHToWWTo2L2Nu'] = {'name' : 'ggHToWWTo2L2Nu',
                             'files' : ['/gpfs/projects/cms/data/LatinosSkims/nanoAOD/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__monoHSkim2016/*GluGluHToWWTo2L2Nu_M125__*']}

# SIGNALS

samples['2HDMa_HWWTollnunu'] = {'name' : '2HDMa_HWWTollnunu',
                             'files' : ['/gpfs/projects/cms/data/LatinosSkims/nanoAOD/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__monoHSkim2016/*2HDMa_HWWTollnunu_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_*']}


