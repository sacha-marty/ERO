from datetime import datetime
from pathlib import Path
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

def get_xml_graph(sector):
	path = "./"+sector+".xml"
	# Look if the graph is already downloaded to dodge the download
	if Path(path).is_file(): return ox.load_graphml(path)
	graph = ox.graph_from_place(sector+', Montreal, Canada', network_type='drive', simplify=True)
	ox.save_graphml(graph, path)
	return graph



def main():
    #get the graphs
	sectors = ["Outremont", "Verdun", "Anjou", "Rivière-des-prairies-pointe-aux-trembles", "Le Plateau-Mont-Royal"]
    #for sector in sectors:
	print(datetime.now(), ": reading "+sectors[1]+" graph")
	graph = get_xml_graph(sectors[1])
	print(datetime.now(), ": readed "+sectors[1]+" graph")
	print(graph)

    #eulerian function
	print(datetime.now(), "converting graph to eulerian")
	eulerize(graph)
	print(graph)

main()
