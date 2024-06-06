from datetime import datetime
from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt
import osmnx as ox

def get_graph():
	path = "./graph.xml"
	if Path(path).is_file(): return ox.load_graphml(path)
	downloaded = ox.graph_from_place('Montreal, Canada', network_type='drive', simplify=True)
	ox.save_graphml(downloaded, path)
	return downloaded

def get_odd_vertices(G: nx.MultiGraph):
	result = []
	for node in G.nodes():
		degree = G.degree(node)
		if degree % 2 == 1: result.append(node)
	return result

def eulerize(G: nx.MultiGraph):
	odd_vertices = get_odd_vertices(G)
	shortcuts = []
	odd_count = len(odd_vertices)
	for i in range(0, odd_count - 1, 2):
		node_from = odd_vertices[i]
		node_to = odd_vertices[i + 1]
		G.add_edge(node_from, node_to)
		shortcuts.append((node_from, node_to))
	return shortcuts

def substitute_shortcuts(G: nx.MultiGraph, path, shortcuts):
	result = []
	for node_from, node_to in path:
		if (node_from, node_to) in shortcuts:
			shortest_path = nx.shortest_path(G, node_from,node_to)
			for i in range(len(shortest_path) - 1):
				result.append((shortest_path[i], shortest_path[i + 1]))
		else:
			result.append((node_from, node_to))
	return result

def measure_length(graph: nx.MultiGraph, edges):
	total_length = 0
	for (node_from, node_to) in edges:
		edge = graph.get_edge_data(node_from, node_to)[0]
		try: total_length += edge['length']
		except: continue
	return total_length

def main():
	print(datetime.now(), "reading the graph")
	directed_graph = get_graph()
	print(directed_graph)

	print(datetime.now(), "converting to undirected")
	graph = nx.MultiGraph(directed_graph.to_undirected())
	print(graph)

	original_edges = []
	for edge in graph.edges(): original_edges.append(edge)

	print(datetime.now(), "converting eulerian")
	shortcuts = eulerize(graph)
	print(graph)

	print(datetime.now(), "finding circuit")
	circuit = list(nx.eulerian_circuit(graph))
	result = substitute_shortcuts(graph, circuit, shortcuts)
	print(datetime.now(), "finished")

	with open("path.txt", "w") as file:
		for step in result: file.write(str(step) + "\n")

	print("length       :", measure_length(graph, result))
	print("ideal_length :", measure_length(graph, original_edges))

main()
