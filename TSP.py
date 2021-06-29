import math
import random
import matplotlib.pyplot as plt
import visualize_tsp





x = [0.6606, 0.5906, 0.00398, 0.9536, 0.8767, 0.9500, 0.5029, 0.9697, 0.2184, 0.2395, 0.3876, 
     0.0213, 0.7471, 0.9464, 0.1636, 0.8200, 0.1649, 0.8192, 0.8191, 0.8646]
y = [0.9695, 0.2124, 0.1367, 0.6091, 0.8148, 0.6740, 0.8274, 0.5979, 0.7148, 0.2867, 0.7041, 
     0.3429, 0.5449, 0.1247, 0.8668, 0.3296, 0.3025, 0.9392, 0.4351, 0.6768]

zipped = zip(x, y)

coords = []

for i, j in zipped: 

    coords.append((i, j))
    
    
N = len(coords)

nodes = [i for i in range(N)]

best_solution = []
best_fitness = float("Inf")
fitness_list = []



def initial_solutionRandom(nodes, best_fitness, best_solution):
    best_solution = random.sample(nodes, len(nodes))     
    best_fitness = fitness(best_solution)
    return best_solution, best_fitness
    

def initial_solutionGreedy(nodes, best_fitness, best_solution):
    """
    Greedy algorithm to get an initial solution (closest-neighbour).
    """
    cur_node = random.choice(nodes)  # start from a random node
    solution = [cur_node]

    free_nodes = set(nodes)
    free_nodes.remove(cur_node)
    while free_nodes:
        next_node = min(free_nodes, key=lambda x: dist(cur_node, x))  # nearest neighbour
        free_nodes.remove(next_node)
        solution.append(next_node)
        cur_node = next_node

    cur_fit = fitness(solution)
    if cur_fit < best_fitness:  # If best found so far, update best fitness
        best_fitness = cur_fit
        best_solution = solution
    
    fitness_list.append(cur_fit)
    
    return solution, cur_fit, best_solution

def dist(node_0, node_1):
    """
    Euclidean distance between two nodes.
    """
    coord_0, coord_1 = coords[node_0], coords[node_1]
    return math.sqrt((coord_0[0] - coord_1[0]) ** 2 + (coord_0[1] - coord_1[1]) ** 2)

def fitness(solution):
    """
    Total distance of the current solution path.
    """
    cur_fit = 0
    for i in range(N):
        cur_fit += dist(solution[i % N], solution[(i + 1) % N])
    return cur_fit

accep = 4



#cur_solution, cur_fitness, best_solution = initial_solutionGreedy(nodes, best_fitness, best_solution)

cur_solution, cur_fitness = initial_solutionRandom(nodes, best_fitness, best_solution)

visualize_tsp.plotTSP([cur_solution],coords )


T = 2
cooling = 0.99 

it = 0
maxit = 50000

while best_fitness > accep and maxit > it:
    
    
    for j in range(200): 
        


        #candidate = list(cur_solution)
        
        #l = random.randint(2, N - 1)
        #k = random.randint(0, N - l)
        #candidate[k : (k + l)] = reversed(candidate[k : (k + l)])
                
        candidate =  random.sample(nodes, len(nodes)) 
        
        candidate_fitness = fitness(candidate)

        
        E = candidate_fitness - best_fitness
        
        if  E < 0 : 
            
            accept = True
        
        else:
               
            p = math.exp(-abs(E)/T)

            #make a decision to accept the worse solution or not
            if random.random() < p:
                accept = True
            else:
                accept = False
            
    
        if accept == True:
            
            best_fitness =  candidate_fitness
            best_solution = candidate
    
    
    print( "Interation {}: best output/cost = {}".format(it, best_fitness))

    fitness_list.append(best_fitness)
    
    #cooling the temperature
    T = T*cooling
    
    it = it + 1


 
plt.plot(fitness_list, 'g', linewidth = 3 )
plt.semilogy(fitness_list)
plt.xlim(0,it)
plt.xlabel('Iterations')
plt.ylabel('Output')
plt.title('S. Annealing Algorithm TSP')
plt.show()


visualize_tsp.plotTSP([best_solution],coords )