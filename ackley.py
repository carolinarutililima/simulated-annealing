
import math
import matplotlib.pyplot as plt
from ypstruct import structure # encapsulates variables 
import sim_annel 

from codetiming import Timer




# def function to optimize ackley fun
def function(x):
    D = 30
    cosx = 0
    listcos = []
    listquad = []
    for i in x:
        cosx = math.cos(2*math.pi*i) 
        listcos.append(cosx)
        listquad.append(i**2)
    sumcos = sum(listcos) 
    sumx = sum(listquad)    
    p1 = -0.2* math.sqrt(1/D * sumx)
    p2 = 1/D *  sumcos  
    fun = 20 + math.exp(1) - 20*math.exp(p1) - math.exp(p2)
    return fun




# Variables according to problem definition
problem = structure()
problem.costfunc = function
problem.varmin = - 32 # -32
problem.varmax = 32 # 32
problem.nv = 30 # variable number



# Simulated Annealing parameters
params = structure()
params.maxit = 100000 # max iterations number
params.accep = 0.1 # acceptance for stop the alg
params.ini_temp = 200 # initial temperature
params.cooling = 0.9 # cooling
params.no_attempts =  200



#Run Simulated Annealing
t = Timer(name="class")
t.start()
output = sim_annel.run(problem, params)
t.stop()


# Results  
plt.plot(output.bestcost, 'b', linewidth = 3, label="Ackley")
plt.legend() 
plt.semilogy(output.bestcost)
plt.xlim(0,output.it)
plt.xlabel('Iterations')
plt.ylabel('Output')
plt.title('S. Annealing Algorithm')
plt.show()