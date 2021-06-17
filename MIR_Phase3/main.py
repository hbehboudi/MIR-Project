import json

result = list()

with open('CrawledPapers.json') as json_file:
    data = json.load(json_file)
    data = list(data)

    counter = 0
    for paper in data:
        if counter < 2000:
            result.append(paper)
            counter += 1

with open('CrawledPapers.json', 'w') as outfile:
    json.dump(result, outfile)
