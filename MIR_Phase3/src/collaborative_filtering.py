from content_based import get_topics, get_papers, get_users, get_scores


def find_neighbours(users, selected_user_id, n):
    neighbours = {}
    for user_id in users.keys():
        if user_id == selected_user_id:
            continue
        neighbours[user_id] = 0
        for topic in users[user_id]:
            neighbours[user_id] += users[user_id][topic] * users[selected_user_id][topic]

    result = [k for k, v in sorted(neighbours.items(), key=lambda item: item[1])]
    result.reverse()
    return result[0:n]


def get_user(n, user_id, data_filename):
    users = get_users(data_filename)
    result = {}

    neighbours = find_neighbours(users, user_id, n)

    for topic in users[user_id]:
        if users[user_id][topic] == 0:
            result[topic] = 0
            for neighbour_user_id in neighbours:
                result[topic] += users[neighbour_user_id][topic]
            result[topic] /= n
        else:
            result[topic] = users[user_id][topic]

    return result


def calculate_collaborative_filtering(user_id, n, data_filename, crawled_filename):
    topics = get_topics(data_filename)
    papers = get_papers(topics, crawled_filename)

    user = get_user(n, user_id, data_filename)

    scores = get_scores(papers, user)

    result = [k for k, v in sorted(scores.items(), key=lambda item: item[1])]
    result.reverse()
    result = result[0:10]

    print(user)
    print()
    print(result)


def main():
    print("user: ", end="")
    user_id = int(input())

    print("n: ", end="")
    n = int(input())

    calculate_collaborative_filtering(user_id, n, '../data.csv', '../CrawledPapers.json')


if __name__ == '__main__':
    main()
