from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import os


'''
translates users input
inp:users input
'''
def transInp(inp):
    trans=Translator()
    translated=trans.translate(inp)
    return translated.text
 

'''
translates bots reply
inp:users input
reply:bots reply
'''   
def transReply(inp,reply):
    trans=Translator()
    detected=trans.detect(inp)
    lang=detected.lang
    translated=trans.translate(reply,dest=lang)
    return translated.text


'''
code:language code(cant detect,need to ask language from user)
'''
def speechToText(code):
	r=sr.Recognizer()
	with sr.Microphone() as source:
		audio=r.listen(source)
		text=r.recognize_google(audio,language=code+'-IN')
		return(text)

'''
code:language code
reply:bots reply
'''
def textToSpeech(code,reply):
	output=gTTS(text=reply,lang=code,slow=False)
	output.save("reply.mp3")
	os.system("start reply.mp3")






'''
languages supported for speech to text with codes.these languages also supported by translation(no need of codes here)
hindi:hi-IN
bangla: bn-IN
english: en-IN
gujarati: gu-IN
kannada:kn-IN
malayalam:ml-IN
marathi:mr-IN
tamil:ta-IN
telugu:te-IN
urdu:ur-IN


'''