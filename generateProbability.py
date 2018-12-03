import networkx as nx

from priorityQueue import PriorityQueue as PQ # priority queue class

def degreeHeuristic(G):
    edgeProb={};
    for u in G:
        degree = sum([G[u][v]['weight'] for v in G[u]])
        edgeProb[u]=degree;
    return edgeProb

def degreeHeuristicSeed(G, k):
    S = []
    d = PQ()
    for u in G:
        degree = sum([G[u][v]['weight'] for v in G[u]])
        # degree = len(G[u])
        d.add_task(u, -degree)
    for i in range(10):
        u, priority = d.pop_item()
        S.append(u)
    return S

def fixedHeuristic(G):
    edgeProb={};
    for u in G:
        edgeProb[u]=0.5;
    return edgeProb

def weightHeuristic(G):
    edgeProb={};
    for u in G:
        edgeProb[u]=sum([G[u][v]['weight'] for v in G[u]])
    return edgeProb

def _sumDist (G, S, no):
    cum = 0
    for u in S:
        try:
            cum += G[no][u]['weight']
        except:
            pass
    return cum

def distanceHeuristic(G, k):
    S = [] # set of chosen nodes
    S_dist = PQ() # distances from each node in G to set S according to metric
    edgeProb={}
    # initialize S with furthest vertices
    try:
        u,v,d = max(G.edges(data=True), key=lambda item: item[2]['weight'])
    except KeyError:
        print('Most likely you have no weight attribute')
    S.extend([u,v])
    
    # compute distances from each node in G to S
    for v in G.nodes():
        if v not in S: # calculate only for nodes in G
            S_dist.add_task(v, - _sumDist(G, S, v)) # take minus to pop the maximum value from priority queue

    # add new nodes to the set greedily
    while len(S) < k:
        u, priority = S_dist.pop_item() # find maximum value of distance to set S
        S.append(u) # append that node to S

        # only increase distance for nodes that are connected to u
        for v in G[u].keys():
            if v not in S: # add only remained nodes
                [priority, count, task] = S_dist.entry_finder[v] # finds distance for the previous step
                try:
                    S_dist.add_task(v, priority-G[u][v]['weight']) # adds distance to the new member of S
                except:
                    print('These are vertices that caused the problem:', u, v)

    for u in G.nodes():
        edgeProb[u]=_sumDist(G, S, u);
    
    return S, edgeProb