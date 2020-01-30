from channels.generic.websocket import WebsocketConsumer
import json

import translate
import firstaid
import bmiwhr
import disease

from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS


class ChatConsumer(WebsocketConsumer):

    height = 0
    weight = 0
    sex = ""
    waist = 0
    hip = 0
    age = 0

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message'][0]
        message1 = text_data_json['message'][1]
        
        translated_message = translate.transInp(message)
        # First Aid
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

        # BMI
        elif message1 == "BMI":
            if (ChatConsumer.height !=0 and ChatConsumer.weight !=0):
                ChatConsumer.height = 0
                ChatConsumer.weight = 0
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

        # Disease Prediction
        elif message1 == "Disease Prediction":
            reply = ""
            ans1 = ""
            ans2 = ""
            self.send(text_data=json.dumps({
                'message': message +"\n"
            }))
            reply = disease.classify(translated_message)
            if(len(reply) == 0):
                ans1 = "Enter more symptoms"
            else:
                for r in reply:
                    ans1 += r[0]+ ", "
                ans1 = ans1[0:-2]
            # reply = translate.transReply(message,reply[0])
            # reply = translate.transReply(message,reply)
            self.send(text_data=json.dumps({
                'message': ans1+"\n"
            }))

        # WHR
        elif message1 == "WHR":            
            if (ChatConsumer.waist !=0 and ChatConsumer.hip !=0 and ChatConsumer.sex != ""):
                ChatConsumer.waist = 0
                ChatConsumer.hip = 0
                ChatConsumer.sex = ""
            reply = ""
            if message != "":
                if ChatConsumer.waist == 0:
                    ChatConsumer.waist = message
                    reply = ChatConsumer.waist
                    self.send(text_data=json.dumps({
                        'message': reply+"\n"
                    }))
                elif ChatConsumer.hip == 0:
                    ChatConsumer.hip = message
                    reply = ChatConsumer.hip
                    self.send(text_data=json.dumps({
                        'message': reply+"\n"
                    }))
                else:
                    ChatConsumer.sex = message
                    reply = ChatConsumer.sex
                    self.send(text_data=json.dumps({
                        'message': reply+"\n"
                    }))
            if(ChatConsumer.waist == 0):
                reply = "Enter your Waist(in cm): "
                self.send(text_data=json.dumps({
                    'message': reply+"\n"
                }))
                # accept
            elif(ChatConsumer.hip == 0):
                reply = "Enter your Hip(in cm): "
                self.send(text_data=json.dumps({
                    'message': reply+"\n"
                }))
            elif(ChatConsumer.sex == ""):
                reply = "Enter your Sex(in male/female): "
                self.send(text_data=json.dumps({
                    'message': reply+"\n"
                }))
            else:
                reply = bmiwhr.waist_to_hip_ratio(ChatConsumer.waist, ChatConsumer.hip, ChatConsumer.sex)
                self.send(text_data=json.dumps({
                    'message': "Your waist To Hip Ratio is: "+reply[1]+" and "+reply[0]+"\n"
                }))

        # BMR
        elif message1 == "BMR":
            if (ChatConsumer.height !=0 and ChatConsumer.weight !=0 and ChatConsumer.sex != "" and ChatConsumer.age !=0):
                ChatConsumer.height = 0
                ChatConsumer.weight = 0
                ChatConsumer.age = 0
                ChatConsumer.sex = ""
            reply = ""
            if message != "":
                if ChatConsumer.height == 0:
                    ChatConsumer.height = message
                    reply = ChatConsumer.height
                    self.send(text_data=json.dumps({
                        'message': reply+"\n"
                    }))
                elif ChatConsumer.weight == 0:
                    ChatConsumer.weight = message
                    reply = ChatConsumer.weight
                    self.send(text_data=json.dumps({
                        'message': reply+"\n"
                    }))
                elif ChatConsumer.age == 0:
                    ChatConsumer.age = message
                    reply = ChatConsumer.age
                    self.send(text_data=json.dumps({
                        'message': reply+"\n"
                    }))
                else:
                    ChatConsumer.sex = message
                    reply = ChatConsumer.sex
                    self.send(text_data=json.dumps({
                        'message': reply+"\n"
                    }))
            if(ChatConsumer.height == 0):
                reply = "Enter your Height(in cm): "
                self.send(text_data=json.dumps({
                    'message': reply+"\n"
                }))
                # accept
            elif(ChatConsumer.weight == 0):
                reply = "Enter your Weight(in kg): "
                self.send(text_data=json.dumps({
                    'message': reply+"\n"
                }))
            elif(ChatConsumer.age == 0):
                reply = "Enter your Age(in years): "
                self.send(text_data=json.dumps({
                    'message': reply+"\n"
                }))
            elif(ChatConsumer.sex == ""):
                reply = "Enter your Sex(in male/female): "
                self.send(text_data=json.dumps({
                    'message': reply+"\n"
                }))
            else:
                reply = bmiwhr.basal_metabolic_rate(ChatConsumer.height, ChatConsumer.weight, ChatConsumer.age, ChatConsumer.sex)
                self.send(text_data=json.dumps({
                    'message': "Your Basal Metabolic Rate: "+reply+"\n"
                }))


        else:
            reply = "Error"
        
        


        