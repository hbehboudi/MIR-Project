import networkx as nx
import json


def calculate_page_ranks(alpha, crawled_filename, page_ranks_filename):
    graph = nx.DiGraph()

    with open(crawled_filename, 'r') as crawled_papers:
        papers = json.loads(crawled_papers.read())

        for paper in papers:
            for reference in paper["references"]:
                graph.add_edge(paper["id"], reference)

    page_ranks = nx.pagerank(graph, alpha)

    with open(page_ranks_filename, 'w') as outfile:
        json.dump(page_ranks, outfile)


def main():
    print("alpha: ", end="")
    alpha = float(input())

    calculate_page_ranks(alpha, "../CrawledPapers.json", "../PageRank.json")


if __name__ == '__main__':
    main()
