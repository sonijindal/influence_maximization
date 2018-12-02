from priorityQueue import PriorityQueue as PQ

def generalGreedy(G, k, edgeProb):
    import time
    start = time.time()
    R = 20 # number of times to run Random Cascade
    S = [] # set of selected nodes
    # add node to S if achieves maximum propagation for current chosen + this node
    for i in range(k):
        s = PQ() # priority queue
        for v in G.nodes():
            if v not in S:
                s.add_task(v, 0) # initialize spread value
                for j in range(R): # run R times Random Cascade
                    [priority, count, task] = s.entry_finder[v]
                    s.add_task(v, priority - float(len(runIC(G, S + [v], (edgeProb[v]/max(edgeProb.values())))))/R) # add normalized spread value
        task, priority = s.pop_item()
        S.append(task)
    return S

def runIC (G, S, edgeProb):

    from copy import deepcopy
    from random import random
    T = deepcopy(S) # copy already selected nodes

    i = 0
    while i < len(T):
        for v in G[T[i]]: # for neighbors of a selected node
            if v not in T: # if it wasn't selected yet
                w = G[T[i]][v]['weight'] # count the number of edges between two nodes
                print(T[i])
                print(edgeProb[T[i] + 1])
                #if random() <= 1 - (1-(edgeProb[int(T[i])]/max(edgeProb.values())))**w: # if at least one of edges propagate influence
                    #print (T[i], 'influences', v)
                  #  T.append(v)
        i += 1
    return T