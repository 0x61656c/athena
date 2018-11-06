import speech_recognition as sr
import os

	#audio_data: AudioData,
 	#language: str = "en-US", 
 	#keyword_entries: Union[Iterable[Tuple[str, float]],
 	#None] = None, 
 	#grammar: Union[str, None] = None,
 	#show_all: bool = False)

def listen():
	try:
		r = recognizer_instance.recognize_sphinx()

		with sr.Microphone() as source:
		    audio = r.listen(source)
		    try:
		        text = r.recognize_google(audio)
		        return text
		    except: 
		    	return None
	except:
		return None


def respond(_input_str):
	os.system("say -v Moira "'%s'"" %(_input_str))

def testRespond():
	respond("Hello, World")

def main():
	#testRespond()
	pass

if __name__ == "__main__":
	main()