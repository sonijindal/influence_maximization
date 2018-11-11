# 6150-Algorithms Project
## Maximizing the spread of influence through a social network.
### Team Members: Sonika Jindal, Anupama Goparaju
### Mid point update - 11/16/2018
================================================================================================
#### Algorithmic Problem:
The paper discusses the problem of selecting the most influential set of individuals who can trigger a cascade of influence in the network for further adoption. This helps in propagation of ideas which has various applications for example during elections, or adoption of some medicine in medicine community. So, it is important to select the initial set of individuals. To propagate the idea they mention the network diffusion process. The optimization problem of selecting most influential individuals is NP-Hard and is studied extensively for innovations, marketing strategies and product launches.

#### Algorithmic Approach:
As per our understanding there are two main problems they are considering:
1.     Finding the initial set of influential individuals: This is key because the right set of individuals will have the highest amount of influence. The authors use 4 different ways of selecting the initial set of nodes:
  1. Greedy
  2. High Degree
  3. Central
  4. Random
2.     Diffusion of idea: Once the initial set is ready, the idea can be propagated using two different diffusion models:
  1. Linear Threshold
  2. Independent Cascade

Using the above steps, they are trying to reason about the performance guarantees based upon the submodular functions. They have proved that for an arbitrary instance of Independent Cascade model as well as the Linear Threshold model, the resulting influence function is submodular.
As per their evaluation, Greedy solution’s performance is within 63% of optimal solution. The heuristics of the greedy algorithm has been compared with the commonly used heuristics such as high-degree, distance-centrality and random selection.

#### Independent Cascade Model:

The diffusion model of Independent Cascade runs in discrete steps. At the beginning, few nodes are selected to be seed nodes. These nodes become active in the very beginning.
After this, in each discrete step, an active node tries to influence one of its inactive neighbors. Every node is given only one chance to activate the same inactive neighbor. 
The success depends on the propagation probability of the edge between these two nodes. Propagation Probability defines how much one node can influence the other node.
In reality, Propagation Probability is dependent on various factors like level of friendship, business relations etc. This will result in different values for each edge.
However, for the experimental purposes in most evaluations, it is often considered to be same for all edges.

#### Our Approach:

In this project, we will work on analysing Independent Cascade (IC) model based upon different diffusion probabilities.
Apart from the initial seed node, the IC model is dependent on the probability values
associated with the edges in the graph. That is the diffusion probability of each link in the graph must be specified in advance for the spread to happen.
However, it is usually difficult to determine the probabilities in advance.
There have been some work in this area to predict the probabilities:

[Learning Diffusion Probability Based on Node Attributes in Social Networks](https://link.springer.com/chapter/10.1007/978-3-642-21916-0_18)

[Learning influence probabilities in social networks](https://dl.acm.org/citation.cfm?id=1718518)

[Learning Influence Diffusion Probabilities under the Linear Threshold Model](https://www.cs.ubc.ca/~sharanv/social_networks_report.pdf)

[Prediction of Information Diffusion Probabilities for Independent Cascade Model](https://link.springer.com/chapter/10.1007/978-3-540-85567-5_9)

The goal of this project is to see the effects of different probabilities on the spread of influence. We will perform the following steps:

1. Seed selection based upon random and greedy heuristics. We call these sets: influential\_set\_random and influenctial\_set\_greedy
2. Call IndependentCascade with influential\_set\_random as Seed and Probability = 0.1, 0.2, 0.3, 0.4 and 0.5
3. Call IndependentCascade with influential\_set\_greedy as Seed and Probability = 0.1, 0.2, 0.3, 0.4 and 0.5

IndependentCascade(Graph, Seed, Probability)
1. Define Final\_set, and copy all nodes from Seed to Final\_set
2. For each node(node\_i) in Final\_set, repeat steps 3 to 5
3. For all the neighbors of the node\_i, repeat steps 4 and 5
4. Generate a random number, num
5. If num < p, then add node\_i to Final\_set
6. The set Final\_set, contains the final outcome after the diffusion is complete.


