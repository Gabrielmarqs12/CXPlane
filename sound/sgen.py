##------------Libraries--------

from gtts import *
from playsound import playsound
import os

##------------Code-------------

def generate(text):
	call = gTTS(text=text, lang='en', tld='com.br')
	com_call = "com_call.mp3"
	call.save(com_call)
	playsound(com_call)

	os.remove("com_call.mp3")
	pass