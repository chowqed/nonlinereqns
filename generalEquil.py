# Filename: generalEquil.py
# Author: Ken Chow
# This file is the main implementation file for the applied general equilibirum model
# as outlined in Shoven and Whalley. It requires the parameters.py and market-clearing.py
# files which define all the parameters and functions needed for calculating the 
# equilibrium values of the model. It uses the fsolve function from the scipy package 
# to determines all the equilibrium prices, outputs, demands etc from the 16 coupled 
# nonlinear equations defining the simple eocnomy in the paper (equations (1)-(11)).
# IMPORTANT: warning messages from scipy and numpy are suppressed, remove the suppression
# for further development or debugging

from parameters import *  # import global parameters and factors function
from marketClearing import * # import market clearing conditions functions
from scipy.optimize import fsolve  # import fsolve for solving nonlinear equations
import warnings # warning messages handler
warnings.simplefilter("ignore") # suppress warning messages from scipy and numpy 

def tax_policy(p,t1=0,t2=0): # vector valued function for the equilibrium conditions 
	q1=p[0]
	q2=p[1]
	p1=p[2]
	p2=p[3]
	pk=p[4]
	pl=p[5]
	xr1=p[6]
	xr2=p[7]
	xp1=p[8]
	xp2=p[9]
	kk1=p[10]
	kk2=p[11]
	ll1=p[12]
	ll2=p[13]
	ir=p[14]
	ip=p[15]

	x0=(demand1(xr1,xp1,q1), demand2(xr2,xp2,q2), capitalCond(kk1,kk2,k_rich),labourCond(ll1,ll2,l_poor), profitcond1(pk,kk1,pl,ll1,p1,q1,t1), profitcond2(pk,kk2,pl,ll2,p2,q2,t2), x_r_1(xr1,ir,p1,p2), x_r_2(xr2,ir,p1,p2), x_p_1(xp1,ip,p1,p2), x_p_2(xp2,ip,p1,p2), cap1(kk1,q1,pk,pl,t1), cap2(kk2,q2,pk,pl,t2), lab1(ll1,q1,pk,pl,t1), lab2(ll2,q2,pk,pl,t2), income1(ir,pk,pl,q1,q2,kk1,kk2,t1,t2), income2(ip,pk,pl,q1,q2,kk1,kk2,t1,t2),pl-1)
	return x0

def equilibrium(init=(10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10),tax1=0,tax2=0): # calculate the roots with fsolve
	s=fsolve(tax_policy,init,(tax1,tax2))
	return s



t0_1=0.5 # initial tax on manufacturing sector
t0_2=0.0 # initial tex on non-manufacturing sector
t1_1=0.5 # new tax on manufacturing
t1_2=0.5 # new tax on non-manufacturing

s=equilibrium() # reproduce table 1.2 from the paper
init2=(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10],s[11],s[12],s[13],s[14],s[15],s[16]) # using this output as the initial guess for cases where there are taxes
e1=equilibrium(init2,t0_1,t0_2) # equilibrium with taxes t0_1, t0_2
e2=equilibrium(init2,t1_1,t1_2) # equilibrium with taxes t1_1, t1_2


print s # table 1.2
print e1 # table 1.3
print e2 # equilibrium values with taxes on both sectors

print "EV and CV changes from no tax to the tax structure (", t0_1,",", t0_2,") :"
print "EV for rich household: ",
print ev_rich(e1[6],e1[7],s[6],s[7],s[14])
print "CV for rich household: ",
print cv_rich(e1[6],e1[7],s[6],s[7],e1[14])
print "EV for poor household: ",
print ev_poor(e1[8],e1[9],s[8],s[9],s[15])
print "CV for poor household", 
print cv_poor(e1[8],e1[9],s[8],s[9],e1[15])

print "EV and CV changes from the tax structure (", t0_1,",", t0_2,") to the tax structure (", t1_1,",", t1_2,") :"
print "EV for rich household: ",
print ev_rich(e2[6],e2[7],e1[6],e1[7],e1[14])
print "CV for rich household: ",
print cv_rich(e2[6],e2[7],e1[6],e1[7],e2[14])
print "EV for poor household: ",
print ev_poor(e2[8],e2[9],e1[8],e1[9],e1[15])
print "CV for poor household", 
print cv_poor(e2[8],e2[9],e1[8],e1[9],e2[15])

print "EV and CV changes from no tax to the tax structure (", t1_1,",", t1_2,") :"
print "EV for rich household: ",
print ev_rich(e2[6],e2[7],s[6],s[7],s[14])
print "CV for rich household: ",
print cv_rich(e2[6],e2[7],s[6],s[7],e2[14])
print "EV for poor household: ",
print ev_poor(e2[8],e2[9],s[8],s[9],s[15])
print "CV for poor household", 
print cv_poor(e2[8],e2[9],s[8],s[9],e2[15])

