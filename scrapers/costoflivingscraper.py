import requests
from bs4 import BeautifulSoup
from listofusstates import states

'''
Scrapes a given page and outputs a tsv file containing
the state followed by the state's average cost of living.
:param: url
:type: str
'''
def scrape_cost_of_living(url):
    assert isinstance(url, str)

    # get the html and set variable rows to all table rows
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    rows = soup.find_all('tr')[2:54]

    # open text file to write
    f = open('../data/cost_of_living.tsv', 'w')
    f.write('STATE\tCOL\n')

    # get the state and cost of living from each row and output it to file
    for row in rows:
        cols = row.find_all('td')
        state = cols[0].get_text().strip()
        col = cols[2].get_text().strip()
        if state in states:
            f.write('{0}\t{1}\n'.format(state, col))

scrape_cost_of_living('https://www.missourieconomy.org/indicators/cost_of_living/')
