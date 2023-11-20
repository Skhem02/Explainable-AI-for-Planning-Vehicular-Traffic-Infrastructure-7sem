import networkx as nx
import xml.etree.ElementTree as ET

# Load the existing rou.xml file
tree = ET.parse('fiftybus.rou.xml')
root = tree.getroot()

# Create a directed graph to represent possible routes and transitions
G = nx.DiGraph()

# Iterate through the vehicles and add their routes to the graph
for vehicle in root.iter('route'):
    route_edges = vehicle.attrib['edges'].split()
    for i in range(len(route_edges) - 1):
        source_edge = route_edges[i]
        destination_edge = route_edges[i + 1]
        G.add_edge(source_edge, destination_edge, weight=1)  # Assuming initial weight is 1

# Find shortest paths between all pairs of nodes (routes) and convert to dictionary
shortest_paths = dict(nx.all_pairs_dijkstra_path(G, weight='weight'))

# Update the routes for all vehicles based on shortest paths
for vehicle in root.iter('route'):
    route_edges = vehicle.attrib['edges'].split()
    updated_edges = []
    for i in range(len(route_edges) - 1):
        source_edge = route_edges[i]
        destination_edge = route_edges[i + 1]
        shortest_path = shortest_paths[source_edge][destination_edge]
        updated_edges.extend(shortest_path[:-1])  # Exclude the destination edge from the updated edges
    vehicle.attrib['edges'] = ' '.join(updated_edges)

# Save the updated routes to the original rou.xml file
tree.write('tbwal4.rou.xml')
