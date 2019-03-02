class StateInfo(object):

    def __init__(self, name = "", tax = 0.0, col = 0.0, avg_salary = 0):
        self.name = name
        self.tax = tax
        self.col = col
        self.avg_salary = avg_salary

    def __repr__(self):
        return '{{state: {0}, tax: {1}, col: {2}, avg_salary: {3}}}'.format(self.name, self.tax, self.col, self.avg_salary)
