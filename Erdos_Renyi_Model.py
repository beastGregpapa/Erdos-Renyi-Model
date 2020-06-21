import random
import matplotlib.pyplot as plt
import math
import networkx as nx
import numpy as np
from networkx.algorithms import average_clustering
from networkx.algorithms import degree_centrality, clustering
from networkx.algorithms import diameter
from networkx.generators.classic import empty_graph, path_graph, complete_graph

# -------------------------------------------------------------------------
#  Erdos-Renyi Random Graph

def quick_gnp_random_graph(n, p, seed=None):
    """"
   Return a random graph G_{n,p}.

  The G_{n,p} graph chooses each of the possible [n(n-1)]/2 edges
  with probability p.

  Which is called Erdős-Rényi graph, or binomial graph.

    Parameters:
      - `n`: the number of nodes
      - `p`: probability for edge creation
      - `seed`: seed for random number generator (default=None)

    This algorithm is of O(n+m) complexity, where m is the expected number of
    edges given as m = p * n * (n-1)/2.

    It should be faster when p is small, and
    the expected number of edges is small (sparse graph).
    """

    G = empty_graph(n)
    G.name = "quick_gnp_random_graph(%s,%s)" % (n, p)

    if not seed is None:
        random.seed(seed)

    # Nodes in graph are from 0, n-1 (this is the second node index).
    i = 1
    j = -1
    lp = math.log(1.0 - p)

    while i < n:
        lr = math.log(1.0 - random.random())
        j = j + 1 + int(lr / lp)
        while j >= i and i < n:
            j = j - i
            i = i + 1
        if i < n:
            G.add_edge(i, j)
    return G


# accepting input from the user
nodes = int(input("please input the number of the nodes   "))
probability = float(input("please input the number of the probability   "))

# drawing the graph of Erdős Renyi
Erdős = quick_gnp_random_graph(nodes, probability)
# Reading input data from oregon2_010407.txt file
internet_graph = nx.read_edgelist("oregon2_010407.txt")

# print(type(G))
# G.number_of_edges()
# print("number of edges of internet_graph is:   "internet_graph.number_of_edges())
# G.number_of_nodes()
# print("number of nodes of internet_graph is:  "internet_graph.number_of_nodes())

# showing number of nodes, edges and average degree of internet graph
print("internet_Graph info: ", nx.info(internet_graph))
print("Erdos Graph info: ", nx.info(Erdős))

# checking if the graph is directed or undirected
print("is internet graph directed?", (nx.is_directed(internet_graph)))
print("is erdős graph directed?", (nx.is_directed(Erdős)))

# diameter(G, e=None)
# degree_centrality(G)
# For average degree: #_edges * 2 / #_nodes;
# comparing average_clustering of both graphs
# print(average_clustering(internet_graph),(average_clustering(Erdős)))

# compute average clustering for the graphs
print("Average clustering of Internet_graph is: ", average_clustering(internet_graph),
      "\nAverage clustering of Erdos graph is:  ", average_clustering(Erdős))

print("Transitivity of internet is: ", nx.transitivity(internet_graph), "\nTransitivity of Erdos is: ",
      nx.transitivity(Erdős))

# compute clustering of the graphs
print("clustering of Internet_graph is ", clustering(internet_graph), "clustering of Erdos graph is  ", clustering(Erdős))

# compute Degree_centrality for nodes
print("Degree_centrality of Internet_graph is : ", degree_centrality(internet_graph), "\nDegree_centrality of Erdos graph is:  ", degree_centrality(Erdős))


# compute Diameter of the Graphs
print("Diameter of Erdos graph is:  ", diameter(Erdős), "\nDiameter of Internet Graph is : ", diameter(internet_graph))
# print ("diameter of erdos is ",nx.diameter(Erdős))

# Drawing Erdős graph according to the users input
nx.draw(Erdős, with_labels=True)
plt.show()

# Drawing Internet_graph with 10981 nodes and 30855 edges
nx.draw(internet_graph, with_labels=True)
plt.show()


