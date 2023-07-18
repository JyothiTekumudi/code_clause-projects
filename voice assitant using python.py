import pyttsx3
import wikipedia
voice=pyttsx3.init()
In=input("searching")
result=wikipedia.summary(In,sentences=5)
print(result)
voice.say(result)
voice.runAndWait()