from ROOT import *
  
def set_stackattributes(stack,ymin,log,norm=False):
  if norm==False:
    stack.SetMinimum(ymin)
  else: stack.SetMinimum(0)
  if log:
    stack.SetMaximum(1.5*stack.GetMaximum())  
  else: stack.SetMaximum(1.2*stack.GetMaximum())
  stack.GetXaxis().SetNdivisions(0)
  stack.GetYaxis().SetTitle("Events")

def makeleg(backhistos,datahist,backnames):
  leg=TLegend(0.75,0.4,0.9,0.8)
  leg.AddEntry(datahist,"data")
  for i in xrange(len(backhistos)):
    leg.AddEntry(backhistos[i],backnames[i],"f")
  leg.SetFillStyle(0)
  leg.SetBorderSize(0)
  return leg

def makeratio(stack,datahist,xtitle):
  back=stack.GetStack().Last()
  ratio=datahist.Clone()
  ratio.SetTitle("")
  ratio.SetXTitle(xtitle)
  ratio.Sumw2()
  ratio.SetStats(0)
  ratio.Divide(back)
  ratio.SetMarkerStyle(20)
  SetOwnership(ratio,0)
  ratio.Draw("E0")
  ratio.SetMaximum(1.6)
  ratio.SetMinimum(0.4)
  return ratio
  
def set_ratioattributes(ratio,xmin,xmax,nbins,xtitle):
  ratio.GetYaxis().SetNdivisions(510)
  ratio.GetYaxis().SetLabelSize(0.1)
  
  ratio.GetXaxis().SetTitle(xtitle)
  ratio.GetXaxis().SetTitleSize(0.11)
  if nbins<15:
    ratio.GetXaxis().SetNdivisions(nbins,0,0)
  else: ratio.GetXaxis().SetNdivisions(nbins/2,0,0)
  ratio.GetXaxis().SetLabelSize(0.1)

def makepadhist(log,norm):
  padhist=TPad("pad_hist","pad_hist",0,0.3,1,1)
  SetOwnership(padhist,0)
  padhist.SetBottomMargin(0)
  padhist.Draw()
  padhist.cd()
  if log==True and norm==False :
    padhist.SetLogy() 
  
def makepadratio():
  pad_ratio=TPad("pad_ratio","pad_ratio",0,0,1,0.3)
  SetOwnership(pad_ratio,0)
  pad_ratio.SetTopMargin(0)
  pad_ratio.SetBottomMargin(0.3)
  pad_ratio.Draw()
  pad_ratio.cd()

########################

f_histos=TFile("histos.root")
f_histos.ls()


text="CMS private work"

log=False
norm=False
xtitle="CSV"
nbins=11
xmin=-0.1
xmax=1
ymin=0

backnames=["b","non-b"]
ptbins_hf_j1probed=["((30<=Jet_Pt[1])&&(Jet_Pt[1]<40))","((40<=Jet_Pt[1])&&(Jet_Pt[1]<60))","((60<=Jet_Pt[1])&&(Jet_Pt[1]<100))","((100<=Jet_Pt[1])&&(Jet_Pt[1]<160))","(Jet_Pt[1]>=160)"]
ptbins_hf_j0probed=["((30<=Jet_Pt[0])&&(Jet_Pt[0]<40))","((40<=Jet_Pt[0])&&(Jet_Pt[0]<60))","((60<=Jet_Pt[0])&&(Jet_Pt[0]<100))","((100<=Jet_Pt[0])&&(Jet_Pt[0]<160))","(Jet_Pt[0]>=160)"]
ptbins_lf_j1probed=["((30<=Jet_Pt[1])&&(Jet_Pt[1]<40))","((40<=Jet_Pt[1])&&(Jet_Pt[1]<60))","(Jet_Pt[1]>=60)"]
ptbins_lf_j0probed=["((30<=Jet_Pt[0])&&(Jet_Pt[0]<40))","((40<=Jet_Pt[0])&&(Jet_Pt[0]<60))","(Jet_Pt[0]>=60)"]
etabins_lf_j1probed=["abs(Jet_Eta[1])<0.8","(0.8<=abs(Jet_Eta[1]))&&(abs(Jet_Eta[1]<1.6))","(1.6<=abs(Jet_Eta[1]))&&(abs(Jet_Eta[1])<2.4)"]
etabins_lf_j0probed=["abs(Jet_Eta[0])<0.8","(0.8<=abs(Jet_Eta[0]))&&(abs(Jet_Eta[0]<1.6))","(1.6<=abs(Jet_Eta[0]))&&(abs(Jet_Eta[0])<2.4)"]

