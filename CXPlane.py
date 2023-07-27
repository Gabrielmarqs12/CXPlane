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

	run()
pass

def run():						## Starts the process of voice recognition
    freq = input("Select a frequency: ")
    txt = prc.freq(freq)
    
    while True:
        audio = rec.recognize(mic)
        req = rec.reconize_google(audio, language = "en-US")
        code, ans = prc.comm(req)
        if code == 1:
            break
        else
        sgen.generate(ans)
    pass
pass

startup()
