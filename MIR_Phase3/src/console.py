from crawler import get_result
from page_rank import calculate_page_ranks
from hits import calculate_hits
from content_based import calculate_content_based
from collaborative_filtering import calculate_collaborative_filtering
import json


def print_main_menu():
    print("**************************")
    print("        Main Menu        ")
    print("1: Crawler")
    print("2: PageRank")
    print("3: HITS")
    print("4: Content-based")
    print("5: Collaborative Filtering")
    print("6: Exit")


def main_menu():
    while True:
        print_main_menu()
        command = int(input())

        if command == 1:
            crawler_menu()

        if command == 2:
            page_rank_menu()

        if command == 3:
            hits_menu()

        if command == 4:
            content_based_menu()

        if command == 5:
            collaborative_filtering_menu()

        if command == 6:
            break


def print_crawler_menu():
    print("*****************************")
    print("        Crawler Menu         ")
    print("1: Add the starting papers")
    print("2: Delete the starting papers")
    print("3: View the starting papers")
    print("4: Set max")
    print("5: View max")
    print("6: Set filename")
    print("7: View filename")
    print("8: Crawl")
    print("9: Back")


def crawler_menu():
    unread = set()
    read = set()
    papers = []
    max_result = 2000
    filename = "default.json"

    while True:
        print_crawler_menu()
        command = int(input())

        if command == 1:
            print("id:", end=" ")
            unread.add(input())

        if command == 2:
            print("id:", end=" ")
            id = input()
            if unread.__contains__(id):
                unread.remove(id)

        if command == 3:
            print(list(unread))

        if command == 4:
            print("max:", end=" ")
            max_result = int(input())

        if command == 5:
            print("max:", max_result)

        if command == 6:
            print("filename:", end=" ")
            filename = input()

        if command == 7:
            print("filename:", filename)

        if command == 8:
            while len(papers) < max_result:
                try:
                    get_result(unread.pop(), papers, read, unread)
                except:
                    pass

            with open(filename, 'w') as outfile:
                json.dump(papers, outfile)

        if command == 9:
            break


def print_page_rank_menu():
    print("******************************")
    print("         PageRank Menu        ")
    print("1: Set alpha")
    print("2: View alpha")
    print("3: Set CrawledPapers filename")
    print("4: View CrawledPapers filename")
    print("5: Set PageRank filename")
    print("6: View PageRank filename")
    print("7: Calculate")
    print("8: Back")


def page_rank_menu():
    crawled_filename = "default.json"
    page_ranks_filename = "defaultPageRank.json"
    alpha = 0.86

    while True:
        print_page_rank_menu()
        command = int(input())

        if command == 1:
            print("alpha:", end=" ")
            alpha = float(input())

        if command == 2:
            print("alpha:", alpha)

        if command == 3:
            print("crawled filename:", end=" ")
            crawled_filename = input()

        if command == 4:
            print("crawled filename:", crawled_filename)

        if command == 5:
            print("PageRanks filename:", end=" ")
            page_ranks_filename = input()

        if command == 6:
            print("PageRanks filename:", page_ranks_filename)

        if command == 7:
            calculate_page_ranks(alpha, crawled_filename, page_ranks_filename)

        if command == 8:
            break


def print_hits_menu():
    print("******************************")
    print("           HITS Menu          ")
    print("1: Set n")
    print("2: View n")
    print("3: Set CrawledPapers filename")
    print("4: View CrawledPapers filename")
    print("5: Calculate")
    print("6: Back")


def hits_menu():
    crawled_filename = "default.json"
    n = 10

    while True:
        print_hits_menu()
        command = int(input())

        if command == 1:
            print("n:", end=" ")
            n = int(input())

        if command == 2:
            print("n:", n)

        if command == 3:
            print("crawled filename:", end=" ")
            crawled_filename = input()

        if command == 4:
            print("crawled filename:", crawled_filename)

        if command == 5:
            calculate_hits(n, crawled_filename, '', '')

        if command == 6:
            break


def print_content_based_menu():
    print("******************************")
    print("      Content Based Menu      ")
    print("1: Set user id")
    print("2: View user id")
    print("3: Set CrawledPapers filename")
    print("4: View CrawledPapers filename")
    print("5: Set data filename")
    print("6: View data filename")
    print("7: Calculate")
    print("8: Back")


def content_based_menu():
    crawled_filename = "default.json"
    data_filename = "data.csv"
    user_id = 0

    while True:
        print_content_based_menu()
        command = int(input())

        if command == 1:
            print("user id:", end=" ")
            user_id = int(input())

        if command == 2:
            print("user id:", user_id)

        if command == 3:
            print("crawled filename:", end=" ")
            crawled_filename = input()

        if command == 4:
            print("crawled filename:", crawled_filename)

        if command == 5:
            print("data filename:", end=" ")
            data_filename = input()

        if command == 6:
            print("data filename:", data_filename)

        if command == 7:
            calculate_content_based(user_id, data_filename, crawled_filename)

        if command == 8:
            break


def print_collaborative_filtering_menu():
    print("******************************")
    print(" Collaborative Filtering Menu ")
    print("1: Set user id")
    print("2: View user id")
    print("3: Set n")
    print("4: View n")
    print("5: Set CrawledPapers filename")
    print("6: View CrawledPapers filename")
    print("7: Set data filename")
    print("8: View data filename")
    print("9: Calculate")
    print("10: Back")


def collaborative_filtering_menu():
    crawled_filename = "default.json"
    data_filename = "data.csv"
    user_id = 0
    n = 10

    while True:
        print_collaborative_filtering_menu()
        command = int(input())

        if command == 1:
            print("user id:", end=" ")
            user_id = int(input())

        if command == 2:
            print("user id:", user_id)

        if command == 3:
            print("n:", end=" ")
            n = int(input())

        if command == 4:
            print("n:", n)

        if command == 5:
            print("crawled filename:", end=" ")
            crawled_filename = input()

        if command == 6:
            print("crawled filename:", crawled_filename)

        if command == 7:
            print("data filename:", end=" ")
            data_filename = input()

        if command == 8:
            print("data filename:", data_filename)

        if command == 9:
            calculate_collaborative_filtering(user_id, n, data_filename, crawled_filename)

        if command == 10:
            break


if __name__ == '__main__':
    main_menu()
