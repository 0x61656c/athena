import wolframalpha

app_id = "L4YVH6-HPV69WKAWQ"

def wolframQuery(_input, _appid = "L4YVH6-HPV69WKAWQ"):
	client = wolframalpha.Client(_appid)
	res = client.query(str(_input))
	try: 
		(next(res.results).text)
		return str((next(res.results).text))
	except:
		return None
	

def testWolframQuery():
	print(wolframQuery("What is 2 + 2?"))

def main():
	testWolframQuery()

if __name__ == "__main__":
	main()