import json


def edit(author):
    words = author.split()

    try:
        int(words[len(words) - 1])
        words = words[0:len(words) - 1]
    except:
        pass

    return " ".join(words)


def edits(author):
    for i in range(10):
        author = edit(author)

    return author


with open('CrawledPapers.json', 'r') as crawled_papers:
    papers = json.loads(crawled_papers.read())

    for paper in papers:
        new_authors = set()
        for author in paper["authors"]:
            new_author = edits(author)
            if new_author != "":
                new_authors.add(new_author)
        paper["authors"] = list(new_authors)

with open('CrawledPapers.json', 'w') as outfile:
    json.dump(papers, outfile)
