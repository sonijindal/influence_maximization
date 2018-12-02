import networkx as nx

from generateProbability  import degreeHeuristic, fixedHeuristic, distanceHeuristic, weightHeuristic 
from generalGreedy import generalGreedy, runIC

import os

def parseDataset(name, flag):
    # read in graph
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
    #calculate initial set
    edgeProb = degreeHeuristic(GU, seed_size);
    S=generalGreedy(GU, seed_size, edgeProb);

    # write results S to file
    with open('seed_set.txt', 'w') as f:
        f.write('Degree Probability: seed size:', seed_size, ':\n')
        for node in S:
            f.write(str(node) + os.linesep)
    
    # calculate average activated set size
    iterations = 1 # number of iterations
    avg = 0
    for i in range(iterations):
        T = runIC(GU, S, edgeProb)
        avg += float(len(T))/iterations

    print ('Degree Probability: Seed_size:', seed_size,' Avg. Targeted', int(round(avg)), 'nodes out of', len(GU))

def fixedProb(seed_size):
    #calculate initial set
    edgeProb = fixedHeuristic(GU, seed_size);
    S=generalGreedy(GU, seed_size, edgeProb);

    # write results S to file
    with open('seed_set.txt', 'w') as f:
        f.write('Fixed Probability: seed size:', seed_size, ':\n')
        for node in S:
            f.write(str(node) + os.linesep)

    # calculate average activated set size
    iterations = 1 # number of iterations
    avg = 0
    for i in range(iterations):
        T = runIC(GU, S, edgeProb)
        avg += float(len(T))/iterations
    print ('Fixed Probability: Seed_size:', seed_size,' Avg. Targeted', int(round(avg)), 'nodes out of', len(GU))

def distanceProb(seed_size):
    #calculate initial set
    S, edgeProb = distanceHeuristic(GW, seed_size);

    # write results S to file
    with open('seed_set.txt', 'w') as f:
        f.write('Distance Probability: seed size:' + str(seed_size) +  ':\n')
        for node in S:
            f.write(str(node) + os.linesep)

    # calculate average activated set size
    iterations = 1 # number of iterations
    avg = 0
    for i in range(iterations):
        T = runIC(GW, S, edgeProb)
        avg += float(len(T))/iterations
    print ('Degree Probability: Seed_size:', seed_size,' Avg. Targeted', int(round(avg)), 'nodes out of', len(GW))


def weightProb(seed_size):
    #calculate initial set
    edgeProb = weightHeuristic(GW, seed_size);
    S=generalGreedy(GW, seed_size, edgeProb);

    # write results S to file
    with open('seed_set.txt', 'w') as f:
        f.write('Weight Probability: seed size:', seed_size, ':\n')
        for node in S:
            f.write(str(node) + os.linesep)

    # calculate average activated set size
    iterations = 1 # number of iterations
    avg = 0
    for i in range(iterations):
        T = runIC(GW, S, edgeProb)
        avg += float(len(T))/iterations
    print ('Weight Probability: Seed_size:', seed_size,' Avg. Targeted', int(round(avg)), 'nodes out of', len(GW))

if __name__ == '__main__':
    import time
    start = time.time()
    GU = parseDataset('facebook_combined.txt', 'un')
    GW = parseDataset('soc-sign-bitcoinalpha.csv', 'weighted')
    seed_size = 5
    while seed_size <= 5:
        degreeProb(seed_size)
        #fixedProb(seed_size)
        #distanceProb(seed_size)
        #weightProb(seed_size)
        seed_size += 5

    console = []