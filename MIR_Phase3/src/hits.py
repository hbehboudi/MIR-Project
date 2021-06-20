import networkx as nx
import json


def get_authors_by_paper_id(id, paper_by_id):
    if paper_by_id.__contains__(id):
        return set(paper_by_id[id]["authors"])

    return set()


def get_authors_by_paper_ids(ids, paper_by_id):
    authors = set()

    for id in ids:
        authors = authors.union(get_authors_by_paper_id(id, paper_by_id))

    return authors


def calculate_hits(n, crawled_filename, hub_filename, authority_filename):
    graph = nx.DiGraph()
    paper_by_id = dict()

    with open(crawled_filename, 'r') as crawled_papers:
        papers = json.loads(crawled_papers.read())

        for paper in papers:
            paper_by_id[paper["id"]] = paper

    for paper in paper_by_id.values():
        for from_author in get_authors_by_paper_id(paper["id"], paper_by_id):
            for to_author in get_authors_by_paper_ids(paper["references"], paper_by_id):
                graph.add_edge(from_author, to_author)

    hubs, authorities = nx.hits(graph)

    if hub_filename != '':
        with open(hub_filename, 'w') as outfile:
            json.dump(hubs, outfile)

    if authority_filename != '':
        with open(authority_filename, 'w') as outfile:
            json.dump(authorities, outfile)

    result = [k for k, v in sorted(authorities.items(), key=lambda item: item[1])]
    result.reverse()
    result = result[0:n]
    print({k: authorities[k] for k in result})


def main():
    print("n: ", end="")
    n = int(input())

    calculate_hits(n, '../CrawledPapers.json', '../Hub.json', '../Authority.json')


if __name__ == '__main__':
    main()
