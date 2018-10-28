#import keywords
import wolframCall
from random import randint
from responses import *
import recorder
import os
import listenTest


def decisionMake(_input = ""):
	"""
	Decides how to process input based on keyword search in input query. 
	Variable input must be string, where it represents the query input by the user.
	All expressions must contain some string element to notify the engine of what protocol to execute
	else it will resort to an output indicative of mem failure.
	"""
	try:
		adjusted_str = _input.replace("Wolfram", " ")
		adjusted_str = adjusted_str.replace(")", " ")
		adjusted_str = adjusted_str.replace("(", " ")
		
		intro = handle(wolframResult)

		_output = str(wolframCall.wolframQuery(adjusted_str))
		return "%s" %(_output)

	except:
		_output = str(handle(notFound))

	
def testDecisionMake():
	#print(decisionMake("wolf How many states are in the US?"))
	pass

def main():
	intro = handle(introductions)
	recorder.respond(intro)
	_string = input()
	recorder.respond(decisionMake(_string))

if __name__ == "__main__":
	main()
