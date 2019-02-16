import requests
from bs4 import BeautifulSoup
from listofusstates import states

'''
Scrapes a given page and outputs a tsv file containing
the state followed by the average income tax rate.
:param: url
:type: str
'''
def scrape_tax_rates(url):
    assert isinstance(url, str)

    # get the html and set variable rows to all table rows
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    rows = soup.find_all('tbody')[1].find_all('tr')

    # open text file to write
    f = open('../data/tax_rate.tsv', 'w')
    f.write('STATE\tTAX\n')

    # get the state and tax rate from each row and output it to file
    for row in rows:
        cols = row.find_all('td')
        state = cols[0].get_text().strip()
        col = cols[9].get_text().strip()[:-1]
        if state in states:
            f.write('{0}\t{1}\n'.format(state, col))

scrape_tax_rates('https://wallethub.com/edu/best-worst-states-to-be-a-taxpayer/2416/')
