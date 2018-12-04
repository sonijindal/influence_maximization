import networkx as nx

from generateProbability  import degreeHeuristic, fixedHeuristic, distanceHeuristic, weightHeuristic, degreeHeuristicSeed, randomProbHeuristic
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
    iterations = 1000 
    avg = 0
    for i in range(iterations):
        T = runIC(GU, S, edgeProb, 'Y')
        avg += float(len(T))/iterations

    print ('Degree Probability: Seed_size:', seed_size,' Avg. Targeted', int(round(avg)), 'nodes out of', len(GU))

    return S, int(round(avg))

def fixedProb(seed_size):
    edgeProb = fixedHeuristic(GU);
    S=generalGreedy(GU, seed_size, edgeProb);
    iterations = 1000 
    avg = 0
    for i in range(iterations):
        T = runIC(GU, S, edgeProb)
        avg += float(len(T))/iterations
    print ('Fixed Probability: Seed_size:', seed_size,' Avg. Targeted', int(round(avg)), 'nodes out of', len(GU))
    return S, int(round(avg))

def RandomProb(seed_size, edgeProb):
    S=generalGreedy(GU, seed_size, edgeProb);
    iterations = 1000 
    avg = 0
    for i in range(iterations):
        T = runIC(GU, S, edgeProb)
        avg += float(len(T))/iterations
    print ('Random Probability: Seed_size:', seed_size,' Avg. Targeted', int(round(avg)), 'nodes out of', len(GU))
    return S, int(round(avg))


def distanceProb(seed_size):
    S=degreeHeuristicSeed(GU, seed_size);
    edgeProb = distanceHeuristic(GU, S);
    S=generalGreedy(GU, seed_size, edgeProb,'Y');
    iterations = 1000 
    avg = 0
    for i in range(iterations):
        T = runIC(GU, S, edgeProb, 'Y')
        avg += float(len(T))/iterations
    print ('Distance Probability: Seed_size:', seed_size,' Avg. Targeted', int(round(avg)), 'nodes out of', len(GU))
    return S, int(round(avg))


def weightProb(seed_size):
    edgeProb = weightHeuristic(GU);
    S=generalGreedy(GU, seed_size, edgeProb, 'Y');
    iterations = 1000 
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
    randomSpread=[];
    distanceSpread=[];
    weightSpread=[];

    degreeSpreadTime=[];
    fixedSpreadTime=[];
    randomSpreadTime=[];
    distanceSpreadTime=[];
    weightSpreadTime=[];

    edgeProb = randomProbHeuristic(GU);
    
    while seed_size <= 30:
        print('.................................................................................................................')
        seed_sets=[];
        sizes.append(seed_size);
        
        start = time.time()
        S, spread=degreeProb(seed_size)
        seed_sets.append(S);
        degreeSpread.append(spread);
        timeTaken = time.time() - start
        degreeSpreadTime.append(timeTaken)
        print ('Degree Probability: TimeTaken:', timeTaken)

        start = time.time()
        S,spread=fixedProb(seed_size)
        seed_sets.append(S);
        fixedSpread.append(spread);
        timeTaken = time.time() - start
        fixedSpreadTime.append(timeTaken)
        print ('Fixed Probability: TimeTaken:', timeTaken)

        start = time.time()
        S,spread=RandomProb(seed_size,edgeProb)
        seed_sets.append(S);
        randomSpread.append(spread);
        timeTaken = time.time() - start
        randomSpreadTime.append(timeTaken)
        print ('Random Probability: TimeTaken:', timeTaken)

        start = time.time()
        S,spread=distanceProb(seed_size)
        seed_sets.append(S);
        distanceSpread.append(spread);
        timeTaken = time.time() - start
        distanceSpreadTime.append(timeTaken)
        print ('Distance Probability: TimeTaken:', timeTaken)

        start = time.time()
        S,spread=weightProb(seed_size)
        seed_sets.append(S);
        weightSpread.append(spread);
        timeTaken = time.time() - start
        weightSpreadTime.append(timeTaken)
        print ('Weight Probability: TimeTaken:', timeTaken)

        result = set(list(seed_sets[0]))
        for s in seed_sets[1:]:
            result.intersection_update(s)
        print("Instersection set of different edge probabilities for the Seed_Size: ",seed_size, result)
        print('.................................................................................................................')
        seed_size += 5
    # import matplotlib.pyplot as plt
    # import numpy as np
    # X  = sizes;
    # Y1 = degreeSpread;
    # Y2 = fixedSpread;
    # Y3 = randomSpread;
    # Y4 = distanceSpread;
    # Y5 = weightSpread;

    # fig = plt.figure()
    # ax=plt
    # line1, =ax.plot(X,Y1,dashes=[6, 2], label='High Degree Heuristic')
    # line2=ax.plot(X,Y2,dashes=[6, 2], label='Fixed Probability Heuristic')
    # line2=ax.plot(X,Y3,dashes=[6, 2], label='Random Probability Heuristic')
    # line3=ax.plot(X,Y4,dashes=[6, 2], label='Distance Heuristic')
    # line4=ax.plot(X,Y5,dashes=[6, 2], label='Weights Heuristic')
    # ax.legend();
    # plt.show()

    # plt.title('Influence of probability on the maximum spread')
    # n_groups = 6

    # fig, ax = plt.subplots()

    # index = np.arange(n_groups)
    # bar_width = 0.1

    # opacity = 0.9
    # error_config = {'ecolor': '0.3'}

    # rects1 = ax.bar(index, degreeSpread, bar_width,
    #             alpha=opacity, color='b',
    #             label='degree')

    # rects2 = ax.bar(index + bar_width, fixedSpread, bar_width,
    #             alpha=opacity, color='m',
    #             label='fixed')

    # rects3 = ax.bar(index + 2*bar_width, randomSpread, bar_width,
    #             alpha=opacity, color='g',
    #             label='random')

    # rects4 = ax.bar(index + 3*bar_width, distanceSpread, bar_width,
    #             alpha=opacity, color='y',
    #             label='distance')

    # rects5 = ax.bar(index + 4*bar_width, weightSpread, bar_width,
    #             alpha=opacity, color='c',
    #             label='weight')

    # ax.set_xlabel('Seed Size')
    # ax.set_ylabel('Percentage Spread')
    # ax.set_title('Percentage Spread by different heiristics')
    # ax.set_xticks((index + bar_width))
    # ax.set_xticklabels(('5', '10', '15', '20', '25', '30'))
    # ax.set_yticks([])
    # ax.legend()

    # fig.tight_layout()
    # plt.show()
    console = []