f_lfsf=[]
graph_hfsc=[]
mc_btmp_hf=[]
mc_b_hf=[]
mc_b_hf=[]
mc_nonb_hf=[]
mc_nonbtmp_hf=[]
datahist_hf=[]
datahisttmp_hf=[]

mc_btmp_lf=[]
mc_b_lf=[]
mc_b_lf=[]
mc_nonb_lf=[]
mc_nonbtmp_lf=[]
datahist_lf=[]
datahisttmp_lf=[]

lfsf=[]
hfsf=[]

print "Read Histos"
for i in xrange(len(ptbins_hf_j0probed)):
  f_lfsf.append([])
  graph_hfsc.append([])
  mc_btmp_hf.append([])
  mc_b_hf.append([])
  mc_nonb_hf.append([])
  mc_nonbtmp_hf.append([])  
  datahist_hf.append([])
  datahisttmp_hf.append([])
  
  mc_btmp_lf.append([])
  mc_b_lf.append([])
  mc_nonb_lf.append([])
  mc_nonbtmp_lf.append([])  
  datahist_lf.append([])
  datahisttmp_lf.append([])
  
  lfsf.append([])
  hfsf.append([TH1F])
  
  
  
  for j in xrange(len(etabins_lf_j0probed)):    
    f_lfsf[i].append(TF1("ptbin"+str(i)+"_etabin"+str(j),"pol6"))
    graph_hfsc[i].append([])
    
    mc_btmp_hf[i].append(TH1F("mc_btmp_hf_ptbin"+str(i)+"_etabin"+str(j),"b-flavor",nbins,xmin,xmax))    
    mc_nonbtmp_hf[i].append(TH1F("mc_nonb_hf_tmpptbin"+str(i)+"_etabin"+str(j),"non-b flavor",nbins,xmin,xmax))
    datahist_hf[i].append(TH1F("datahist_hf_ptbin"+str(i)+"_etabin"+str(j),"datahist",nbins,xmin,xmax))
    datahisttmp_hf[i].append(TH1F("datahisttmp_hf_ptbin"+str(i)+"_etabin"+str(j),"datahisttmp",nbins,xmin,xmax))
    mc_nonb_hf[i].append(TH1F("mc_nonb_hf_ptbin"+str(i)+"_etabin"+str(j),"non-b flavor",nbins,xmin,xmax))
    mc_b_hf[i].append(TH1F("mc_b_hf_ptbin"+str(i)+"_etabin"+str(j),"b-flavor",nbins,xmin,xmax))
    
    mc_btmp_lf[i].append(TH1F("mc_btmp_lf_ptbin"+str(i)+"_etabin"+str(j),"b-flavor",nbins,xmin,xmax))
    mc_b_lf[i].append(TH1F("mc_b_lf_ptbin"+str(i)+"_etabin"+str(j),"b-flavor",nbins,xmin,xmax))
    mc_nonb_lf[i].append(TH1F("mc_nonb_lf_ptbin"+str(i)+"_etabin"+str(j),"non-b flavor",nbins,xmin,xmax))
    datahist_lf[i].append(TH1F("datahist_lf_ptbin"+str(i)+"_etabin"+str(j),"datahist",nbins,xmin,xmax))
    datahisttmp_lf[i].append(TH1F("datahist_lf_tmpptbin"+str(i)+"_etabin"+str(j),"datahisttmp",nbins,xmin,xmax))
    mc_nonbtmp_lf[i].append(TH1F("mc_nonb_lf_tmpptbin"+str(i)+"_etabin"+str(j),"non-b flavor",nbins,xmin,xmax))
    
    mc_btmp_hf[i][j].SetDirectory(0)
    mc_nonbtmp_hf[i][j].SetDirectory(0)
    mc_b_hf[i][j].SetDirectory(0)
    mc_nonb_hf[i][j].SetDirectory(0)
    datahist_hf[i][j].SetDirectory(0)
    datahisttmp_hf[i][j].SetDirectory(0)

    SetOwnership(mc_btmp_hf[i][j],0)
    SetOwnership(mc_nonbtmp_hf[i][j],0)
    SetOwnership(mc_b_hf[i][j],0)
    SetOwnership(mc_nonb_hf[i][j],0)
    SetOwnership(datahist_hf[i][j],0)
    SetOwnership(datahisttmp_hf[i][j],0)
    #mc_b_hf[i][j].Print()
    
      
    mc_btmp_lf[i][j].SetDirectory(0)
    mc_nonbtmp_lf[i][j].SetDirectory(0)
    mc_b_lf[i][j].SetDirectory(0)
    mc_nonb_lf[i][j].SetDirectory(0)
    datahist_lf[i][j].SetDirectory(0)
    datahisttmp_lf[i][j].SetDirectory(0)

    SetOwnership(mc_btmp_lf[i][j],0)
    SetOwnership(mc_nonbtmp_lf[i][j],0)
    SetOwnership(mc_b_lf[i][j],0)
    SetOwnership(mc_nonb_lf[i][j],0)
    SetOwnership(datahist_lf[i][j],0)
    SetOwnership(datahisttmp_lf[i][j],0)
    

    mc_btmp_hf[i][j]=f_histos.Get("mc_btmp_hf_ptbin"+str(i)+"_etabin"+str(j))    
    mc_nonbtmp_hf[i][j]=f_histos.Get("mc_nonbtmp_hf_ptbin"+str(i)+"_etabin"+str(j))
    datahist_hf[i][j]=f_histos.Get("datahist_hf_ptbin"+str(i)+"_etabin"+str(j))
    datahisttmp_hf[i][j]=f_histos.Get("datahisttmp_hf_ptbin"+str(i)+"_etabin"+str(j))
    mc_nonb_hf[i][j]=f_histos.Get("mc_nonb_hf_ptbin"+str(i)+"_etabin"+str(j))
    mc_b_hf[i][j]=f_histos.Get("mc_b_hf_ptbin"+str(i)+"_etabin"+str(j))
    
    #mc_b_hf[i][j].Print()
    #datahist_hf[i][j].Print()
    
    mc_btmp_lf[i][j]=f_histos.Get("mc_btmp_lf_ptbin"+str(i)+"_etabin"+str(j))
    mc_b_lf[i][j]=f_histos.Get("mc_b_lf_ptbin"+str(i)+"_etabin"+str(j))
    mc_nonb_lf[i][j]=f_histos.Get("mc_nonb_lf_ptbin"+str(i)+"_etabin"+str(j))
    datahist_lf[i][j]=f_histos.Get("datahist_lf_ptbin"+str(i)+"_etabin"+str(j))
    datahisttmp_lf[i][j]=f_histos.Get("datahisttmp_lf_ptbin"+str(i)+"_etabin"+str(j))
    mc_nonbtmp_lf[i][j]=f_histos.Get("mc_nonbtmp_lf_ptbin"+str(i)+"_etabin"+str(j))
    
    mc_b_hf[i][j].SetFillColor(kRed)
    mc_nonb_hf[i][j].SetFillColor(kGreen)
    datahist_hf[i][j].SetMarkerStyle(20)
    datahist_hf[i][j].SetMarkerSize(0.7)
    datahist_hf[i][j].Sumw2()
    
    mc_b_lf[i][j].SetFillColor(kRed)
    mc_nonb_lf[i][j].SetFillColor(kGreen)
    datahist_lf[i][j].SetMarkerStyle(20)
    datahist_lf[i][j].SetMarkerSize(0.7)
    datahist_lf[i][j].Sumw2()
    
    lfsf[i].append(TH1F())
    
    
