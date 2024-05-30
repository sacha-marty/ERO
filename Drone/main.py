from datetime import datetime
from pathlib import Path
#need to be imported
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

def get_xml_graph():
	path = "./Montreal.xml"
	# Look if the graph is already downloaded to dodge the download
	if Path(path).is_file(): return ox.load_graphml(path)
	graph = ox.graph_from_place('Montreal, Canada', network_type='drive', simplify=True)
	ox.save_graphml(graph, path)
	return graph

def odd_vertices_graph(graph: nx.MultiGraph):
	vertices = []
	for node in graph.nodes():
		Nbr_vertices = graph.degree(node)
		if Nbr_vertices % 2 == 1: vertices.append(node)
	return vertices


def eulerize(graph: nx.MultiGraph):
	odd_vertices = odd_vertices_graph(graph)
	odd_links = []
	odd_count = len(odd_vertices)
	for i in range(0, odd_count - 1, 2):
		node_from = odd_vertices[i]
		node_to = odd_vertices[i + 1]
		graph.add_edge(node_from, node_to)
		odd_links.append((node_from, node_to))
	return odd_links

def main():
	#get the graph
	print(datetime.now(), ": reading graph")
	dir_graph = get_xml_graph()
	print(datetime.now(), ": readed graph")
	print(dir_graph)

    #make the graph undirected as drone dont care about road direction
	print(datetime.now(), ": converting to undirected")
	graph = nx.MultiGraph(dir_graph.to_undirected())
	print(datetime.now(), ": converted to undirected")
	print(graph)

    #eulerian function
	print(datetime.now(), ": converting graph to eulerian")
	eulerize(graph)
	print(datetime.now(), ": converted graph to eulerian")
	print(graph)

main()