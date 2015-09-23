from ROOT import *


f_histos=TFile("histos.root","RECREATE")
datafiles=["/storage/8/tpfotzer/BEANTrees/2015B_newGT/SingleMuon_2015B_Tree_TA.root ",
	   "/storage/8/tpfotzer/BEANTrees/2015B_newGT/SingleElectron_2015B_Tree_TA.root "]
datachain=TChain("MVATree")
for file in datafiles:
  datachain.AddFile(file)
#"/storage/8/tpfotzer/BEANTrees/2015B_newJEC/MC_Pythia_ST_tW_RUN2_Tree.root",
#	"/storage/8/tpfotzer/BEANTrees/2015B_newJEC/MC_Pythia_ST_t_RUN2_Tree.root",
#	"/storage/8/tpfotzer/BEANTrees/2015B_newJEC/MC_Pythia_ST_tbarW_RUN2_Tree.root",
#	"/storage/8/tpfotzer/BEANTrees/2015B_newJEC/MC_Pythia_ST_tbar_RUN2_Tree.root",
#	"/storage/8/tpfotzer/BEANTrees//2015B_newJEC/MC_Pythia_WJets_RUN2_Tree.root",
#	"/storage/8/tpfotzer/BEANTrees/2015B_newJEC/MC_Pythia_ZJets_RUN2_Tree.root",
#	"/storage/8/tpfotzer/BEANTrees/2015B_newJEC/MC_Pythia_WW_RUN2_Tree.root"
  
mcfiles_hf=["/storage/8/tpfotzer/BEANTrees/2015B_newGT/MC_Pythia_TTbar_RUN2_Tree.root",
	    "/storage/8/tpfotzer/BEANTrees/2015B_newGT/MC_Pythia_ST_tW_RUN2_Tree.root",
	    "/storage/8/tpfotzer/BEANTrees/2015B_newGT/MC_Pythia_ST_t_RUN2_Tree.root",
	    "/storage/8/tpfotzer/BEANTrees/2015B_newGT/MC_Pythia_ST_tbarW_RUN2_Tree.root",
	    "/storage/8/tpfotzer/BEANTrees/2015B_newGT/MC_Pythia_ST_tbar_RUN2_Tree.root",
	    "/storage/8/tpfotzer/BEANTrees/2015B_newGT/MC_QCD_MuEnriched_Tree.root"  ]
mcfiles_lf=["/storage/8/tpfotzer/BEANTrees/2015B_newGT/MC_Pythia_ZJets_RUN2_Tree.root",]	
mcchain_hf=TChain("MVATree")
for file in mcfiles_hf:
  mcchain_hf.AddFile(file)
mcchain_lf=TChain("MVATree")
for file in mcfiles_lf:
  mcchain_lf.AddFile(file)
########################
nbins=11
xmin=-0.1
xmax=1
ymin=0

ptbins_hf_j1probed=["((30<=Jet_Pt[1])&&(Jet_Pt[1]<40))","((40<=Jet_Pt[1])&&(Jet_Pt[1]<60))","((60<=Jet_Pt[1])&&(Jet_Pt[1]<100))","((100<=Jet_Pt[1])&&(Jet_Pt[1]<160))","(Jet_Pt[1]>=160)"]
ptbins_hf_j0probed=["((30<=Jet_Pt[0])&&(Jet_Pt[0]<40))","((40<=Jet_Pt[0])&&(Jet_Pt[0]<60))","((60<=Jet_Pt[0])&&(Jet_Pt[0]<100))","((100<=Jet_Pt[0])&&(Jet_Pt[0]<160))","(Jet_Pt[0]>=160)"]
ptbins_lf_j1probed=["((30<=Jet_Pt[1])&&(Jet_Pt[1]<40))","((40<=Jet_Pt[1])&&(Jet_Pt[1]<60))","((60<=Jet_Pt[1])&&(Jet_Pt[1]<100))","((100<=Jet_Pt[1])&&(Jet_Pt[1]<160))","(Jet_Pt[1]>=160)"]
ptbins_lf_j0probed=["((30<=Jet_Pt[0])&&(Jet_Pt[0]<40))","((40<=Jet_Pt[0])&&(Jet_Pt[0]<60))","((60<=Jet_Pt[0])&&(Jet_Pt[0]<100))","((100<=Jet_Pt[0])&&(Jet_Pt[0]<160))","(Jet_Pt[0]>=160)"]

