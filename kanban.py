
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
		
		return None
	
	except:
		return "Err: FNF"

def event(_input = ""):
	write("events.txt",_input)

def meeting(_input = ""):
	write("meetings.txt", _input)

def assignment(_input = ""):
	write("assignements.txt", _input)

def reminders (_input = ""):
	write("reminders.txt")

def testGet():
	print(get("boards.txt"))

def main():
	testGet()

if __name__ == "__main__":
	main()


