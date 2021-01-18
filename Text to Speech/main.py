import streamlit as st
import pyttsx3


def text_to_speech():
    st.title("Text to Speech")
    st.subheader("Build with Python and pyttsx3")
    talk = st.text_input("Enter Your Text :")
    friend = pyttsx3.init()

    if st.button("Male Voice"):
        pass
    elif st.button("Female Voice"):
        voices = friend.getProperty('voices')
        friend.setProperty('voice', voices[1].id)

    friend.say(talk)
    friend.runAndWait()


if __name__ == "__main__":
    text_to_speech()