Nao speach with Real AI

Nao from Softbank Robotics is used to talk to a human.  On the background a Python 3.7 script is running on the parl.ai python platform.  I used the tasks of https://parl.ai/projects/dodecadialogue/​.
And I added an own speech agent based on the local_human agent of parl.ai.  Just added speech_recognition based on google, to transform the spoken tekst into an anwer to send to the interactive script.


Installation procedure :

1. Download and Install python 2.7
2. Download and Install python 3.7
3. pip install parlai
4. pip install SpeechRecognition
5. pip install pipwin
6. Microsoft Visual C++ 14.0 is required. Get it with "Build Tools for Visual Studio": https://visualstudio.microsoft.com/downloads/
7. Download corresponding wheel and navigate to Download map :  https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
8. pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl


For more info on Parlai, please visit parl.ai

Once installed make sure that NAO robot is up and connected. Specify the IP address and port in nao.py, port will be probably 9559, for the IP of Nao, press on his belly to hear the IP.
You can also try the code with Choregraph by setting up a Virtual Robot.  Visit Softbankrobotics website to do this.

In that case the IP will be 127.0.0.1 and the port, you can check in Choregraph in the preferences/Virtual Robot tab


To start te code launch the  wanted task (Check on Parl.ai for more tasks like  Wiki talker etc....) :


The code has been tested with following commands :


python ai.py  --model-file zoo:dodecadialogue/all_tasks_mt/model

and 

python ai.py  --model-file zoo:dodecadialogue/wizard_of_wikipedia_ft/model --inference beam --beam-size 10 --beam-min-length 10 --beam-block-ngram 3 --beam-context-block-ngram 3 -t wizard_of_wikipedia










