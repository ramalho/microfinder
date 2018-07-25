from index import parse_line, add_entry	

def test_parse_line():
	line = "0024;DOLLAR SIGN;Sc;0;ET;;;;;N;;;;;"

	char, name = parse_line(line)

	assert char == "$"
	assert name == "DOLLAR SIGN"

def test_single_entry():
	entries = {}
	char, name = "$", "DOLLAR SIGN"

	add_entry(entries, char, name)

	assert "DOLLAR" in entries
	assert "SIGN" in entries
	assert entries["DOLLAR"] == ["$"]
	assert entries["SIGN"] == ["$"]

def test_multiple_entries():
	entries = {}
	data = [("$", "DOLLAR SIGN"), ("%", "PERCENT SIGN")]

	for char, name in data:
		add_entry(entries, char, name)

	assert entries["PERCENT"] == ["%"]
	assert entries["SIGN"] == ["$", "%"]
	
