TFG plotter
======================

# 0 - Set the environment

    cd CMSSW_11_1_0/src/

    SetEnv

    cmsenv

# 1 - 

Texto2

    codigo

    hola


# 2 - Merge the histograms

Merge the histograms for each process 
    
    hadd -f histos/WWTo2L2Nu.root histos/histos_WWTo2L2Nu__*
    hadd -f histos/TTTo2L2Nu.root histos/histos_TTTo2L2Nu__*
    hadd -f histos/ggHToWWTo2L2Nu.root histos/histos_GluGluHToWWTo2L2Nu_M125__*
    hadd -f histos/2HDMa_HWWTollnunu.root histos/histos_2HDMa_HWWTollnunu_*

Merge all the processes

    hadd -f histos/hadd.root histos/WWTo2L2Nu.root histos/TTTo2L2Nu.root histos/ggHToWWTo2L2Nu.root histos/2HDMa_HWWTollnunu.root