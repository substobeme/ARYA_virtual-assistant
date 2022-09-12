import wikipedia as wk
import os
import pafy
import requests
import time
import random
import re,subprocess,urllib.parse,urllib.request
import pyttsx3 as pt
import speech_recognition as sp
import webbrowser as wb
import datetime
import pyjokes
def sptotext():
    recognizer= sp.Recognizer()
    with sp.Microphone() as source:
        print("Plz say")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            hrd= recognizer.recognize_google(audio)
            print(f"I heard this {hrd}")
            return hrd
        except sp.UnknownValueError:
            print("failed")
def texttosp(x):
    engine=pt.init()
    vc= engine.getProperty('voices')
    engine.setProperty('voice',vc[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
import vlc
def video(name):
    qs=urllib.parse.urlencode({"search_query":name})
    formaturl=urllib.request.urlopen("https://www.youtube.com/results?"+qs)
    search_results=re.findall(r"watch\?v=(\S{11})",formaturl.read().decode())
    clip="https://www.youtube.com/watch?v="+"{}".format(search_results[0])
    vd=pafy.new(clip)
    tm= vd.length
    vdlnk=vd.getbest()
    media=vlc.MediaPlayer(vdlnk.url)
    media.play()
    n=int(input("1 to stop"))
    if n==1:
        media.stop()
def wiki(sr):
    tell=wk.summary(sr,sentences=3)
    print(tell)
    texttosp(tell)
def google(gg):
    wb.open('https://www.google.com/search?q='+gg)
def joke():
    jk=pyjokes.get_joke(language="en",category="all")
    texttosp(jk)
def time_tell():
    tm=datetime.datetime.now()
    d= tm.strftime("%A")
    H= tm.strftime("%I")
    M=tm.strftime("%M")
    tel= f"Today is {d}, and it is {H} hours and {M} minutes now"
    print(tel)
    texttosp(tel)