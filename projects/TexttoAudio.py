import os
from gtts import gTTS
from playsound import playsound

audio = os.path.join(os.getcwd(), "speech.mp3")
language = 'en'
sp = gTTS(text="By following these steps, you should be able to troubleshoot and resolve the issue with playing the audio file using the playsound module. If you continue to face issues, switching to an alternative library like pygame is a reliable solution.", lang=language, slow=False)
sp.save(audio)
playsound(audio)
print("==== Audio is playing ====")
