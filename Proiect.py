import os
import time
import sys
import speech_recognition as sr
from gtts import gTTS
from scipy.io import wavfile
import numpy as np
from random import seed
from random import randint
seed()

cale = r'C:\Users\Raluca\Desktop\Proiect'
raspunsuri=[]
raspunsuri = os.listdir('raspunsuri')
for i in [1,2,3,4,5]:
    
    print("Rostiti comanda")
    sprec = sr.Recognizer()
    with sr.Microphone() as source:
        myaudio = sprec.listen(source)

        rez = sprec.recognize_google(myaudio,language = "ro-RO",show_all=False)
    print(rez)

    lista_intrebare = rez.split()
    time.sleep(5)
    

    if "stop" in lista_intrebare:
        raspuns1=[[5,4,1,3],[6]]
        valoare_raspuns=randint(0,1)
        fs,r2 = wavfile.read(os.path.join('raspunsuri',raspunsuri[raspuns1[valoare_raspuns][0]]))
        for j in raspuns1[valoare_raspuns][1:]:
            _,data2 = wavfile.read(os.path.join('raspunsuri',raspunsuri[j]))
            r2 = np.concatenate((r2,data2))
        wavfile.write('raspuns1.wav',fs,r2)
        mymono2 = os.path.join(cale,'raspuns1.wav')
        myaudiofile2 = sr.AudioFile(mymono2)
        with myaudiofile2 as source:
            myaudio2 = sprec.record(myaudiofile2)
            text = sprec.recognize_google(myaudio2,language = "ro-RO",show_all=False)
        print (text)
        raspuns1 = gTTS(text, lang ='ro',slow = False)
        raspuns1.save('raspuns1.mp3')
        os.system('raspuns1.mp3')
        time.sleep(5)
        continue
    
    
    if "revedere" in lista_intrebare:
        print("Va multumim! O zi buna!")
        sys.exit()
        
        
