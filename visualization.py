import networkx as nx
import matplotlib.pyplot as plt
import json
import os


def create_graph(data):
    """
    Creates a networkx graph from the urls.
    """
    plot_values = []
    # Get all the values 
    for k, v in data.items():
        for link in v:
            # create tuples with links connected to the "parent link"
            plot_values.append((k, link, 1))

    G = nx.DiGraph()
    # add the values(tuples) to be plotted
    G.add_weighted_edges_from(plot_values)

    # Create network
    nx.draw_networkx(G, node_color= "Blue", node_size= 3, width= 0.05, arrows= False,with_labels= False)
    
    # Plot
    plt.axis('off')
    plt.show()