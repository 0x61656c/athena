import responses

def read(request = ""):
	with open(request,"r") as file:
		array = []
		for line in file:
			array.append(line)

	return array
			
def write(request = "", content = ""):
	try:
		with open(request, "w") as file:
			file.write("%s \n" %str(content))

	except:
		return "Err: FNF"

def event(_input = ""):
	write("data/events.txt",_input)

def meeting(_input = ""):
	write("data/meetings.txt", _input)

def assignment(_input = ""):
	write("data/assignments.txt", _input)

def reminders(_input = ""):
	write("data/reminders.txt")

def testGet():
	print(get("data/boards.txt"))

def main():
	testGet()

if __name__ == "__main__":
	main()


