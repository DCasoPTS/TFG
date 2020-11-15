""" File to especify the variables that are going to be plotted 

>> The structure should appear as follows:
We have a variable dict: variable = {}
variable['variable1_key'] = {'name' : 'name in the file or expression',
                             'range' : [0, 1],
                             'label' : 'label'}



>> NOTE: Expression syntax
Before each variable it is required to write event. such as
event.PV_vx - event.RefittedPV_vx


"""

variables['mll'] = {'name' : 'event.mll',
                    'range' : [12, 80],
                    'binning' : 40,
                    'label' : 'mll [GeV]'}

variables['ptll'] = {'name' : 'event.ptll',
                    'range' : [30, 300],
                    'binning' : 40,
                    'label' : 'ptll [GeV]'}

variables['puppimet'] = {'name' : 'event.PuppiMET_pt',
                    'range' : [20, 300],
                    'binning' : 40,
                    'label' : 'PuppiMET [GeV]'}

variables['mth'] = {'name' : 'event.mth',
                    'range' : [50, 400],
                    'binning' : 40,
                    'label' : 'mT(ll+PuppiMET) [GeV]'}

variables['mtw2'] = {'name' : 'event.mtw2',
                    'range' : [50, 300],
                    'binning' : 40,
                    'label' : 'mT(l2+PuppiMET) [GeV]'}


variables['drll'] = {'name' : 'event.drll',
                     'range' : [0, 2.5],
                     'binning' : 40,
                     'label' : 'dR(l1,l2)'}

variables['pt1'] = {'name' : 'event.Lepton_pt[0]',
                     'range' : [25, 250],
                     'binning' : 40,
                     'label' : 'ptl1 [GeV]'}


variables['pt2'] = {'name' : 'event.Lepton_pt[1]',
                     'range' : [20, 150],
                     'binning' : 40,
                     'label' : 'ptl2 [GeV]'}

