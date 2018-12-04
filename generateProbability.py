import networkx as nx

from priorityQueue import PriorityQueue as PQ # priority queue class

def degreeHeuristic(G):
    edgeProb={};
    for u in G:
        degree = sum([1 for v in G[u] if G[u][v]['weight']])
        edgeProb[u]=degree;
    return edgeProb

def degreeHeuristicSeed(G, k):
    S = []
    d = PQ()
    for u in G:
        degree = sum([G[u][v]['weight'] for v in G[u]])
        # degree = len(G[u])
        d.add_task(u, -degree)
    for i in range(k):
        u, priority = d.pop_item()
        S.append(u)
    return S

def fixedHeuristic(G):
    edgeProb={};
    for u in G:
        edgeProb[u]=0.3;
    return edgeProb

def weightHeuristic(G):
    edgeProb={};
    for u in G:
        edgeProb[u]=sum([G[u][v]['weight'] for v in G[u]])
    return edgeProb

def randomProbHeuristic(G):
    from random import random
    edgeProb={};
    for u in G:
        edgeProb[u]=random();
    return edgeProb


def _sumDist (G, S, no):
    cum = 0
    for u in S:
        try:
            if(G[no][u]['weight']):
                cum += 1;
        except:
            pass
    return cum

def distanceHeuristic(G, S):
   
    S_dist = PQ() # distances from each node in G to set S according to metric
    edgeProb={}
    
    for u in G.nodes():
        edgeProb[u]=_sumDist(G, S, u);
    
    return edgeProb