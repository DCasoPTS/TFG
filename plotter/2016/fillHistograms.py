""" -> FILL THE HISTOGRAMS <-

>> Command: 

   python fillHistograms.py --samples [SAMPLE] --variables variables.py --cuts cuts.py --outputFile output_[SAMPLENAME]

"""



import os
import ROOT
import argparse
from math import *


#################################################################################

def createHistogram(tree, key, variable, selection):

    histo = ROOT.TH1F(key, '', variable['binning'], variable['range'][0], variable['range'][1])
    histo.GetXaxis().SetTitle(variable['label'])
    histo.GetYaxis().SetTitle('Events')

    for event in tree:
        
        if not selection:
            continue

        value = eval(variable['name'])

#        w = eval('event.EventSplit_trainingWeight * event.specialMCWeigths * event.XSWeight * event.METFilter_MC * event.SFweight2l * event.PrefireWeight * event.Lepton_promptgenmatched[0] * event.Lepton_promptgenmatched[1]')
        w = eval('event.specialMCWeigths * event.XSWeight * event.METFilter_MC * event.SFweight2l * event.PrefireWeight * event.Lepton_promptgenmatched[0] * event.Lepton_promptgenmatched[1]')

        histo.Fill(value, w)

    return histo


#################################################################################
#################################################################################
#################################################################################


if __name__ == '__main__':

    ########## main code here
    parser = argparse.ArgumentParser(description = "Receive the parameters")
    parser.add_argument('--variables', action = 'store', type = str, dest = 'variables', help = 'Define the variables that are going to be plotted')
    parser.add_argument('--samples', action = 'store', type = str, dest = 'samples', help = 'Define the samples that are read')
    parser.add_argument('--cuts', action = 'store', type = str, dest = 'cuts', help = 'Define the cuts of the variables')
    parser.add_argument('--outputFile', action = 'store', type = str, dest = 'outputFile', help = 'Name of the output file')

    args = parser.parse_args()



    ########## Open the output

    # Create directory for the jobs files
    dirName = 'histos'
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    
    file_output = ROOT.TFile(dirName + '/histos_' +args.outputFile + '.root', 'RECREATE')


    ########## Fill the histograms

    variables = {}
    variableFile = open(args.variables, 'r')
    exec(variableFile)

    cuts = {}
    cutsFile = open(args.cuts, 'r')
    exec(cutsFile)

    # -> Loop over the variables

    tree = ROOT.TChain("Events", "")

    tree.Add(args.samples)

    for key, var in variables.iteritems():
        for keycut, cut in cuts.iteritems():

            if '2HDMa' in args.outputFile:
                h = createHistogram(tree, 'Signal' + args.outputFile.split('_')[10] + '_' + key + '_' + keycut, var, cuts[keycut])
            else:
                h = createHistogram(tree, args.outputFile.split('_')[0] + '_' + key + '_' + keycut, var, cuts[keycut])
            file_output.cd()
            h.Write()

    file_output.Close()