#f_histos.Close()



gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
line=TLine(xmin,1,xmax,1)
line.SetLineColor(kBlack)

text1 = TLatex()
text1.SetNDC()
text1.SetTextFont(42)
text1.SetTextSize(0.05)

#################################
###########PLOT##################
#################################  

#################plot#################
print "MAKE PLOTS"
for k in xrange(3):
  for i in xrange(len(ptbins_hf_j0probed)):
    print "analyzing HF"     
    #################################
    ###########HEAVY FLAVOR##########
    #################################    
    cutlabel="Muon Channel, HF, ==2tlp, ==2 Jets, pass Z veto, >=1N_BTagT, ptbin"+str(i)+" etabin"+str(j)+" it"+ str(k) 
    stack=THStack()
    hf_b=mc_b_hf[i][0].Clone()
    hf_nonb=mc_nonb_hf[i][0].Clone()
    hf_data=datahist_hf[i][0].Clone()    
    
    for j in xrange(len(etabins_lf_j0probed)):
	hf_data.Add(datahist_hf[i][j])
	hf_data.Add(datahisttmp_hf[i][j])
	hf_b.Add(mc_btmp_hf[i][j])
	hf_b.Add(mc_btmp_hf[i][j])
	mc_nonb_hf[i][j].Add(mc_nonbtmp_hf[i][j])
      ##apply LF SF
	if k!=0:
	  mc_nonb_hf[i][j].Multiply(lfsf[i][j])
	  mc_nonbtmp_hf[i][j].Multiply(lfsf[i][j])
    for j in xrange(len(etabins_lf_j0probed)):
      hf_nonb.Add(mc_nonb_hf[i][j])
      hf_nonb.Add(mc_nonbtmp_hf[i][j])	
      ###makestack###
    stack.Add(hf_b,"hist")
    stack.Add(hf_nonb,"hist")  
    back_hf=stack.GetStack().Last()   
  
    #normierung  auf data event yield
    backevents_hf=back_hf.Integral()
    dataevents_hf=hf_data.Integral()
    if backevents_hf!=0:
      normratio_hf=dataevents_hf/backevents_hf
    else: normratio_hf=1
    hf_b.Scale(normratio_hf)
    hf_nonb.Scale(normratio_hf)
    #print "normalized"
  
    mcstack_hf=THStack()
    mcstack_hf.Add(hf_b,"hist")
    mcstack_hf.Add(hf_nonb,"hist")
    #print "mchstack rdy"
  
    c=TCanvas()
    c.cd()  
    mchistos_hf=[hf_b,hf_nonb]
    leg_hf=makeleg(mchistos_hf,hf_data.GetName(),backnames)
    makepadhist(log,norm)  
    mcstack_hf.Draw()
    set_stackattributes(mcstack_hf,ymin,log,norm)
    hf_data.Draw("SAMEE0")
    leg_hf.Draw()  
    text1.DrawLatex(0.175, 0.863, text)
    #text1.DrawLatex(0.175, 0.76, "#geq 6 Jets, #geq 4 b-tags, 1 tight muon")
    text1.DrawLatex(0.175, 0.815, cutlabel) 
      
    mcsum_hf=mcstack_hf.GetStack().Last()
    mcevents_hf=mcsum_hf.Integral()
    print "MC Events: ", mcevents_hf
    print "data Events: ",dataevents_hf
      
    c.cd()
    makepadratio()  
    ratio_hf=makeratio(mcstack_hf,hf_data,xtitle)
    set_ratioattributes(ratio_hf,xmin,xmax,nbins,xtitle)
    line.Draw()    
  
    c.Print("HF"+"_ptbin"+str(i)+"_it_"+str(k)+".pdf")
    #c.Print("HF"+"_ptbin"+str(i)+".png")

    c2=TCanvas()
    c2.cd()
    #print "calculate diff"
    hist_diff_hf=hf_data.Clone()
    hist_diff_hf.SetTitle("Data-nonb")
    hist_diff_hf.Add((-1)*hf_nonb)
    hist_diff_hf.Draw("E0")
    hist_diff_hf.SetLineColor(kBlue)
  
    hf_b.Draw("SAMEE0")
    hf_b.SetMarkerStyle(20)
    hf_b.SetMarkerSize(0.7)
    hf_b.SetLineColor(kRed)
    c2.BuildLegend(0.2,0.8,0.7,0.9)

    text1.DrawLatex(0.175, 0.95, "HF_diff_ptbin"+str(i)+"_etabin"+str(j)+"_it_"+str(k))
    c2.Print("HF"+"_diff_ptbin"+str(i)+"_etabin"+str(j)+"_it_"+str(k)+".pdf")
    #c2.Print("HF"+"_diff_ptbin"+str(i)+".png")
  
    c3=TCanvas()
    c3.cd()
    #print "calculate scalefactors"
    hfsf[i]=hist_diff_hf.Clone()
    hfsf[i].SetTitle("HFSC")
    hfsf[i].SetName("hfsc_ptbin"+str(i))
    hfsf[i].Divide(hf_b)
    hfsf[i].Draw("E0")
    hfsf[i].SetMarkerSize(0.7)
    hfsf[i].SetMarkerStyle(20)
    graph_hfsc[i][j]=TGraph(hfsf[i])
    #print graph_hfsc.Eval(0.2)
    graph_hfsc[i][j].Draw("SAMEC")
    #hist_hfsf.Eval(interpol)
    c3.BuildLegend(0.2,0.85,0.7,0.9)
    text1.DrawLatex(0.175, 0.95, "ptbin"+str(i)+"_it_"+str(j))   
    c3.Print("HFSC"+"_ptbin"+str(i)+"_etabin"+str(j)+"_it_"+str(j)+".pdf") 
    #c3.Print("HFSC"+"_ptbin"+str(i)+".png")
    
    
  #################################
  ###########LIGHT FLAVOR##########
  #################################
  
  
  #for j in xrange(len(etabins_lf_j0probed)):
    cutlabel="Muon Channel, LF, ==2tlp, ==2 Jets, fail Z veto, >=1N_BTagT, ptbin"+str(i)+" etabin"+str(j)+" it"+ str(k) 
    print "analyzing LF" 
    for j in xrange(len(etabins_lf_j0probed)):
      datahist_lf[i][j].Add(datahisttmp_lf[i][j])    
      mc_b_lf[i][j].Add(mc_btmp_lf[i][j])
      mc_nonb_lf[i][j].Add(mc_nonbtmp_lf[i][j])
	
      #apply HF SF
      if i!=0:
	mc_b_lf[i][j].Multiply(hfsf[i])
    
      ###makestack###
      stack_lf=THStack()
      stack_lf.Add(mc_b_lf[i][j],"hist")
      stack_lf.Add(mc_nonb_lf[i][j],"hist")

    
      back_lf=stack_lf.GetStack().Last()
      
  #normierung  auf data event yield
      backevents_lf=back_lf.Integral()
      dataevents_lf=datahist_lf[i][j].Integral()
      if backevents_lf!=0:
	normratio_lf=dataevents_lf/backevents_lf
      else: normratio_lf=1
      mc_b_lf[i][j].Scale(normratio_lf)
      mc_nonb_lf[i][j].Scale(normratio_lf)
    
      mcstack_lf=THStack()
      mcstack_lf.Add(mc_b_lf[i][j],"hist")
      mcstack_lf.Add(mc_nonb_lf[i][j],"hist")
    
      c4=TCanvas()
      c4.cd()  
      mchistos_lf=[mc_b_lf[i][j],mc_nonb_lf[i][j]]
      leg_lf=makeleg(mchistos_lf,datahist_lf[i][j].GetName(),backnames)
      makepadhist(log,norm)  
      mcstack_lf.Draw()
      set_stackattributes(mcstack_hf,ymin,log,norm)
      datahist_lf[i][j].Draw("SAMEE0")
      leg_lf.Draw()  
      text1.DrawLatex(0.175, 0.863, text)
      #text1.DrawLatex(0.175, 0.76, "#geq 6 Jets, #geq 4 b-tags, 1 tight muon")
      text1.DrawLatex(0.175, 0.815, cutlabel) 

      mcsum_lf=mcstack_lf.GetStack().Last()
      mcevents_lf=mcsum_lf.Integral()
      print "MC Events: ", mcevents_lf
      print "data Events: ",dataevents_lf

    
      c4.cd()
      makepadratio()  
      ratio_lf=makeratio(mcstack_lf,datahist_lf[i][j],xtitle)
      set_ratioattributes(ratio_lf,xmin,xmax,nbins,xtitle)
      line.Draw()    
      c4.Print("LF"+"_ptbin"+str(i)+"_etabin"+str(j)+"_it_"+str(k)+".pdf")
      #c4.Print("LF"+"_ptbin"+str(i)+"_etabin"+str(j)+".png")

      c5=TCanvas()
      c5.cd()
      hist_diff_lf=datahist_lf[i][j].Clone()
      hist_diff_lf.SetTitle("Data-b")
      hist_diff_lf.Add((-1)*mc_b_lf[i][j])
      hist_diff_lf.Draw("E0")
      hist_diff_lf.SetLineColor(kBlue)
  
      mc_nonb_lf[i][j].Draw("SAMEE0")
      mc_nonb_lf[i][j].SetMarkerStyle(20)
      mc_nonb_lf[i][j].SetMarkerSize(0.7)
      mc_nonb_lf[i][j].SetLineColor(kRed)
      c5.BuildLegend(0.2,0.8,0.7,0.9)
      text1.DrawLatex(0.175, 0.95, "LF_ptbin"+str(i)+"_etabin"+str(j)+"_it_"+str(k))  
      c5.Print("LF"+"_diff_ptbin"+str(i)+"_etabin"+str(j)+"_it_"+str(k)+".pdf")
      #c5.Print("LF"+"_diff_ptbin"+str(i)+"_etabin"+str(j)+".png")
    
      c6=TCanvas()
      c6.cd()
      lfsf[i][j]=hist_diff_lf.Clone()
      lfsf[i][j].SetTitle("LFSC")
      lfsf[i][j].SetName("lfsc_ptbin"+str(i)+"_etabin"+str(j)+"_it_"+str(k))
      lfsf[i][j].Divide(mc_nonb_lf[i][j])
      lfsf[i][j].Draw("E0")
      lfsf[i][j].SetMarkerSize(0.7)
      lfsf[i][j].SetMarkerStyle(20)
      ##Fit LFSC
      
      f_lfsf[i][j]=lfsf[i][j].Fit("pol6","F","",0,1)
      c6.BuildLegend(0.2,0.85,0.7,0.9)
      text1.DrawLatex(0.175, 0.95, "ptbin"+str(i)+"_etabin"+str(j)+"_it_"+str(k))   
      c6.Print("LFSC"+"_ptbin"+str(i)+"_etabin"+str(j)+"_it_"+str(k)+".pdf") 
      #c6.Print("LFSC"+"_ptbin"+str(i)+"_etabin"+str(j)+".png")

#canvas.Print(pdfname+"]")
raw_input("Press Enter...")

    