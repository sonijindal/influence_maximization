import networkx as nx
import random
import os

def genGraph (n,m,fname='',p=.75,mw=5):
    G = nx.dense_gnm_random_graph(n,m)
    for e in G.edges():
        if random.random() < p:
            G[e[0]][e[1]]['weight'] = 1
        else:
            G[e[0]][e[1]]['weight'] = random.randint(2,mw)
    if fname:
        with open(fname, 'w+') as f:
            for v1,v2,edata in G.edges(data=True):
                for i in range(edata['weight']):
                    f.write('%s %s' %(v1, v2))
                    f.write('\n');

if __name__ == '__main__':
    genGraph(1000, 1000, 'small_graph_1000.txt')
    genGraph(500, 500, 'small_graph.txt')