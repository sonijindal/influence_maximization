import networkx as nx

from generateProbability  import degreeHeuristic, fixedHeuristic, distanceHeuristic, weightHeuristic, degreeHeuristicSeed
from generalGreedy import generalGreedy, runIC

import os

def parseDataset(name, flag):
    G = nx.Graph()
    with open(name) as f:
        if(flag=='weighted'):
            n, m, w = f.readline().split(',');
        else:
            n,m=f.readline().split();
        for line in f:
            if(flag=='weighted'):
                u, v, w = map(int, line.split(','))
            else:
                u,v=map(int, line.split());
            try:
                if(flag=='weighted'):
                    G[u][v]['weight'] += w;
                else:
                    G[u][v]['weight']+=1;
            except:
                if(flag=='weighted'):
                    G.add_edge(u,v, weight=w);
                else:
                    G.add_edge(u,v,weight=1);
    print ('Built graph G')
    return G

def degreeProb(seed_size):
    edgeProb = degreeHeuristic(GU);
    S=generalGreedy(GU, seed_size, edgeProb, 'Y');
    iterations = 200 
    avg = 0
    for i in range(iterations):
        T = runIC(GU, S, edgeProb)
        avg += float(len(T))/iterations

    print ('Degree Probability: Seed_size:', seed_size,' Avg. Targeted', int(round(avg)), 'nodes out of', len(GU))

    return S, int(round(avg))

def fixedProb(seed_size):
    edgeProb = fixedHeuristic(GU);
    S=generalGreedy(GU, seed_size, edgeProb);
    iterations = 200 
    avg = 0
    for i in range(iterations):
        T = runIC(GU, S, edgeProb)
        avg += float(len(T))/iterations
    print ('Fixed Probability: Seed_size:', seed_size,' Avg. Targeted', int(round(avg)), 'nodes out of', len(GU))
    return S, int(round(avg))

def distanceProb(seed_size):
    S, edgeProb = distanceHeuristic(GU, seed_size);
    iterations = 200 
    avg = 0
    for i in range(iterations):
        T = runIC(GU, S, edgeProb)
        avg += float(len(T))/iterations
    print ('Distance Probability: Seed_size:', seed_size,' Avg. Targeted', int(round(avg)), 'nodes out of', len(GU))
    return S, int(round(avg))


def weightProb(seed_size):
    edgeProb = weightHeuristic(GU);
    S=generalGreedy(GU, seed_size, edgeProb);
    iterations = 200 
    avg = 0
    for i in range(iterations):
        T = runIC(GU, S, edgeProb, 'Y')
        avg += float(len(T))/iterations
    print ('Weight Probability: Seed_size:', seed_size,' Avg. Targeted', int(round(avg)), 'nodes out of', len(GU))
    return S, int(round(avg))

if __name__ == '__main__':
    import time
    start = time.time()
    GU = parseDataset('small_graph.txt', 'un')
    #GW = parseDataset('soc-sign-bitcoinalpha.csv', 'weighted')
    seed_size = 5
    sizes=[];
    degreeSpread=[];
    fixedSpread=[];
    distanceSpread=[];
    weightSpread=[];

    while seed_size <= 10:
        print('.................................................................................................................')
        seed_sets=[];
        sizes.append(seed_size);
        
        S, spread=degreeProb(seed_size)
        seed_sets.append(S);
        degreeSpread.append(spread);

        S,spread=fixedProb(seed_size)
        seed_sets.append(S);
        fixedSpread.append(spread);
        
        S,spread=distanceProb(seed_size)
        seed_sets.append(S);
        distanceSpread.append(spread);

        S,spread=weightProb(seed_size)
        seed_sets.append(S);
        weightSpread.append(spread);

        seed_size += 5
        result = set(list(seed_sets[0]))
        for s in seed_sets[1:]:
            result.intersection_update(s)
        print("Instersection set of different edge probabilities for the Seed_Size: ",seed_size, result)
        print('.................................................................................................................')

    import matplotlib.pyplot as plt

    X  = sizes;
    Y1 = degreeSpread;
    Y2 = fixedSpread;
    Y3 = distanceSpread;
    Y4 = weightSpread;

    fig = plt.figure()
    ax=plt
    line1, =ax.plot(X,Y1,dashes=[6, 2], label='High Degree Heuristic')
    line2=ax.plot(X,Y2,dashes=[6, 2], label='Fixed Probability Heuristic')
    line3=ax.plot(X,Y3,dashes=[6, 2], label='Distance Heuristic')
    line4=ax.plot(X,Y4,dashes=[6, 2], label='Weights Heuristic')
    ax.legend();
    plt.show()

    plt.title('Influence of probability on the maximum spread')
    console = []