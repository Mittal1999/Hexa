from channels.generic.websocket import WebsocketConsumer
import json

import translate
import firstaid

from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.send(text_data=json.dumps({
            'message': message +"\n"
        }))
        translated_message = translate.transInp(message)
        reply = firstaid.chat(translated_message)
        translated_reply = translate.transReply(message,reply)

        self.send(text_data=json.dumps({
            'message': translated_reply+"\n"
        }))

    