from random import randint

introductions = ["I am listening",
	"What can I do for you?",
	"How can I help you?",
	"What do you need?",
	"How can I assist you today?"]

notFound = ["That query failed for some reason.",
	"Im not sure why, but that query seemed to fail.",
	"Query failed. Try again?",
	"I'm afraid I couldn't handle those inputs."]

wolframResult = ["Here is what I found boss:",
	"Here is what we are looking at:",
	"I found something:",
	"I found this:",
	"Here is what I have got"]

def handle(samples):
	choice = randint(0,len(samples)-1)
	return samples[choice]

