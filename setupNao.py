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

Posture = ALProxy("ALRobotPosture", ip_address, port)
Posture.goToPosture("Stand", 3.0)
asr_service.say("Hello, You want to talk with me?", configuration)

