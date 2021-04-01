Nao speach with Real AI

Nao from Softbank Robotics is used to talk to a human.  On the background a Python 3.7 script is running on the parl.ai python platform.  I used the tasks of https://parl.ai/projects/dodecadialogue/​.
And I added an own speech agent based on the local_human agent of parl.ai.  Just added speech_recognition based on google, to transform the spoken tekst into an anwer to send to the interactive script.


To install you need following requirements :

parlai
SpeechRecognition
pipwin
pyaudio


For Parlai, please visit parl.ai

Once installed make sure that NAO robot is up and connected. Specify the IP address and port in nao.py, port will be probably 9559, for the IP of Nao, press on his belly to hear the IP.
You can also try the code with Choregraph by setting up a Virtual Robot.  Visit Softbankrobotics website to do this.

In that case the IP will be 127.0.0.1 and the port, you can check in Choregraph in the preferences/Virtual Robot tab


To start te code launch the  wanted task (Check on Parl.ai for more tasks like  Wiki talker etc....) :


The code has been tested with following commands :


python ai.py  --model-file zoo:dodecadialogue/all_tasks_mt/model

and 

python ai.py  --model-file zoo:dodecadialogue/wizard_of_wikipedia_ft/model --inference beam --beam-size 10 --beam-min-length 10 --beam-block-ngram 3 --beam-context-block-ngram 3 -t wizard_of_wikipedia










