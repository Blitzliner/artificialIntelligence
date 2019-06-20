from hear import voice
import logging

logging.basicConfig(format="%(asctime)s: %(name)s: %(levelname)s: %(message)s", level=logging.INFO)
log = logging.getLogger("main")



voice = voice.voice("Manuel", "Bot")
voice.speak("Hallo")
ret_val = 1
while ret_val :
    data = voice.listen()
    ret_val = voice.jarvis(data)