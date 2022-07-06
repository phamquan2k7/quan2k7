import requests
import streamlit as st
from streamlit_lottie import st_lottie
import streamlit as st
st.set_page_config(page_title="My web page" , page_icon=":tada:",layout="wide")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .css-1rs6os {visibility: hidden;}
            .css-17ziqus {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_o6spyjnc.json")
lottie_hi = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_z7DhMX.json")
with st.container():
    st.write("---")
    left_column , right_column = st.columns(2)
    with left_column:
        st.subheader("Hi , I am Quân :wave:")
        st.title("A student from Viet Nam")
        st.write("I am passionate about finding ways to use Python to be more and more effective")
        st.write("[learn more>](https://www.youtube.com/channel/UC3opf8J6aPKbP4EZj892rwQ)")
    with right_column:
        st_lottie(lottie_hi , height=300)
with st.container():
    st.write("---")
    left_column , right_column = st.columns(2)
    with left_column:
         st.header("What I do")
         st.write("##")
         st.write("""
         On my YouTube channel I am creating tutorials for people who:
         - are looking for a way to leverage the power of Python in their day-to-day work.
         - are working with Excel and found themselves thinking - "there has to be a better way.""" 
         )
         st.write("[learn more>](https://www.youtube.com/channel/UC3opf8J6aPKbP4EZj892rwQ)")
    with right_column:
        st_lottie(lottie_hello , height=300,key="coding")
with st.container():
    st.write("---")
    st.header("contact with me")
    st.write('##')
    contact_form = """
    <form action="https://formsubmit.co/quanpham122007@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder ="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Details of your problem"></textarea>
    <button type="submit">Send</button>
</form>
"""
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")
left_column , right_column = st.columns(2)
with left_column :
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()