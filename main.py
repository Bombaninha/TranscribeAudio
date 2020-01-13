import speech_recognition as sr 
import config as c

file_audio = sr.AudioFile(c.Path())
file_text = open(c.text_file['name'], c.text_file['mode'])

r = sr.Recognizer()

with file_audio as source: 
	r.adjust_for_ambient_noise(source) 
	audio = r.record(source)

text = r.recognize_google(audio)	
file_text.write(text)
file_text.close()