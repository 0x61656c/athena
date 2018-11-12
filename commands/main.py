#import keywords
import wolframCall
from random import randint
from responses import *
from kanban import *
import recorder
import os
import listenTest

def wolfram(_input):
	"""
	Runs input through Wolfram Alpha.
	"""
	adjusted_str = _input.replace("calculate", " ")
	adjusted_str = adjusted_str.replace(")", " ")
	adjusted_str = adjusted_str.replace("(", " ")

	print(adjusted_str)
	_output = str(wolframCall.wolframQuery(adjusted_str))
	print(_output)
	return "%s" %(_output)

def kanban(_input):
	"""
	adds event to necessary text file, for readback later.
	"""
	
	if "event" in _input:
		event(_input)
		return handle(kanbanEvent)

	elif "assignment" in _input:
		assignment(_input)
		return handle(assignmentEvent)


	elif "meeting" in _input:
		meeting(_input)
		return handle(kanbanMeeting)


def tellJoke():
	output = handle(jokes)
	return output

def decisionMake(_input = ""):
	"""
	Decides how to process input based on keyword search in input query. 
	Variable input must be string, where it represents the query input by the user.
	All expressions must contain some string element to notify the engine of what protocol to execute
	else it will resort to an output indicative of mem failure.
	"""
	try:

		if "calculate" in _input:
			"""replace above string with protocol name"""
			return wolfram(_input)

		elif "schedule" in _input:
			return kanban(_input)

		elif "joke" in _input:
			return tellJoke()

		elif "hide a body" in _input or "dispose of" in _input:
			return "I found some promising garbage dumbs nearby"

		else:
			return str(handle(notFound))


	except:
		_output = str(handle(notFound))

	
def testDecisionMake():
	#print(decisionMake("wolf How many states are in the US?"))
	pass

def main():
	intro = handle(introductions)
	#recorder.respond(intro)
	print(intro)
	#_string = listenTest.listen()
	_string = input()
	#recorder.respond(decisionMake(_string))
	print(decisionMake(_string))

if __name__ == "__main__":
	main()
