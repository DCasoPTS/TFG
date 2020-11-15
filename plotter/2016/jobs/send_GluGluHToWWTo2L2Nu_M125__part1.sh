#!/bin/bash
cd /gpfs/users/dcaso/CMSSW_11_1_0/src
eval `scramv1 runtime -sh`
cd /gpfs/users/dcaso/TFG/plotter
python fillHistograms.py --samples /gpfs/projects/cms/data/LatinosSkims/nanoAOD/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__monoHSkim2016/nanoLatino_GluGluHToWWTo2L2Nu_M125__part1.root --variables variables.py --cuts cuts.py --outputFile GluGluHToWWTo2L2Nu_M125__part1