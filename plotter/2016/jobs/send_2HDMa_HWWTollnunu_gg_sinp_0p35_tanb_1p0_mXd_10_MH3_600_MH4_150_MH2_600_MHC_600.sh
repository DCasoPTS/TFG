#!/bin/bash
cd /gpfs/users/dcaso/CMSSW_11_1_0/src
eval `scramv1 runtime -sh`
cd /gpfs/users/dcaso/TFG/plotter
python fillHistograms.py --samples /gpfs/projects/cms/data/LatinosSkims/nanoAOD/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__monoHSkim2016/nanoLatino_2HDMa_HWWTollnunu_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600.root --variables variables.py --cuts cuts.py --outputFile 2HDMa_HWWTollnunu_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600
