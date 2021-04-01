from naoqi import ALProxy
import qi
import argparse
from datetime import datetime
import time
import sys

#ip_address = "127.0.0.1"
#port = 13984

ip_address = "192.168.0.22"
port = 9559


import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
import urllib3
import pygame
urllib3.disable_warnings()
import os



session = qi.Session()
session.connect("tcp://" + str(ip_address) + ":" + str(port))

asr_service = session.service("ALAnimatedSpeech")
tts = ALProxy("ALTextToSpeech", ip_address, port)
tts.setLanguage("English")
# set the local configuration
configuration = {"bodyLanguageMode": "contextual"}

try:
    text = sys.argv[1]
    print("You said : {}".format(text))
    if (text!=""):
        asr_service.say(text, configuration)
except:
    print("Sorry could not recognize what you said")

