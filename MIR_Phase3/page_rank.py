import networkx as nx
import json

print("alpha: ", end="")
alpha = float(input())

G = nx.DiGraph()

with open('CrawledPapers.json', 'r') as myfile:
    papers = json.loads(myfile.read())

    for paper in papers:
        id = paper["id"]

        for reference in paper["references"]:
            G.add_edge(id, reference)

page_ranks = nx.pagerank(G, alpha)

with open('PageRank.json', 'w') as outfile:
    json.dump(page_ranks, outfile)
