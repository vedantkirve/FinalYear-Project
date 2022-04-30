import speech_recognition as sr
import matplotlib.pyplot as plt
from easygui import *
from PIL import Image
import string
ads = []
def func():
        r = sr.Recognizer()
        
        arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z']
        with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source) 
                i=0
                while True:
                        print("I am Listening")
                        audio = r.listen(source)
                        try:
                                a=r.recognize_google(audio)
                                a = a.lower()
                                print('You Said: ' + a.lower())
                                
                                for c in string.punctuation:
                                    a= a.replace(c,"")
                                    
                                if(a.lower()=='goodbye' or a.lower()=='good bye' or a.lower()=='bye'):
                                        print("oops!Time To say good bye")
                                        break
                                
                                else:
                                    for i in range(len(a)):
                                                    if(a[i] in arr):
                                            
                                                            ImageAddress = 'letters/'+a[i]+'.jpg'
                                                            ads.append(ImageAddress)
                                                            
                                                    else:
                                                            continue

                        except:
                                print(" ")
                       
print(ads)
