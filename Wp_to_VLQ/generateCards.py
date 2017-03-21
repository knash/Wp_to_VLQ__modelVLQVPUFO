#! /bin/env python

import os, shutil, subprocess

Reference_dirs = ["WpToTpB_conf","WpToBpT_conf"]
for Reference_dir in Reference_dirs:
	prefixington = Reference_dir.replace('_conf','')
	VLQ = Reference_dir.replace('WpTo','')[0:2]

	if VLQ=='Tp':
		pdgid = '6000006'
	elif VLQ=='Bp':
		pdgid = '6000007'
	else:
		print "BAD VLQ"
	FinalStates = ["Ht"]
	Chiralities =["LH","RH"]
	Masses = [[1500,[700,900,1200]],[2000,[900,1200,1500]],[2500,[1200,1500,1900]]]
	Zwidths = [[0.03,'Nar'],[0.1,'Wid'],[0.3,'ExWid']]
	Twidths = [[0,'Nar'],[0.1,'Wid'],[0.3,'ExWid']]

	for state in FinalStates:
		for hand in Chiralities:
			for zmass in Masses:
				for tmass in zmass[1]:
					for zwidth in Zwidths:
						for twidth in Twidths:
							if twidth[1]=='Wid' and zwidth[1]=='Nar' and not (
								(zmass[0]==1500 and tmass==700 and hand=='LH') or
								(zmass[0]==2000 and tmass==1200 and hand=='LH') or
								(zmass[0]==2500 and tmass==1900 and hand=='LH') ):
								continue
							if zwidth[1]=='Wid' and twidth[1]=='Nar' and not (
								(zmass[0]==1500 and tmass==700 and hand=='LH') or
								(zmass[0]==2000 and tmass==1200 and hand=='LH') or
								(zmass[0]==2500 and tmass==1900 and hand=='LH') ):
								continue
							if zwidth[1]=='Wid' and twidth[1]=='Wid' and not (
								(zmass[0]==1500 and tmass==700 and hand=='LH') or
								(zmass[0]==2000 and tmass==1200 and hand=='LH') or
								(zmass[0]==2500 and tmass==1900 and hand=='LH') ):
								continue
							#create name
							sampleName = prefixington+'_Wp'+str(zmass[0])+zwidth[1]+'_'+VLQ+str(tmass)+twidth[1]+hand+'_'+state
							print sampleName
							#remove dir if already exists and create
							if os.path.isdir(sampleName):
								shutil.rmtree(sampleName)
							os.makedirs(sampleName)
							# Copy cards
							shutil.copyfile(Reference_dir+'/'+'run_card.dat',sampleName+'/'+sampleName+'_run_card.dat')
							shutil.copyfile(Reference_dir+'/'+state+'_madspin_card.dat',sampleName+'/'+sampleName+'_madspin_card.dat')
							shutil.copyfile(Reference_dir+'/'+state+'_proc_card.dat',sampleName+'/'+sampleName+'_proc_card.dat')
							shutil.copyfile(Reference_dir+'/'+state+'_'+hand+'_customizecards.dat',sampleName+'/'+sampleName+'_customizecards.dat')
							shutil.copyfile(Reference_dir+'/extramodels.dat',sampleName+'/'+sampleName+'_extramodels.dat')
							#customization
							with open("{0}/{0}_proc_card.dat".format(sampleName), "a") as f:
								f.write("output "+sampleName)
							with open("{0}/{0}_customizecards.dat".format(sampleName), "a") as f:
								f.write("set param_card mass "+pdgid+" %e\n" % tmass)
								f.write("set param_card mass 6000024 %e\n" % zmass[0])
								f.write("set param_card decay 6000024 %e\n" % (zmass[0] * zwidth[0]))
								if twidth[0]==0:
									f.write("set param_card decay "+pdgid+" %e" % 0.001)
								else:
									f.write("set param_card decay "+pdgid+" %e" % (tmass * twidth[0]))
