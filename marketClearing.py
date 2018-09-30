# Filename: marketClearing.py
# Author: Ken Chow
# Date: 29/09/2012
# This file contains definitions of all the market clearing, factors and demand definitions
# which will be used in the general equilibrium program to solve the system of coupled 
# non-linear equations.

from parameters import * # imports global parameters




def demand1(xr1,xp1,q1):
	return xr1+xp1-q1

def demand2(xr2,xp2,q2):
	return xr2+xp2-q2

def capitalCond(k1,k2,kbar):
	return k1+k2-kbar

def labourCond(l1,l2,lbar):
	return l1+l2-lbar

def profitcond1(pk,k1,pl,l1,p1,q1,t1):
	return pk*(1+t1)*k1+pl*l1-p1*q1

def profitcond2(pk,k2,pl,l2,p2,q2,t2):
	return pk*(1+t2)*k2+pl*l2-p2*q2

def x_r_1(xr1,ir,p1,p2):
	return x_rich_1(ir,p1,p2)-xr1

def x_r_2(xr2,ir,p1,p2):
	return x_rich_2(ir,p1,p2)-xr2

def x_p_1(xp1,ip,p1,p2):
	return x_poor_1(ip,p1,p2)-xp1

def x_p_2(xp2,ip,p1,p2):
	return x_poor_2(ip,p1,p2)-xp2

def cap1(kk1,q1,pk,pl,t1):
	return k1(q1,pk,pl,t1)-kk1

def cap2(kk2,q2,pk,pl,t2):
	return k2(q2,pk,pl,t2)-kk2

def lab1(ll1,q1,pk,pl,t1):
	return l1(q1,pk,pl,t1)-ll1

def lab2(ll2,q2,pk,pl,t2):
	return l2(q2,pk,pl,t2)-ll2


def income1(ir,pk,pl,q1,q2,k1,k2,t1,t2):
	return pk*k_rich+share_r*(t1*pk*k1+t2*pk*k2)-ir

def income2(ip,pk,pl,q1,q2,k1,k2,t1,t2):
	return pl*l_poor+share_p*(t1*pk*k1+t2*pk*k2)-ip
