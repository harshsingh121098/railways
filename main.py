import os
import pandas as pd
from gtts import gTTS
from pydub import AudioSegment

def textTospeech(text,filename):
    pass

def mergeaudios(audios):  #returns pydubs audio segment
    pass

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')
    
def generateannouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    

if __name__== "__main__":
    print("genarating skeleton..")
    generateSkeleton()
    print("now generating announcement..")
    generateannouncement("Railway.xlsx")
