import streamlit as st
from streamlit_chat import message
import requests
import openai
import urllib.request
from PIL import Image

openai.api_key = st.secrets["api_key"] 



# def query(payload):
#   response = requests.post(API_URL, headers=headers, json=payload)
#   return response.json()


def get_text():
    input_text = st.text_input("What is your question?", key="input")
    return input_text


# def model_response(question):
#     start_sequence = "A:"
#     restart_sequence = "\n\nQ: "
#     response = openai.Completion.create(
#         model=st.secrets["model"],
#         api_key=st.secrets["api_key"],
#         prompt=restart_sequence+question+'\n\n###\n\n',
#         temperature=0,
#         # max tokens as response
#         max_tokens=100,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0,
#         # if you insert '.' or new line this means you quit the chat. so do not insert a "." or a new line at the end of your question
#         stop=[".", "\n"]
#     )

#     return response['choices'][0]['text']


def model_response(question):
    start_sequence = "A:"
    restart_sequence = "\n\nQ: "
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=restart_sequence+question+'\n\n###\n\n',
        temperature=0,
        # max tokens as response
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        # if you insert '.' or new line this means you quit the chat. so do not insert a "." or a new line at the end of your question
        stop=[".", "\n"]
    )

    return response['choices'][0]['text']



st.set_page_config(
    page_title="Omdena Lublin Chapter: Financial Chatbot",
    page_icon="https://i.ibb.co/ZYG59cp/omdena-transparent.png"
)


st.image("https://i.ibb.co/H2z983v/Omdena-Lublin-Chapter.jpg", caption=None,
         width=300, use_column_width=None, clamp=False, channels='RGB', output_format='auto')

st.header("AI Tool for Linguistic and Psychometric Assessemnt")

st.caption("Disclaimer: This application is for showcasing code pusued to Github. It is not a replacement for task-3 and task-4.")

tab1, tab2, tab3 = st.tabs(["Ask question", "Summarization", "Classification"])

with tab1:

    st.markdown(
        "Wondering how to  improve your soft skills ? Here is the solution!")

    st.markdown("You can ask it questions like:")

    st.markdown(
        "***How to have clear communication ?*** ***What is active listenning ?*** ***How to be a good listener ?***")


    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []


    user_input = get_text()


    if user_input:
        output = model_response(user_input)
        st.session_state.past.append(user_input)
        # st.session_state.generated.append(output["generated_text"])
        st.session_state.generated.append(output)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key=str(i))
            message(st.session_state['past'][i],
                    is_user=True, key=str(i) + '_user')

with tab2:

    st.header(
        "Text Summarizationunder construction....")

    title = st.text_input('Text to summarize :')
    


with tab3:

    st.header(
        "Classification under construction....")
    title = st.text_input('Text classify :')
