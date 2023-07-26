##------------Libraries--------

from lib import process as prc
from sound import sgen
import speech_recognition as sr
import pyaudio

import os

##------------Code-------------

def startup():					## Search for missing files
	os.system("cls")
	print("CXPlane v1.0")
	print("")

	print("Searching for missing files...")
	try:
		with open("info.txt", "r") as info:
			msg = info.readlines()
			for ln in msg:
				if "*" in ln:
					print("[V] File Detected")
	except FileNotFoundError:
		print("[!]Error 404. Creating a info file")
		with open("info.txt", "a") as info:
			info.write("Callsign:\nDeparture:\nArrival:\n*:")
		pass
	register()
pass

def register():					## Read information from info.txt and transfer to process.py library 
	print("Reading Files...")	
	with open("info.txt", "r") as info:
		msg = info.readlines()
		prc.start(msg)

	recognition()
pass

def recognition():				## Starts the process of voice recognition
	print("Inicializing Recognizer...")
	rec = sr.Recognizer()
	print("[V] Recognizer Startup Completed !")
	with sr.Microphone(1) as mic:
		rec.adjust_for_ambient_noise(mic)
		print("[V]System Ready... Waiting for your request!")
		while True:
			audio = rec.listen(mic)
			req = rec.recognize_google(audio, language="en-US")
			ans = prc.recognize(req)
			sgen.generate(ans)
		pass
pass
	
startup()
