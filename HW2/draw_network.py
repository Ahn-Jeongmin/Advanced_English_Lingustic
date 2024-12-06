import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Load the file
file_path = 'network_for_rating_1_2.csv'
data = pd.read_csv(file_path)

# Filter the data for weights >= 2
filtered_data = data[:300]

# Create a directed graph using NetworkX
G = nx.DiGraph()

# Add edges to the graph with weights
for _, row in filtered_data.iterrows():
    G.add_edge(row['source'], row['target'], weight=row['weight'])

#연결 중요도에 따라 그래프 노드 크기를 다르게 설정
centrality = nx.degree_centrality(G)
node_sizes = [centrality[node] * 90000 for node in G.nodes]

# Extract edge weights for line width
edge_weights = [G[u][v]['weight'] for u, v in G.edges]


# Draw the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Position nodes using the spring layout
nx.draw(
    G, 
    pos, 
    with_labels=True, 
    node_size=node_sizes, 
    node_color="lightblue", 
    font_size=10, 
    edge_color="gray", 
    width=edge_weights  # Set edge width based on weights
)
# Add edge labels for weights
edge_labels = nx.get_edge_attributes(G, 'weight')
#nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

plt.title("Graph Visualization (Weight Represented as Line Width)", fontsize=14)
plt.show()



