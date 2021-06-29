import numpy as np 
import matplotlib.pyplot as plt
from ypstruct import structure
import sim_annel 


from codetiming import Timer


# def function to optimize quadract fun
def function(x):
    summ = 0
    lst_summ = []
    for i in x:
        summ = summ + i
        quad = summ ** 2
        lst_summ.append(quad)
    
    y = sum(lst_summ)
    
    return y


# Variables according to problem definition
problem = structure()
problem.costfunc = function
problem.varmin = - 100 # -100
problem.varmax = 100 # 100
problem.nv = 5 # variable number




# Simulated Annealing parameters
params = structure()
params.maxit = 100000 # max iterations number
params.accep = 1 # acceptance for stop the alg
params.ini_temp = 200 # initial temperature
params.cooling = 0.9 # cooling
params.no_attempts =  1000


#Run Simulated Annealing
t = Timer(name="class")
t.start()
output = sim_annel.run(problem, params)
t.stop()

# Results  
plt.plot(output.bestcost, 'g', linewidth = 3, label="Quadratic")
plt.legend()
plt.semilogy(output.bestcost)
plt.xlim(0,output.it)
plt.xlabel('Iterations')
plt.ylabel('Output')
plt.title('S. Annealing Algorithm')
plt.show()
    