from priorityQueue import PriorityQueue as PQ

def generalGreedy(G, k, edgeProb, flag='N'):
    import time
    start = time.time()
    R = 5 
    S = []
    for i in range(k):
        s = PQ() 
        for v in G.nodes():
            if v not in S:
                s.add_task(v, 0) 
                for j in range(R):
                    [priority, count, task] = s.entry_finder[v]
                    s.add_task(v, priority - float(len(runIC(G, S + [v], edgeProb, flag)))/R) # add normalized spread value
        task, priority = s.pop_item()
        S.append(task)
    return S

def runIC (G, S, edgeProb, flag='N'):
    from copy import deepcopy
    from random import random
    T = deepcopy(S) 

    i = 0
    while i < len(T):
        for v in G[T[i]]: 
            if v not in T: 
                w = G[T[i]][v]['weight'] 
                if(flag=='Y'):
                    val=(edgeProb[T[i]] + edgeProb[v])/2;
                    maxval=max(edgeProb.values());
                    p=val/maxval;
                else:
                    p=edgeProb[T[i]];
                if random() <= 1 - (1-p)**w: 
                    T.append(v)
        i += 1
    return T