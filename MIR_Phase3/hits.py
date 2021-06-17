import networkx as nx
import json

print("n: ", end="")
n = int(input())

G = nx.DiGraph()
paper_dict = dict()


def get_authors_by_paper_id(id):
    if paper_dict.__contains__(id):
        return set(paper_dict[id]["authors"])

    return set()


def get_authors_by_paper_ids(ids):
    authors = set()

    for id in ids:
        authors = authors.union(get_authors_by_paper_id(id))

    return authors


with open('CrawledPapers.json', 'r') as crawled_papers:
    papers = json.loads(crawled_papers.read())

    for paper in papers:
        id = paper["id"]
        paper_dict[id] = paper

for paper in paper_dict.values():
    for from_author in get_authors_by_paper_id(paper["id"]):
        for to_author in get_authors_by_paper_ids(paper["references"]):
            G.add_edge(from_author, to_author)

hubs, authorities = nx.hits(G)

with open('Hub.json', 'w') as outfile:
    json.dump(hubs, outfile)

with open('Authority.json', 'w') as outfile:
    json.dump(authorities, outfile)

result = [k for k, v in sorted(authorities.items(), key=lambda item: item[1])]
result.reverse()
result = result[0:n]
print({k: authorities[k] for k in result})
