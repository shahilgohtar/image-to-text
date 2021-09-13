import cv2
from PIL import Image
import pytesseract
from time import sleep
from gtts import gTTS
import os
import subprocess
from googletrans import Translator
import urllib.request
import numpy as np
import playsound
import pyttsx3
import subprocess

translator = Translator()


url = 'http://192.168.230.78:8080/shot.jpg'

IMAGE_FILE = 'charimage.jpg'

inputlang = 'en'
frame = 10
language="English"
print("language you enter is "+language)

if (language == "Tamil"):
    inputlang = 'ta'
    
elif (language == "English"):
    inputlang = 'en'

elif (language == "Hindi"):
    inputlang = 'hi'

   

    
while frame >1:
    print("Reading")
    try:
        imgResp=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgNp,-1)
    except:
        print("URL NOT opened stream video")
        break

    cv2.imshow('image',img)
    cv2.waitKey(1)
    frame = frame -1
    sleep(.5)
print("writing img")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('image',gray)
cv2.waitKey(1)
cv2.imwrite(IMAGE_FILE, gray)
sleep(1)
img = cv2.imread(IMAGE_FILE)
print("conv img to txt")
words = pytesseract.image_to_string(img, lang = "eng")
print(words)
wrd=str(words)
sleep(2)
    
if (not words):
    words = "No character recognized"

words = translator.translate(wrd,dest="hi")
print("Translated OUTPUT:%s" % words.text)
    
        
print("playing audio")
tts = gTTS(text=words.text,lang="en")
tts.save("speech.mp3")
sleep(1)
import subprocess
sound_program = "E:/VLC/vlc.exe"
sound_file = "E:/project/speech.mp3"
subprocess.call([sound_program, sound_file])


cv2.destroyAllWindows()
print("Exiting")



