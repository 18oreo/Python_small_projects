from gtts import gTTS
text ="" #the message you want to convert from text to voice
tts = gTTS(text=text, lang="en")
tts.save("voice.mp3")
print("Audio Saved Successfully")

# pip install gTTS (this library needed)