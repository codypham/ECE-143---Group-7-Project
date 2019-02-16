class StateInfo(object):
	'''
	State object with inputs c, t, s

	c is the float cost of living
	t is the float tax rate
	s is the int salary
	'''
	def __init__(self, c=100.0, t=0.0, s=0):
		self.col = c
		self.tax = t
		self.sal = s
	def compute(self):
		return self.sal*(1-self.tax)/self.col

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
		print(line)
		line = file_object.readline()
		while line:
			state, col, tax, sal = parse_line(line)
			print(state, "	", col, "	", tax, "	", sal)
			data[state] = StateInfo(col, tax, sal)
			line = file_object.readline()
		return data
