# Filename: parameters.py
# Author: Ken Chow
# This file contains global parameters and the definitions of all the relevant 
# functions for the implementation of the applied general equilibrium 
# model outlined in Shoven and Whalley (1984)

# global parameters
k_rich=25 # rich endowment of capital
l_poor=60 # poor endowment of labour
delta_1=0.6  # subscript 1 denotes manufacturing and 2 denotes non-manufacturing
delta_2=0.7
sigma_1=2.0
sigma_2=0.5
sigma_rich=1.5
sigma_poor=0.75
alpha_rich_1=0.5
alpha_rich_2=0.5
alpha_poor_1=0.3
alpha_poor_2=0.7
phi_1=1.5
phi_2=2.0
share_r=0.4
share_p=0.6

#sigma_1=0.1   # uncomment these parameters for last part of the assignment
#sigma_2=2.4
#alpha_rich_1=0.3
#alpha_rich_2=0.7
#alpha_poor_1=0.5
#alpha_poor_2=0.5


def q1(l,k): # production function for the manufacturoing good
	rho=(sigma_1-1)/sigma_1	
	q=phi_1*(delta_1*l**rho+(1-delta_1)*k**rho)**(1/rho)
	return q
def q2(l,k): # production function for the non-manufacturoing good
	rho=(sigma_2-1)/sigma_2	
	q=phi_2*(delta_2*l**rho+(1-delta_2)*k**rho)**(1/rho)
	return q

#print q1(25.999,4.039) # sanity check
#print q2(34.001,20.961) # sanity check

def l1(q,pk,pl,t_k=0.0): # labour demand for manufacturing good
	pk=pk*(1+t_k)
	rho=(1-sigma_1)/sigma_1
	l=(1/phi_1)*q*(delta_1+(1-delta_1)*(delta_1*pk/((1-delta_1)*pl))**(1-sigma_1))**(1/rho)
	return l

def l2(q,pk,pl,t_k=0): # labour demand for non-manufacturing good
	pk=pk*(1+t_k)
	rho=(1-sigma_2)/sigma_2
	l=(1/phi_2)*q*(delta_2+(1-delta_2)*(delta_2*pk/((1-delta_2)*pl))**(1-sigma_2))**(1/rho)
	return l


#print l1(22.387,1.128,1.0,0.5)
#print l2(57.307,1.128,1.0,0)

def k1(q,pk,pl,t_k=0): # capital demand for the manufacturing good
	pk=pk*(1+t_k)
	rho=sigma_1/(1-sigma_1)
	k=(1/phi_1)*q*(delta_1*((1-delta_1)*pl/(delta_1*pk))**(1-sigma_1)+(1-delta_1))**rho
	return k

def k2(q,pk,pl,t_k=0): # capital demand for the manufacturing good
	pk=pk*(1+t_k)
	rho=sigma_2/(1-sigma_2)
	k=(1/phi_2)*q*(delta_2*((1-delta_2)*pl/(delta_2*pk))**(1-sigma_2)+(1-delta_2))**rho
	return k

#print k1(22.387,1.128,1.0,0.5)
#print k2(57.307,1.128,1.0,0)

def x_rich_1(i,p1,p2): # demand for manfacturing good for the rich
	x=alpha_rich_1*i/(p1**sigma_rich*(alpha_rich_1*p1**(1-sigma_rich)+alpha_rich_2*p2**(1-sigma_rich)))
	return x

def x_poor_1(i,p1,p2): # demand for manfacturing good for the poor
	x=alpha_poor_1*i/(p1**sigma_poor*(alpha_poor_1*p1**(1-sigma_poor)+alpha_poor_2*p2**(1-sigma_poor)))
	return x

#print x_rich_1(29.102,1.467,1.006)
#print x_poor_1(61.367,1.467,1.006)

def x_rich_2(i,p1,p2): # demand for non-manufacturing good for the rich
	x=alpha_rich_2*i/(p2**sigma_rich*(alpha_rich_1*p1**(1-sigma_rich)+alpha_rich_2*p2**(1-sigma_rich)))
	return x

def x_poor_2(i,p1,p2): # demand for non-manufacturing good for the rich
	x=alpha_poor_2*i/(p2**sigma_poor*(alpha_poor_1*p1**(1-sigma_poor)+alpha_poor_2*p2**(1-sigma_poor)))
	return x

#print x_rich_2(29.102,1.467,1.006)
#print x_poor_2(61.367,1.467,1.006)

def income_r(pk,pl,q1,q2,t_1=0,t_2=0): #income for rich household
	income=pk*k_rich+share_r*(t_1*pk*k1(q1,pk,pl,t_1)+t_2*pk*k2(q1,pk,pl,t_2))
	return income

def income_p(pk,pl,q1,q2,t_1=0,t_2=0): #income for poor household
	income=pl*l_poor+share_p*(t_1*pk*k1(q1,pk,pl,t_1)+t_2*pk*k2(q1,pk,pl,t_2))
	return income

#print income_r(1.373,1,24.942,54.378,0,0)
#print income_p(1.373,1,24.942,54.378,0,0)
#print income_r(1.128,1,22.387,57.307,0.5,0)
#print income_p(1.128,1,22.387,57.307,0.5,0)

def utility_rich(x1,x2): #utility function for rich household
	rho=(sigma_rich-1)/sigma_rich
	u=(alpha_rich_1**(1/sigma_rich)*x1**rho+alpha_rich_2**(1/sigma_rich)*x2**rho)**(1/rho)
	return u

def utility_poor(x1,x2): #utility function for poor household
	rho=(sigma_poor-1)/sigma_poor
	u=(alpha_poor_1**(1/sigma_poor)*x1**rho+alpha_poor_2**(1/sigma_poor)*x2**rho)**(1/rho)
	return u

def ev_rich(x1_n,x2_n,x1,x2,i_o): #equivalent variation
	e=(utility_rich(x1_n,x2_n)-utility_rich(x1,x2))*i_o/utility_rich(x1,x2)
	return e

def cv_rich(x1_n,x2_n,x1,x2,i_n):
	e=(utility_rich(x1_n,x2_n)-utility_rich(x1,x2))*i_n/utility_rich(x1_n,x2_n)
	return e

def ev_poor(x1_n,x2_n,x1,x2,i_o): #equivalent variation
	e=(utility_poor(x1_n,x2_n)-utility_poor(x1,x2))*i_o/utility_poor(x1,x2)
	return e

def cv_poor(x1_n,x2_n,x1,x2,i_n):
	e=(utility_poor(x1_n,x2_n)-utility_poor(x1,x2))*i_n/utility_poor(x1_n,x2_n)
	return e

