import streamlit as st
from streamlit_chat import message
import requests
import openai
import urllib.request
from PIL import Image
import time
import os
from pytube import YouTube

openai.api_key = st.secrets["api_key"]


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
#     print("Execution time : %s seconds." % (time.time() - start_time))
    return transcript['text']


st.set_page_config(
    page_title="Omdena India Chapter: AI Tool for Linguistic and Psychometric Assessement")


st.image("images/Hyderabad-India-Chapter.png", caption=None,
         width=300, use_column_width=None, clamp=False, channels='RGB', output_format='auto')

st.header("AI Tool for Linguistic and Psychometric Assessement")

st.caption("Disclaimer: This application is for showcasing code pushed to Github. It is not a replacement for task-3 and task-4.")

tab1, tab2 = st.tabs(["ASR", "Text features extraction"])


with tab1:

        st.header("ASR - of a Youtube video")

        user_input = get_text()

        if user_input:

                video = retrieve_audio(user_input, "")

                video_file = open(video, 'rb')
                video_bytes = video_file.read()

                st.audio(video_bytes)

                transcription = transcript_file(video)

                st.text(transcription)






with tab2:

    st.header("Text features extraction. Under construction...")




