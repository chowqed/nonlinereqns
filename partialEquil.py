# Filename: partialEquil.py
# Author: Ken Chow
# Date: 25/09/2012
# This file contains various functions for calculating partial equilibrium 
# results from Shoven and Whalley (1984). It requires the parameters.py file for
# definitions of global parameters and other primitive functions definitions

from parameters import *
from scipy.integrate import quad  # quad is the numarical integration function

# defining parameters for partial equil calculations
ir=34.337 # income for rich household from table 2
ip=60     # income for poor household from table 2
p0=1.399  # price of manufacturing goods before taxes 
p2=1.093  # price for non-manufacturing goods 
tm=0.5    # tax rate on the manufacturing good
pk=1.373  # price of capital
pl=1      # price of labour


def supply(tm): # supply curve which equals to the marginal cost function
 	pkt=pk*(1+tm) # price of capital at tax rate tm	
	s=pl*l1(1,pk,pl,tm)+pkt*k1(1,pk,pl,tm) # marginal cost for good m
	return s

def demandM(p1): # total demand for the manufacturing good
	x=x_rich_1(ir,p1,p2)+x_poor_1(ip,p1,p2)
	return x

def govRev(p1): # government revenue from tax
	q=demandM(p1)  # demand for manufacturing good at price p1
	k=k1(q,p1,p2,tm)  # capital demand at q, p1, p2
	g=pk*tm*k      # government revenue
	return g

def richD(p1): # damand curve for rich household
	return x_rich_1(ir,p1,p2)

def poorD(p1): # demand curve for poor household
	return x_poor_1(ip,p1,p2)

def richD2(p1): # deamand for good 2 from rich household 
	return x_rich_2(ir,p1,p2)

def poorD2(p1): # demand for good 2 from the poor household
	return x_poor_2(ip,p1,p2)

def welfareloss(func,p1,t,share): # calculating welfare loss, func is the demand curve
	govDist=govRev(p1)*share # share of government rebate 
	#print quad(func,p0,p1)[0], govDist
	return govDist-quad(func,p0,p1)[0]


p1=supply(tm) # calculate the parital equilibrium price for good 1
print "Capital used in the sector 1: ",
print k1(demandM(p1),p1,p2,tm)
print "Government revenue: ",
print govRev(p1)
print "Welfare loss for rich household: ",
print welfareloss(richD,p1,tm,share_r)
print "Welfare loss for poor household: ", 
print welfareloss(poorD,p1,tm,share_p)

xr1_o=richD(p0)
xr2_o=richD2(p0)
xr1_n=richD(p1)
xr2_n=richD2(p1)
xp1_o=poorD(p0)
xp2_o=poorD2(p0)
xp1_n=poorD(p1)
xp2_n=poorD2(p1)
ir_n=pk*k_rich+share_r*govRev(p1)
ip_n=pl*l_poor+share_p*govRev(p1)

print "EV for rich ", ev_rich(xr1_n,xr2_n,xr1_o,xr2_o,ir)
print "CV for Rich ", cv_rich(xr1_n,xr2_n,xr1_o,xr2_o,ir_n)
print "EV for poor ", ev_poor(xp1_n,xp2_n,xp1_o,xp2_o,ip)
print "CV for poor ", cv_poor(xp1_n,xp2_n,xp1_o,xp2_o,ip_n)


