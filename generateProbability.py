def degreeHeuristic(G, k, p=.01):
    S = []
    d = PQ()
    edgeProb={};
    for u in G:
        degree = sum([G[u][v]['weight'] for v in G[u]])
        edgeProb[u]=degree;
    return edgeProb

def fixedHeuristic(G, k, p=.01):
    S = []
    d = PQ()
    edgeProb={};
    for u in G:
        edgeProb[u]=p;
    return edgeProb

def distanceHeuristic(G, k, p=.01):
    S = []
    d = PQ()
    edgeProb={};
    for u in G:
        #TODO
        edgeProb[u]=degree;
    return edgeProb

def weightHeuristic(G, k, p=.01):
    S = []
    d = PQ()
    edgeProb={};
    for u in G:
        #TODO
        edgeProb[u]=G[u][];
    return edgeProb