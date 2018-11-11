#6150-Algorithms Project
##Paper: Maximizing the spread of influence through a social network.
###Team Members: Sonika Jindal, Anupama Goparaju

###Algorithmic Problem:
The paper discusses the problem of selecting the most influential set of individuals who can trigger a cascade of influence in the network for further adoption. This helps in propagation of ideas which has various applications for example during elections, or adoption of some medicine in medicine community. So, it is important to select the initial set of individuals. To propagate the idea they mention the network diffusion process. The optimization problem of selecting most influential individuals is NP-Hard and is studied extensively for innovations, marketing strategies and product launches.

###Algorithmic Approach:
As per our understanding there are two main problems they are considering:
1.     Finding the initial set of influential individuals: This is key because the right set of individuals will have the highest amount of influence. The authors use 4 different ways of selecting the initial set of nodes:
a.     Greedy
b.     High Degree
c.     Central
d.     Random
2.     Diffusion of idea: Once the initial set is ready, the idea can be propagated using two different diffusion models:
a.     Linear Threshold
b.     Independent Cascade
Using the above steps, they are trying to reason about the performance guarantees based upon the submodular functions. They have proved that for an arbitrary instance of Independent Cascade model as well as the Linear Threshold model, the resulting influence function is submodular.
As per their evaluation, Greedy solution’s performance is within 63% of optimal solution. The heuristics of the greedy algorithm has been compared with the commonly used heuristics such as high-degree, distance-centrality and random selection.

###Our Approach:
We would consider few publicly available network data sets and implement the greedy approach and diffusion models discussed in the paper and compare the performance of these algorithms. The possible pitfall here is finding the optimal solution is NP-Hard and we may have to use random selection of nodes in the network for comparison.
Tasks which we plan to do:
1.     Implement the diffusion models presented in the paper and run it with different datasets and see the spread
2.     Come up with different heuristics and implement them. Then compare the spread with these heuristics. Below are are the heuristics that we can try:
Betweenness centrality of a vertex is the number of shortest paths that pass through a given vertex.
Degree discount is when a vertex k is picked in the influential set of nodes, for the next vertex j being picked, if j is a neighbor of k, the edge kj is not counted.

 


