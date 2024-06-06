from datetime import datetime
from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt
import osmnx as ox

def get_graph():
	path = "./graph.xml"
	if Path(path).is_file(): return ox.load_graphml(path)
	downloaded = ox.graph_from_place('Plateau-Mont-Royal, Montreal, Canada', network_type='drive', simplify=True)
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

def get_city():
	directed_graph = get_graph()
	graph = nx.MultiGraph(directed_graph.to_undirected())
	return graph

def segment(graph, circuit, count):
	total_length = measure_length(graph, circuit)
	(parts, current_length, current_index) = ([], 0, 0)
	for part_index in range(0, count):
		fraction = (part_index + 1) / count
		part = []
		while current_length < (total_length * fraction) and current_index < len(circuit):
			part.append(circuit[current_index])
			current_length += measure_length(graph, [circuit[current_index]])
			current_index += 1
		parts.append(part)
	return parts

def serialize_circuit(circuit, path):
	with open(path, "w") as file:
		for step in circuit: file.write(str(step) + "\n")

def main():
	print(datetime.now(), "reading the graph")
	graph = get_city()

	original_edges = []
	for edge in graph.edges(): original_edges.append(edge)

	print(datetime.now(), "converting eulerian")
	shortcuts = eulerize(graph)
	print(graph)

	print(datetime.now(), "finding circuit")
	circuit = list(nx.eulerian_circuit(graph))
	result = substitute_shortcuts(graph, circuit, shortcuts)
	print(datetime.now(), "finished")

	serialize_circuit(circuit, "./path.txt")

	print("length       :", measure_length(graph, result))
	print("ideal_length :", measure_length(graph, original_edges))

	for count in range(0, 10):
		parts = []
		segments = segment(graph, result, count)
		index = 0
		for seg in segments:
			length = measure_length(graph, seg)
			print("path_", count, "_", index, ":   ", length)
			serialize_circuit(seg, f"./out/path_{count}_{index}.txt")
			parts.append((length, seg))
			index += 1

main()
