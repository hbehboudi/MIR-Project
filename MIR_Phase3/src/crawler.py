import json
import time

from selenium import webdriver


def click_button(browser):
    try:
        time.sleep(3)
        xpath = '//*[@id="mainArea"]/router-view/div/div/div/div/div[3]/ma-tag-cloud/div/div'
        button = browser.find_element_by_xpath(xpath)
        button.click()
        time.sleep(3)
    except:
        pass


def get_title(browser):
    xpath = '//*[@id="mainArea"]/router-view/div/div/div/div/h1'
    return browser.find_element_by_xpath(xpath=xpath).text


def get_abstract(browser):
    xpath = '//*[@id="mainArea"]/router-view/div/div/div/div/p'
    return browser.find_element_by_xpath(xpath=xpath).text


def get_year(browser):
    xpath = '//*[@id="mainArea"]/router-view/div/div/div/div/a[1]/span[1]'
    return browser.find_element_by_xpath(xpath=xpath).text


def get_authors(browser):
    xpath = '//*[@id="mainArea"]/router-view/div/div/div/div/ma-author-string-collection/div/div/div[%d]/a[1]'
    authors = []

    try:
        while True:
            authors.append(browser.find_element_by_xpath(xpath % (len(authors) + 1)).text)
    except:
        pass

    return authors


def get_related(browser):
    xpath = '//*[@id="topic-related-malinktag-%d"]/a/div[2]'
    related = []

    try:
        while True:
            related.append(browser.find_element_by_xpath(xpath % len(related)).text)
    except:
        pass

    return related


def get_citation_count(browser):
    xpath = '//*[@id="mainArea"]/router-view/div/div/div/div/div[1]/ma-statistics-item[2]/div[2]/div[2]/div[1]'
    return browser.find_element_by_xpath(xpath).text


def get_reference_count(browser):
    xpath = '//*[@id="mainArea"]/router-view/div/div/div/div/div[1]/ma-statistics-item[1]/div[2]/div[2]/div[1]'
    return browser.find_element_by_xpath(xpath=xpath).text


def get_reference(browser):
    xpath = '//*[@id="mainArea"]/router-view/router-view/ma-edp-serp/div/div[2]/div/compose/div/div[2]/ma-card[' \
            '%d]/div/compose/div/div[1]/a[1] '
    references = []
    try:
        while True:
            href = browser.find_element_by_xpath(xpath % (len(references) + 1)).get_attribute('href')
            references.append(href[37:47])
    except:
        pass

    return references


def get_result(id, papers, read, unread):
    if read.__contains__(id):
        return

    browser = webdriver.Chrome(executable_path='../chromedriver')
    browser.get("https://academic.microsoft.com/paper/" + str(id))

    time.sleep(2)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    click_button(browser)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(12)

    paper = {
        "id": id,
        "title": get_title(browser),
        "abstract": get_abstract(browser),
        "date": get_year(browser),
        "authors": get_authors(browser),
        "related_topics": get_related(browser),
        "citation_count": get_citation_count(browser),
        "reference_count": get_reference_count(browser),
        "references": get_reference(browser)
    }

    if paper["reference_count"] == "0":
        paper["references"] = []

    # if len(paper["references"]) > 0 or paper["reference_count"] == 0:
    papers.append(paper)

    read.add(id)

    for id in paper["references"]:
        unread.add(id)

    browser.close()


def main():
    unread = set()
    unread.add("2981549002")
    unread.add("3105081694")
    unread.add("2950893734")
    unread.add("3119786062")
    unread.add("2145339207")
    unread.add("2153579005")

    read = set()
    papers = []
    max_result = 2000

    while len(papers) < max_result:
        try:
            get_result(unread.pop(), papers, read, unread)
        except:
            pass

    with open('../CrawledPapers.json', 'w') as outfile:
        json.dump(papers, outfile)


if __name__ == '__main__':
    main()
