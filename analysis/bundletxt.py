from stateinfo import StateInfo
import csv

'''
Given the state tax, cost of living, and salary info tsv files,
combine them to a single data set represented as a tsv file.
'''
def bundle_data():

    # open source tsv files to read
    salary = open('../data/average_salary.tsv', 'r')
    col = open('../data/cost_of_living.tsv', 'r')
    tax = open('../data/tax_rate.tsv', 'r')

    # open tsv file to write
    result = open('../data/master_data.tsv', 'w')
    result.write('STATE\tTAX\tCOST OF LIVING\tSALARY\n')

    # parse by tab delimiter
    sal_rows = csv.reader(salary, delimiter='\t')
    col_rows = csv.reader(col, delimiter='\t')
    tax_rows = csv.reader(tax, delimiter='\t')

    # skip the first row
    next(sal_rows)
    next(col_rows)
    next(tax_rows)

    dict = {}

    for row in sal_rows:
        state = row[0]
        sal = int(row[1].replace(',', ''))
        if state in dict:
            dict[state].avg_salary = sal
        else:
            dict[state] = StateInfo(name = state, avg_salary = sal)

    for row in col_rows:
        state = row[0]
        col = float(row[1])
        if state in dict:
            dict[state].col = col
        else:
            dict[state] = StateInfo(name = state, col = col)

    for row in tax_rows:
        state = row[0]
        tax = float(row[1])
        if state in dict:
            dict[state].tax = tax
        else:
            dict[state] = StateInfo(name = state, tax = col)

    for key, value in dict.items():
        result.write('{0}\t{1}\t{2}\t{3}\n'.format(value.name, value.tax, value.col, value.avg_salary))

bundle_data()
