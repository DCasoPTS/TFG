""" -> FILL THE HISTOGRAMS <-

>> Command: 

   python fillHistograms.py --samples [SAMPLE] --variables variables.py --cuts cuts.py --outputFile output_[SAMPLENAME]

"""



import os
import ROOT
import argparse
from math import *


#################################################################################

def createHistogram(tree, key, variable, selection, ev_weight):

    histo = ROOT.TH1F(key, '', 60, variable['range'][0], variable['range'][1])
    histo.GetXaxis().SetTitle(variable['label'])
    histo.GetYaxis().SetTitle('Events')

    for event in tree:
        
        if not selection:
            continue

        value = eval(variable['name'])
        w = eval(ev_weight)

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
        
        h = createHistogram(tree, args.outputFile.split('__')[0] + '_' + key, var, cuts['SignalRegion'], cuts['EventWeight'])
        file_output.cd()
        h.Write()

    file_output.Close()

