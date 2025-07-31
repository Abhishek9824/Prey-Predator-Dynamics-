
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import odeint


#This is initial conditions
y0=[10,1]


t=np.linspace(0,50,num=1000)

#Parameters
alpha=1.1
beta=0.4
delta=0.1
gamma=0.4

#for steady state condition
#y0=[gamma/delta , alpha/beta]

params=[alpha,beta, delta, gamma]


#defining function
def sim(variables, t, params):
  #Deer population level
  x=variables[0]
  #Wolve population level

  y=variables[1]


  alpha=params[0]
  beta =params[1]
  delta=params[2]
  gamma=params[3]

  dxdt=alpha*x-beta*x*y
  dydt= delta*x*y-gamma*y

  return([dxdt, dydt])


y=odeint(sim, y0, t, args=(params,))

f,(ax1,ax2) = plt.subplots(2)

line1, = ax1.plot(t,y[:,0], color="b")



line2, = ax2.plot(t,y[:,1], color="r")

ax1.set_ylabel("Deers (hundreds)")
ax2.set_ylabel("Wolves (hundreds)")
ax2.set_xlabel("Time")

plt.show()

#steadystate: no changes in population dyanmics
#y0=[gamma\deta, aplha\beta]