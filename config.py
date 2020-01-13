import os

#Audio file settings
current_file_path = os.getcwd() + "\\audios\\"
audio_file = {
	"name" : 'harvard.wav',
	"path" : current_file_path
}

def Path():
	return audio_file['path'] + audio_file['name']

#Text file settings
text_file = {
	"name" : 'texto.txt',
	"mode" : 'w'
}
