import networkx as nx
import json


def main():
    print("alpha: ", end="")
    alpha = float(input())

    graph = nx.DiGraph()

    with open('../CrawledPapers.json', 'r') as crawled_papers:
        papers = json.loads(crawled_papers.read())

        for paper in papers:
            for reference in paper["references"]:
                graph.add_edge(paper["id"], reference)

    page_ranks = nx.pagerank(graph, alpha)

    with open('../PageRank.json', 'w') as outfile:
        json.dump(page_ranks, outfile)


if __name__ == '__main__':
    main()
