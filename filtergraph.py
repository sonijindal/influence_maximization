import networkx as nx
from priorityQueue import PriorityQueue as PQ

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

def degreeHeuristicSeed(G, k):
    S = []
    d = PQ()
    for u in G:
        degree = sum([1 for v in G[u] if G[u][v]['weight']])
        # degree = len(G[u])
        d.add_task(u, -degree)
    for i in range(k):
        u, priority = d.pop_item()
        S.append(u)
    return S



if __name__ == '__main__':
    import time
    start = time.time()
    GU = parseDataset('graph.csv', 'weighted')
    # G=parseDataset('public_graph.txt', 'un')
    # print(nx.info(G));
    listofsubnodes=[];
    S=degreeHeuristicSeed(GU, 800);
    f=open('public_graph.txt', 'w');
    with open("graph.csv","r") as fi:
        for i in range(770, len(S)):
            for ln in fi:
                if ln.startswith(str(S[i])):
                    val=ln.split(',');
                    for j in range(0,int(val[2].rstrip())):
                        c=str(S[i])+' '+str(val[1])+'\n';
                        f.write(c);
                    if(int(val[2]) not in listofsubnodes and int(val[2]) not in S):
                        listofsubnodes.append(int(val[1]));
            fi.seek(0);
    print(listofsubnodes);
    with open("graph.csv","r") as fi:
        for i in range(0, len(listofsubnodes)):
            for ln in fi:
                if ln.startswith(str(listofsubnodes[i])):
                    val=ln.split(',');
                    for j in range(0,int(val[2].rstrip())):
                        c=str(listofsubnodes[i])+' '+str(val[1])+'\n';
                        f.write(c);

            fi.seek(0);




