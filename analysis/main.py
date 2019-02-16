from parser import *
states = parse_file("../data/master_data.tsv")

for key in states:
	print(key, ": ", states[key].compute())
