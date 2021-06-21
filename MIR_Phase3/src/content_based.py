import csv
import json


def get_topics(data_filename):
    with open(data_filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            return [topic.lower() for topic in row.keys()]
    return []


def get_users(data_filename):
    user_by_id = {}

    with open(data_filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0

        for row in csv_reader:
            user = {}

            for key in row.keys():
                if row[key] == '':
                    user[key.lower()] = 0
                else:
                    user[key.lower()] = float(row[key])

            user_by_id[line_count] = user
            line_count += 1

    return user_by_id


def get_papers(topics, crawled_filename):
    papers = {}

    with open(crawled_filename, 'r') as crawled_papers:
        for paper in json.loads(crawled_papers.read()):
            row = {}

            for topic in topics:
                paper["related_topics"] = [x.lower() for x in paper["related_topics"]]
                if paper["related_topics"].__contains__(topic):
                    row[topic] = 1
                else:
                    row[topic] = 0

            papers[paper["id"]] = row

    return papers


def get_scores(papers, user):
    scores = {}

    for paper_id in papers:
        score = 0
        paper = papers[paper_id]

        for topic in paper:
            score += paper[topic] * user[topic]

        scores[paper_id] = score

    return scores


def calculate_content_based(user_id, data_filename, crawled_filename):
    topics = get_topics(data_filename)
    users = get_users(data_filename)
    papers = get_papers(topics, crawled_filename)

    scores = get_scores(papers, users[user_id])

    result = [k for k, v in sorted(scores.items(), key=lambda item: item[1])]
    result.reverse()
    result = result[0:10]
    # print({k: scores[k] for k in result})
    print(result)


def main():
    print("user: ", end="")
    user_id = int(input())

    calculate_content_based(user_id, '../data.csv', '../CrawledPapers.json')


if __name__ == '__main__':
    main()
