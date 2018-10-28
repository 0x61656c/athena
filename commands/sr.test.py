import speech_recognition as sr

r = recognizer_instance.recognize_sphinx()
	#audio_data: AudioData,
 	#language: str = "en-US", 
 	#keyword_entries: Union[Iterable[Tuple[str, float]],
 	#None] = None, 
 	#grammar: Union[str, None] = None,
 	#show_all: bool = False)

with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except: 
    	print(None)