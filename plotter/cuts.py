
_tmp = [
    'event.Lepton_pdgId[0]*event.Lepton_pdgId[1] == -11*13',
    'event.Lepton_pt[0]>25.',
    'event.Lepton_pt[1]>20.',
    '(event.nLepton==2 || event.Lepton_pt[2]<10.)',
    'event.mll>12.',
    'event.PuppiMET_pt > 20.',
    'event.mpmet > 20.',
    'event.ptll > 30.',
    'event.mth > 50.',
    'event.mll < 80.',
    'event.drll < 2.5',
    'event.nbjets == 0',

       ]


cuts['SignalRegion'] = ' && '.join(_tmp)


_tmp = [
    'event.EventSplit_trainingWeight',
    'event.specialMCWeigths',
    'event.XSWeight',
    'event.METFilter_MC',
    'event.SFweight2l',
    'event.PrefireWeight',
    'event.Lepton_promptgenmatched[0]',
    'event.Lepton_promptgenmatched[1]',

       ]


cuts['EventWeight'] = ' * '.join(_tmp)




