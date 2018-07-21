import winspeech
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
	winspeech.say('Speak Anything : ')
	audio = r.listen(source)
	
	try:
		text = r.recognize_google(audio)
		winspeech.say('You Said : {}'.format(text))
	except:
		winspeech.say('Sorry I Could not understand you')
