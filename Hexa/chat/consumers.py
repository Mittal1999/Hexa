from channels.generic.websocket import WebsocketConsumer
import json

import translate
import firstaid
import bmiwhr

from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS


class ChatConsumer(WebsocketConsumer):

    height = 0
    weight = 0

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message'][0]
        message1 = text_data_json['message'][1]
        
        translated_message = translate.transInp(message)
        if message1 == "First Aid":
            reply = ""
            self.send(text_data=json.dumps({
                'message': message +"\n"
            }))
            reply = firstaid.chat(translated_message)
            reply = translate.transReply(message,reply)
            reply = translate.transReply(message,reply)
            self.send(text_data=json.dumps({
                'message': reply+"\n"
            }))
        elif message1 == "BMI":
            reply = ""
            if message != "":
                if ChatConsumer.height == 0:
                    ChatConsumer.height = message
                    reply = ChatConsumer.height
                    self.send(text_data=json.dumps({
                        'message': reply+"\n"
                    }))
                else:
                    ChatConsumer.weight = message
                    reply = ChatConsumer.weight
                    self.send(text_data=json.dumps({
                        'message': reply+"\n"
                    }))
            if(ChatConsumer.height == 0):
                reply = "Enter your height(in m): "
                self.send(text_data=json.dumps({
                    'message': reply+"\n"
                }))
                # accept
            elif(ChatConsumer.weight == 0):
                reply = "Enter your weight(in kg): "
                self.send(text_data=json.dumps({
                    'message': reply+"\n"
                }))
            else:
                reply = bmiwhr.bmi(ChatConsumer.height, ChatConsumer.weight)
                self.send(text_data=json.dumps({
                    'message': "Your BMI is: "+reply[1]+" and you are "+reply[0]+"\n"
                }))
        else:
            reply = "Error"
        if (ChatConsumer.height !=0 and ChatConsumer.weight !=0):
            ChatConsumer.height = 0
            ChatConsumer.weight = 0
    