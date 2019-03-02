from us_state_abbrev import us_state_abbrev

class StateInfo(object):
	'''
	State object with inputs name, col, tax, sal

	name is the state name
	col is the float cost of living
	tax is the float tax rate
	sal is the int salary
	'''
	def __init__(self, name, abbrev='', col=100.0, tax=0.0, sal=0):
		self.name = name
		self.abbrev = abbrev
		self.col = col
		self.tax = tax
		self.sal = sal

	def __repr__(self):
		return '{{state: {0}, tax: {1}, col: {2}, sal: {3}}}'.format(self.name, self.tax, self.col, self.sal)

	def compute(self):
		result = self.sal
		tax = self.tax/100
		result = result - (result*tax)
		result = result/(self.col/100)
		return round(result,2)

def parse_line(data):
	'''
	Inputs a tab delimited string and separates the string
	returns a set formatted like [string, float, float, int]

	'''
	line = data.split('\t')
	state = line[0]
	tax = float(line[1])
	cost_of_living = float(line[2])
	income = int(line[3])
	return state, cost_of_living, tax, income

def parse_file(filepath):
	'''
	Parses the text of the file and returns the data in a dictionary

	Filepath is a string with the input filepath location

	Returns a dictionary with the key being the name of the state and
	'''
	data = {}

	with open(filepath, 'r') as file_object:
		line = file_object.readline()
		# print(line)
		line = file_object.readline()
		while line:
			state, col, tax, sal = parse_line(line)
			# print(state, "	", col, "	", tax, "	", sal)
			data[state] = StateInfo(state, us_state_abbrev[state], col, tax, sal)
			line = file_object.readline()
		return data

def generate_data_set(filepath):
	data_map = parse_file(filepath)

	result = open('../data/data_analysis.tsv', 'w')
	result.write('STATE\tCODE\tTAX\tCOST OF LIVING\tSALARY\tADJUSTED INCOME\n')

	for info in data_map.values():
		result.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n'.format(info.name, info.abbrev, info.tax, info.col, info.sal, info.compute()))

generate_data_set('../data/master_data.tsv')
