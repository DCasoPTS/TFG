import ROOT
import argparse

# python plotHistograms.py --inputFile histos/hadd.root --outputDir plots --norm norm1

#################################################################################

def tuneHistogram(histo, color, var, isSignal):
    
    if isSignal:
#        histo.SetFillColorAlpha(color, 0.3)
        histo.SetLineColor(color)
        histo.SetLineWidth(3)
        histo.GetXaxis().SetLabelSize(0.03)
        histo.GetYaxis().SetLabelSize(0.03)
        histo.GetXaxis().SetTitleSize(0.037)
        histo.GetYaxis().SetTitleSize(0.037)
        histo.GetXaxis().SetTitleOffset(1.27)
        histo.GetYaxis().SetTitleOffset(1.4)
        histo.GetXaxis().SetTitle(var)
    else:
        histo.SetFillColorAlpha(color, 0.8)
        histo.SetLineColor(color)
        histo.GetXaxis().SetLabelSize(0.03)
        histo.GetYaxis().SetLabelSize(0.03)
        histo.GetXaxis().SetTitleSize(0.037)
        histo.GetYaxis().SetTitleSize(0.037)
        histo.GetXaxis().SetTitleOffset(1.27)
        histo.GetYaxis().SetTitleOffset(1.4)
        histo.GetXaxis().SetTitle(var)
 

#################################################################################
#################################################################################
#################################################################################


if __name__ == '__main__':

    ########## main code here
    parser = argparse.ArgumentParser(description = "Receive the parameters")
    parser.add_argument('--inputFile', action = 'store', type = str, dest = 'inputFile', help = 'Input ROOT file with the data')
    parser.add_argument('--outputDir', action = 'store', type = str, dest = 'outputDir', default = '', help = 'Name of the output dir')
    parser.add_argument('--log', action = 'store_true', dest = 'log', help = 'Linear orllogaritmic scale in Y axis')
    parser.add_argument('--norm', action = 'store', type = str, dest = 'norm', default = 'norm0', help = 'Normalization Option')
    args = parser.parse_args()


    ########## Open the tree

    file_input = ROOT.TFile(args.inputFile)

    samples = []
    myvars = []
    cuts = []

    ## List of samples, variables and cuts:
    for key in file_input.GetListOfKeys():
    
        h = key.ReadObj()
        histo_name = str(h.GetName())
        histo_name = histo_name.split('_', 2)
        if histo_name[0] not in samples: samples.append(histo_name[0])
        if histo_name[1] not in myvars: myvars.append(histo_name[1]) 
        if histo_name[2] not in cuts: cuts.append(histo_name[2]) 


    ########## Load the colors
    colors = {}
    exec(open('colors.py', 'r'))

    ########## Load the variables
    variables = {}
    exec(open('variables.py', 'r'))

    ########## Plot the histograms

    c1 = ROOT.TCanvas('c1', '', 500, 500)
    c1.SetTicks(1,1)
    ROOT.gStyle.SetOptStat(0)
    ROOT.TGaxis.SetMaxDigits(4)
    prefix = '' # default

    for var in myvars:
        for cut in cuts:
            ## Y axis scale options

            if (args.log): 
                prefix = 'log_'
                c1.SetLogy(1)
            else:
                prefix = 'lin_'
                c1.SetLogy(0)


            ## Legend construction

            leg = ROOT.TLegend(0.54, 0.89 - len(samples)*0.04, 0.89, 0.89)
            leg.SetTextSize(0.03)
            leg.SetBorderSize(0)

            c = 0
            ## Overlap representation implementation
            
            stack = ROOT.THStack()

            for sam in samples:
                if not 'Signal' in sam:
                    h = file_input.Get(sam + '_' + var + '_' + cut)
                    tuneHistogram(h, colors[sam], variables[var]['label'], 0)
                    stack.Add(h)

                    if (args.norm == 'norm1'):
                        h.Scale(0.33333333/h.Integral())

                    if (args.log): 
                        h.SetMaximum(10.*h.GetMaximum())
                    else: h.SetMaximum(1.2*h.GetMaximum())

                    leg.AddEntry(h, sam, 'f')

                    
            stack.Draw('hist')

            for sam in samples:
                
                if 'Signal' in sam:
                    h = file_input.Get(sam + '_' + var + '_' + cut)
                    tuneHistogram(h, colors[sam],  variables[var]['label'], 1)

                    if (args.norm == 'norm1'):
                        h.Scale(1/h.Integral())

                    if (args.log): 
                        h.SetMaximum(10.*h.GetMaximum())
                    else: h.SetMaximum(1.2*h.GetMaximum())

                    h.Draw('hist same')
                    h.Draw('axis same')

                    leg.AddEntry(h, sam, 'f')


            ## Draw the legend:
            leg.Draw()


            ## Save the plots

            c1.SaveAs(str(args.outputDir) + "/" + prefix + str(var) + '_' + str(cut) + '.png')
            c1.SaveAs(str(args.outputDir )+ "/" + prefix + str(var) + '_' + str(cut) + '.pdf')

            c1.Clear()


