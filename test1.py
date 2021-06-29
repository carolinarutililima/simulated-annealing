import time
import random
import math
import numpy as np
import matplotlib.pyplot as plt

initial_temperature = 100
cooling = 0.7
number_variables = 2
upper_bounds = [3,3]
lower_bounds = [-3,-3]
computing_time = 0.3


def objective_function(X):
    x = X[0]
    y = X[1]
    
    value = x*y
    
    return value

initial_sulution = np.zeros(number_variables)
for v in range(number_variables):
    initial_sulution[v] = random.uniform(lower_bounds[v], upper_bounds[v])
    
current_solution = initial_sulution
best_solution = initial_sulution
n = 1 # no of solution accepted 
best_fitness = objective_function(best_solution)
current_temperature = initial_temperature
start = time.time()
no_attempts = 100
record_best_fitness = []

for i in range(999999):
    for j in range(no_attempts):
        
        for k in range(number_variables):
            current_solution[k] = best_solution[k] + 0.1 * (random.uniform(lower_bounds[k], upper_bounds[k]))
            current_solution[k] = max(min(current_solution[k], upper_bounds[k]), lower_bounds[k])
            
        
        current_fitness = objective_function(current_solution)
        E = abs(current_fitness - best_fitness)
        
        if i == 0  and j == 0 :
            
            EA = E
            
        if current_fitness < best_fitness:
            
            p = math.exp(-E/(EA*current_temperature))
            #make a decision to accept the worse solution or not
            if random.random()<p:
                accept = True
            else:
                accept = False
                
        else:
            accept = True
        
        if accept == True:
            best_solution =  current_solution
            best_fitness = objective_function(best_solution)
            n = n + 1 # count the solution accpeted
            EA = (EA * (n-1) + E)/n
            
    print('interation: {}, best_solution: {}, best_fitness: {}'.format(i, best_solution, best_fitness))
    record_best_fitness.append(best_fitness)
    #cooling the temperature
    current_temperature = current_temperature*cooling
    #stop by computing time
    end =  time.time()
    if end-start >= computing_time:
        break
    
plt.plot(record_best_fitness)
    
            
                  
            



    