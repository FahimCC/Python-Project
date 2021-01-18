import pyautogui
import time
import webbrowser as wb
import streamlit as st


def auto_typing():
    st.title("Auto Typing of Same Text")
    st.subheader("Build with Python, pyautogui and webbrowser")
    text = st.text_input("Enter the text: ")
    count = st.text_input("How much time the text will be repeated: ")
    if st.button("Start Typing"):
        counter = 0
        st.success("N.B. Please open notepad/text editor writing will be started within 10s.")
        time.sleep(10)
        while counter != int(count):
            st.success(counter)
            time.sleep(3)
            # What do you want to write in many times.
            pyautogui.typewrite(text)
            pyautogui.press("enter")
            counter = counter + 1


if __name__ == "__main__":
    auto_typing()
