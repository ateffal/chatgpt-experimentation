import streamlit as st
from streamlit_chat import message
import requests
import openai
import urllib.request
from PIL import Image
import time
import os
from pytube import YouTube
from pydub import AudioSegment
from pydub.utils import make_chunks
# from pyannote.audio import Pipeline
import pyannote.audio.pipelines
import pandas as pd

openai.api_key = st.secrets["api_key"]
pyannote_key = st.secrets["pyannote_key"]


# This function scrapes the audio from a YouTube video and saves it in the output directory
# and returns the full path of the audio
def retrieve_audio(video_link, output_dir):
    """
    This function scrapes the audio from a YouTube video and saves it in the output directory
    """
    try:
        video = YouTube(video_link)
        audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
        audio.download(output_dir)
        return output_dir  + audio.default_filename
    except:
        print("Connection error")
        return ""

def get_text():
    input_text = st.text_input("Type the link of the Youtube video", key="input")
    return input_text

def transcript_file(path_file):
    start_time = time.time()
    audio_file= open(path_file, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    trans_time = time.time() - start_time
    return transcript['text'], trans_time

def diarize_audio(path_file, from_ = 0 , to_ = 10):
    t1 = from_ * 1000 # works in milliseconds
    t2 = to_ * 60 * 1000

    newAudio = AudioSegment.from_wav(path_file)
    a = newAudio[t1:t2]
    a.export("audio.wav", format="wav")

    pipeline = Pipeline.from_pretrained('pyannote/speaker-diarization', use_auth_token=pyannote_key)
    DEMO_FILE = {'uri': 'blabal', 'audio': 'audio.wav'}
    dz = pipeline(DEMO_FILE)
    return dz
    




st.set_page_config(
    page_title="Omdena India Chapter: AI Tool for Linguistic and Psychometric Assessment")


st.image("images/Hyderabad-India-Chapter.png", caption=None,
         width=300, use_column_width=None, clamp=False, channels='RGB', output_format='auto')

st.header("AI Tool for Linguistic and Psychometric Assessment")

st.caption("Disclaimer: This application is for showcasing code pushed to Github. It is not a replacement for task-3 and task-4.")

tab1, tab2 = st.tabs(["ASR", "Text features extraction"])


with tab1:

        st.header("ASR - of a Youtube video.")
        st.text("Ex : https://www.youtube.com/watch?v=E9tXfQZx6CA&t=52s")

        user_input = get_text()

        if user_input:

                video = retrieve_audio(user_input, "")

                video_file = open(video, 'rb')
                video_bytes = video_file.read()

                st.audio(video_bytes)

                transcription, trans_time_ = transcript_file(video)

                st.text('Execution time in seconds : ' + str(trans_time_))
                st.text('[' + str(int(trans_time_/60)) +  ' minutes.]')

                st.text_area("", value= transcription, height=800)

                # dz = diarize_audio(video)

                # with open("diarization.txt", "w") as text_file:
                #     text_file.write(str(dz))

                # turns = open('diarization.txt').read().splitlines()

                # starts = []
                # ends = []
                # speakers = []

                # for turn in turns:
                #     t1, t2 = re.findall('[0-9]+:[0-9]+:[0-9]+', string=turn)
                #     speaker = re.findall('SPEAKER_[0-9][0-9]', string=turn)
                #     starts.append(t1)
                #     ends.append(t2)
                #     speakers.append(speaker[0])

                # df = pd.DataFrame({'start' : starts, 'end' : ends , 'speaker': speakers})

                # st.dataframe(data=df)
                







with tab2:

    st.header("Text features extraction. Under construction...")




