import requests
from bs4 import BeautifulSoup
from listofusstates import states

def scrape_salaries(url):
    '''
    Scrapes a given page and outputs a tsv file containing
    the state followed by the average salary.
    :param: url
    :type: str
    '''
    assert isinstance(url, str)

    # get the html and set variable rows to all table rows
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    rows = soup.find_all('tbody')[6].find_all('tr')

    # open text file to write
    f = open('../data/average_salary.tsv', 'w')
    f.write('STATE\tSALARY\n')

    # get the state and salary from each row and output it to file
    for row in rows:
        cols = row.find_all('td')
        state = cols[0].get_text().strip()
        col = cols[3].get_text().strip()[1:]
        if state in states:
            f.write('{0}\t{1}\n'.format(state, col))

scrape_salaries('https://www.computercareers.org/computer-engineer-salary/')
