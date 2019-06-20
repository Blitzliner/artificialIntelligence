#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import logging
from playsound import playsound
from datetime import datetime

log = logging.getLogger("voice")
#ch = logging.StreamHandler()
#ch.setLevel(logging.INFO)
#formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s')
#ch.setFormatter(formatter)
#log.addHandler(ch)

class voice:
    
    def __init__(self, user, assistent):
        self.user = user
        self.assistent = assistent
    
    def speak(self, audio_string, out_dir='_temp'):
        if not os.path.isdir(out_dir):
            os.mkdir(out_dir)
        filename = datetime.now().strftime('%Y%m%d_%H%M%S') + '.mp3'  
        filepath = os.path.join(out_dir, filename)
        log.info(F"{self.assistent}: {audio_string}")
        tts = gTTS(text=audio_string, lang='de')
        tts.save(filepath)
        playsound(filepath)
    
    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            log.info("Wait for input")
            audio = r.listen(source)
            data = ""
            try:
                # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                data = r.recognize_google(audio, language='de-DE')        
                log.info(F"{self.user}: {data}")
            except sr.UnknownValueError:
                log.warning("Please try again.")
            except sr.RequestError as e:
                log.error("Could not request results from Google Speech Recognition service; {0}".format(e))
    
        return data
    
    def jarvis(self, data):
        data = data.lower()
        ret_val = 1
        
        if "wie geht es dir" in data:
            self.speak("Mir geht es gut.")
    
        if "wie viel uhr haben wir" in data:
            self.speak(ctime())
    
        if "wo ist" in data:
            data = data.split(" ")
            location = data[2]
            self.speak("Ein moment, Ich zeige dir wo " + location + " liegt.")
            os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
         
        if any(s in data for s in ["beenden", "beende", "exit", "schließen"]):
            self.speak("Okay")
            ret_val = 0
            
        return ret_val 

# initialization
if __name__== "__main__":
    time.sleep(2)
    voice = voice("Manuel", "Bot")
    voice.speak("Hallo")
    ret_val = 1
    while ret_val :
        data = voice.listen()
        ret_val = voice.jarvis(data)