#ptbins_lf_j1probed=["((30<=Jet_Pt[1])&&(Jet_Pt[1]<40))","((40<=Jet_Pt[1])&&(Jet_Pt[1]<60))","(Jet_Pt[1]>=60)"]
#ptbins_lf_j0probed=["((30<=Jet_Pt[0])&&(Jet_Pt[0]<40))","((40<=Jet_Pt[0])&&(Jet_Pt[0]<60))","(Jet_Pt[0]>=60)"]
	
etabins_lf_j0probed=["abs(Jet_Eta[0])<0.8","(0.8<=abs(Jet_Eta[0]))&&(abs(Jet_Eta[0]<1.6))","(1.6<=abs(Jet_Eta[0]))&&(abs(Jet_Eta[0])<2.4)"]
etabins_lf_j1probed=["abs(Jet_Eta[1])<0.8","(0.8<=abs(Jet_Eta[1]))&&(abs(Jet_Eta[1]<1.6))","(1.6<=abs(Jet_Eta[1]))&&(abs(Jet_Eta[1])<2.4)"]

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

for i in xrange(len(ptbins_hf_j0probed)):
  f_lfsf.append([])
  graph_hfsc.append([])
  mc_btmp_hf.append([])
  mc_b_hf.append([])
  mc_b_hf.append([])
  mc_nonb_hf.append([])
  mc_nonbtmp_hf.append([])  
  datahist_hf.append([])
  datahisttmp_hf.append([])
  
  mc_btmp_lf.append([])
  mc_b_lf.append([])
  mc_b_lf.append([])
  mc_nonb_lf.append([])
  mc_nonbtmp_lf.append([])  
  datahist_lf.append([])
  datahisttmp_lf.append([])
  

  for j in xrange(len(etabins_lf_j0probed)):
    f_lfsf[i].append(TF1("ptbin"+str(i)+"_etabin"+str(j),"pol6"))
    graph_hfsc[i].append([])
    
    mc_btmp_hf[i].append(TH1F("mc_btmp_hf_ptbin"+str(i)+"_etabin"+str(j),"b-flavor",nbins,xmin,xmax))
    mc_b_hf[i].append(TH1F("mc_b_hf_ptbin"+str(i)+"_etabin"+str(j),"b-flavor",nbins,xmin,xmax))
    mc_nonbtmp_hf[i].append(TH1F("mc_nonbtmp_hf_ptbin"+str(i)+"_etabin"+str(j),"non-b flavor",nbins,xmin,xmax))
    datahist_hf[i].append(TH1F("datahist_hf_ptbin"+str(i)+"_etabin"+str(j),"datahist",nbins,xmin,xmax))
    datahisttmp_hf[i].append(TH1F("datahisttmp_hf_ptbin"+str(i)+"_etabin"+str(j),"datahisttmp",nbins,xmin,xmax))
    mc_nonb_hf[i].append(TH1F("mc_nonb_hf_ptbin"+str(i)+"_etabin"+str(j),"non-b flavor",nbins,xmin,xmax))
    
    
    mc_btmp_lf[i].append(TH1F("mc_btmp_lf_ptbin"+str(i)+"_etabin"+str(j),"b-flavor",nbins,xmin,xmax))
    mc_b_lf[i].append(TH1F("mc_b_lf_ptbin"+str(i)+"_etabin"+str(j),"b-flavor",nbins,xmin,xmax))
    mc_nonb_lf[i].append(TH1F("mc_nonb_lf_ptbin"+str(i)+"_etabin"+str(j),"non-b flavor",nbins,xmin,xmax))
    datahist_lf[i].append(TH1F("datahist_lf_ptbin"+str(i)+"_etabin"+str(j),"datahist",nbins,xmin,xmax))
    datahisttmp_lf[i].append(TH1F("datahisttmp_lf_ptbin"+str(i)+"_etabin"+str(j),"datahisttmp",nbins,xmin,xmax))
    mc_nonbtmp_lf[i].append(TH1F("mc_nonbtmp_lf_ptbin"+str(i)+"_etabin"+str(j),"non-b flavor",nbins,xmin,xmax))
    
   




