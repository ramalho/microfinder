
def parse_line(line):
	
	code, name = line.split(";")[:2]
	char = chr(int(code, 16))
	return char, name

def add_entry(index, char, name):
	for word in name.split():
		if word in index:
			index[word].append(char)
		else:
			index[word] = [char]