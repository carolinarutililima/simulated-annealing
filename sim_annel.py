import random
import math
import numpy as np
from ypstruct import structure



def run(problem, params):

    #Problem definition 
    costfunc = problem.costfunc
    varmin = problem.varmin
    varmax = problem.varmax
    nv = problem.nv
    bounds = [varmin, varmax]
    
    
    
    # Parameters 
    maxit = params.maxit # max iterations number
    accep = params.accep # acceptance for stop the alg
    ini_temp = params.ini_temp  # initial temperature
    cooling = params.cooling  # cooling rate
    no_attempts =  params.no_attempts # attempts number to get a new solution


    initial_solution = np.zeros(nv)
    for v in range(nv):
        initial_solution[v] = random.uniform(bounds[0], bounds[1])
        
        
    current_solution = initial_solution
    best_solution = initial_solution
    best_fitness = costfunc(best_solution)
    T = ini_temp
    record_best_fitness = []


    it = 0
    
    while best_fitness > accep and maxit > it:
       
        for j in range(no_attempts):
            
            for k in range(nv):
                    
    
                current_solution[k] = best_solution[k] +  0.1 * nv * (random.uniform(bounds[0], bounds[1]))
    
    
                if current_solution[k] > bounds[1]:
                        current_solution[k] = bounds[1]
                if current_solution[k] < bounds[0]:
                        current_solution[k] = bounds[0]
                        
        
            current_fitness = costfunc(current_solution)
            E = current_fitness - best_fitness
            
    
            if  E < 0 : 
                
                accept = True
            
            else:
                   
                p = math.exp(-E/T)
    
                #make a decision to accept the worse solution or not
                if random.random() < p:
                    accept = True
                else:
                    accept = False
                
        
            if accept == True:
                
                best_solution =  current_solution
                best_fitness = costfunc(best_solution)
            
        
        print( "Iteration {}: best output/cost = {}".format(it, best_fitness))
    
        record_best_fitness.append(best_fitness)
        
        #cooling the temperature
        T = T*cooling
        
        it = it + 1
        
    output = structure()
    output.bestcost = record_best_fitness
    output.it = it
    
    return output 

        
                
                      
                
    
    
    
        