zveto="(((Zmumu_M<(65.5+0.375*Evt_Pt_MET))||(Zmumu_M>(108-0.25*Evt_Pt_MET))||(Zmumu_M<(79-0.75*Evt_Pt_MET))||(Zmumu_M>(99+0.5*Evt_Pt_MET)))||((Zelel_M<(65.5+0.375*Evt_Pt_MET))||(Zelel_M>(108-0.25*Evt_Pt_MET))||(Zelel_M<(79-0.75*Evt_Pt_MET))||(Zelel_M>(99+0.5*Evt_Pt_MET))))"
zveto_lf="(((Zmumu_M>(65.5+0.375*Evt_Pt_MET))||(Zmumu_M<(108-0.25*Evt_Pt_MET))||(Zmumu_M>(79-0.75*Evt_Pt_MET))||(Zmumu_M<(99+0.5*Evt_Pt_MET)))||((Zelel_M>(65.5+0.375*Evt_Pt_MET))||(Zelel_M<(108-0.25*Evt_Pt_MET))||(Zelel_M>(79-0.75*Evt_Pt_MET))||(Zelel_M<(99+0.5*Evt_Pt_MET))))"
lfmllcut="((abs(Zmumu_M-91)<10)||(abs(Zelel_M-91)<10))"
#0.004186*
backweight="(Weight*Weight_PV)"

  #################################
  ###########Project Histos########
  #################################
