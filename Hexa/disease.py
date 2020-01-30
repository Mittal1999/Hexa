import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
import pandas as pd
import numpy as np
import time
stemmer = LancasterStemmer()
from sklearn.externals import joblib

df = pd.read_csv("dataset_last_try_copy.csv",encoding = "ISO-8859-1")
training_data =[]

for i in range (0,df.shape[0]):
    class_ = df.iloc[i].Source
    tp = df.iloc[i].Target
    d = dict([
        ("class",class_),
        ("sentence",tp)
    ])
    training_data.append(d)

words=[]
classes=[]
documents=[]
ignore_words=['?']


for pattern in training_data:
    w=nltk.word_tokenize(pattern['sentence'])
    words.extend(w)
    documents.append((w,pattern['class']))
    if pattern['class'] not in classes:
        classes.append(pattern['class'])

words=list(set(words))
classes=list(set(classes))
training=[]
output=[]
output_empty=[0]*len(classes)


for doc in documents:
    bag=[]
    pattern_words=doc[0]

    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    training.append(bag)
    output_row=list(output_empty)
    output_row[classes.index(doc[1])] = 1
    output.append(output_row)
    

i=0
w=documents[i][0]



def sigmoid(x):
    output=1/(1+np.exp(-x))
    return output

def sigmoid_output_to_derivative(output):
    return output*(1-output)

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    return sentence_words


def bow(sentence, words, show_details=False):
    sentence_words=clean_up_sentence(sentence)
    bag=[0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def think(sentence, show_details=False):
    x=bow(sentence.lower(),words,show_details)
    if show_details:
        print("sentence:", sentence, "\n bow:", x)
    l0=x
    l1 = sigmoid(np.dot(l0, synapse_0))
    l2 = sigmoid(np.dot(l1, synapse_1))
    return l2

    
X = np.array(training)
y = np.array(output)


ERROR_THRESHOLD = 0.01

synapse_file = 'intent_final.json' 
with open(synapse_file) as data_file: 
    synapse = json.load(data_file) 
    synapse_0 = np.asarray(synapse['synapse0']) 
    synapse_1 = np.asarray(synapse['synapse1'])

def classify(sentence, show_details=False):
    results = think(sentence, show_details)
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD ] 
    results.sort(key=lambda x: x[1], reverse=True) 
    return_results =[[classes[r[0]],r[1]] for r in results]
    # print ("%s \n Predicted Disease: %s" % (sentence, return_results))
    
    return return_results

# test = input("Enter your symtomps: \n")
# classify(test)