#for i in xrange(len(ptbins_hf_j0probed)):
for i in xrange(5):
  print ptbins_hf_j1probed[i]  

  #for j in xrange(len(etabins_lf_j0probed)):
  for j in xrange(3):
    print etabins_lf_j0probed[j]
    #################################
    ###########HEAVY FLAVOR##########
    #################################
    print "Projecting HF into Histos"
   
    bcut_j1probed_hf=backweight+"*((N_TightLeptons==2)&&(N_Jets==2)&&(Evt_Pt_MET>50)&&"+zveto+"&&(Jet_CSV[0]>0.89)"+"&&(abs(Jet_Flav[1])==5)&&("+ptbins_hf_j1probed[i]+")"+"&&("+etabins_lf_j1probed[j]+"))"
    nonbcut_j1probed_hf=backweight+"*((N_TightLeptons==2)&&(N_Jets==2)&&(Evt_Pt_MET>50)&&"+zveto+"&&(Jet_CSV[0]>0.89)"+"&&(abs(Jet_Flav[1])!=5)&&("+ptbins_hf_j1probed[i]+")"+"&&("+etabins_lf_j1probed[j]+"))"
    bcut_j0probed_hf=backweight+"*((N_TightLeptons==2)&&(N_Jets==2)&&(Evt_Pt_MET>50)&&"+zveto+"&&(Jet_CSV[1]>0.89)"+"&&(abs(Jet_Flav[0])==5)&&("+ptbins_hf_j0probed[i]+")"+"&&("+etabins_lf_j0probed[j]+"))"
    nonbcut_j0probed_hf=backweight+"*((N_TightLeptons==2)&&(N_Jets==2)&&(Evt_Pt_MET>50)&&"+zveto+"&&(Jet_CSV[1]>89)"+"&&(abs(Jet_Flav[0])!=5)&&("+ptbins_hf_j0probed[i]+")"+"&&("+etabins_lf_j0probed[j]+"))"
    datacut_j0probed_hf="(N_TightLeptons==2)&&(N_Jets==2)&&(Evt_Pt_MET>50)&&(Jet_CSV[1]>0.89)&&"+zveto+"&&("+ptbins_hf_j0probed[i]+")"+"&&("+etabins_lf_j0probed[j]+")"
    datacut_j1probed_hf="(N_TightLeptons==2)&&(N_Jets==2)&&(Evt_Pt_MET>50)&&(Jet_CSV[0]>0.89)&&"+zveto+"&&("+ptbins_hf_j1probed[i]+")"+"&&("+etabins_lf_j1probed[j]+")"
  
    datachain.Project(datahist_hf[i][j].GetName(),"Jet_CSV[1]",datacut_j1probed_hf)
    datachain.Project(datahisttmp_hf[i][j].GetName(),"Jet_CSV[0]",datacut_j0probed_hf)
    mcchain_hf.Project(mc_b_hf[i][j].GetName(),"Jet_CSV[1]",bcut_j1probed_hf)
    mcchain_hf.Project(mc_nonb_hf[i][j].GetName(),"Jet_CSV[1]",nonbcut_j1probed_hf)
    mcchain_hf.Project(mc_btmp_hf[i][j].GetName(),"Jet_CSV[0]",bcut_j0probed_hf)
    mcchain_hf.Project(mc_nonbtmp_hf[i][j].GetName(),"Jet_CSV[0]",nonbcut_j0probed_hf)
    
    #################################
    ###########LIGHT FLAVOR##########
    #################################  
    print "Projecting LF into Histos"
    bcut_j1probed_lf=backweight+"*((N_TightLeptons==2)&&(N_Jets==2)&&(Evt_Pt_MET<30)&&"+zveto_lf+"&&(Jet_CSV[0]<0.605)"+"&&(abs(Jet_Flav[1])==5)&&"+lfmllcut+"&&("+ptbins_lf_j1probed[i]+")"+"&&("+etabins_lf_j1probed[j]+"))"
    nonbcut_j1probed_lf=backweight+"*((N_TightLeptons==2)&&(N_Jets==2)&&(Evt_Pt_MET<30)&&"+zveto_lf+"&&(Jet_CSV[0]<0.605)"+"&&(abs(Jet_Flav[1])!=5)&&"+lfmllcut+"&&("+ptbins_lf_j1probed[i]+")"+"&&("+etabins_lf_j1probed[j]+"))"
    bcut_j0probed_lf=backweight+"*((N_TightLeptons==2)&&(N_Jets==2)&&(Evt_Pt_MET<30)&&"+zveto_lf+"&&(Jet_CSV[1]<0.605)"+"&&(abs(Jet_Flav[0])==5)&&"+lfmllcut+"&&("+ptbins_lf_j0probed[i]+")"+"&&("+etabins_lf_j0probed[j]+"))"
    nonbcut_j0probed_lf=backweight+"*((N_TightLeptons==2)&&(N_Jets==2)&&(Evt_Pt_MET<30)&&"+zveto_lf+"&&(Jet_CSV[1]<0.605)"+"&&(abs(Jet_Flav[0])!=5)&&"+lfmllcut+"&&("+ptbins_lf_j0probed[i]+")"+"&&("+etabins_lf_j0probed[j]+"))"
    datacut_j0probed_lf="(N_TightLeptons==2)&&(N_Jets==2)&&(Evt_Pt_MET<30)&&(Jet_CSV[1]>0.605)&&"+zveto_lf+"&&"+lfmllcut+"&&("+ptbins_lf_j0probed[i]+")"+"&&("+etabins_lf_j0probed[j]+")"
    datacut_j1probed_lf="(N_TightLeptons==2)&&(N_Jets==2)&&(Evt_Pt_MET<30)&&(Jet_CSV[0]>0.605)&&"+zveto_lf+"&&"+lfmllcut+"&&("+ptbins_lf_j1probed[i]+")"+"&&("+etabins_lf_j1probed[j]+")"

    datachain.Project(datahist_lf[i][j].GetName(),"Jet_Eta[1]",datacut_j1probed_lf)
    datachain.Project(datahisttmp_lf[i][j].GetName(),"Jet_Eta[0]",datacut_j0probed_lf)
    mcchain_lf.Project(mc_b_lf[i][j].GetName(),"Jet_CSV[1]",bcut_j1probed_lf)
    mcchain_lf.Project(mc_nonb_lf[i][j].GetName(),"Jet_CSV[1]",nonbcut_j1probed_lf)
    mcchain_lf.Project(mc_btmp_lf[i][j].GetName(),"Jet_CSV[0]",bcut_j0probed_lf)
    mcchain_lf.Project(mc_nonbtmp_lf[i][j].GetName(),"Jet_CSV[0]",nonbcut_j0probed_lf)
    
    ###write histos to file###
    mc_b_hf[i][j].Write()
    mc_nonb_hf[i][j].Write()
    mc_btmp_hf[i][j].Write()
    mc_nonbtmp_hf[i][j].Write()
    datahist_hf[i][j].Write()
    datahisttmp_hf[i][j].Write()
    
    mc_b_lf[i][j].Write()
    mc_nonb_lf[i][j].Write()
    mc_btmp_lf[i][j].Write()
    mc_nonbtmp_lf[i][j].Write()
    datahist_lf[i][j].Write()
    datahisttmp_lf[i][j].Write()


f_histos.Close()   
    
    
    
    
    
    