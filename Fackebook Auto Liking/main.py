import pyautogui
import time
import webbrowser as wb
import streamlit as st


def fb_auto_liking():
	st.title("Facebook Post Auto Reacting")
	st.subheader("Build with Python and pyautogui")
	link = st.text_input("Enter Facebook link or any Profile link: ")
	if st.button("Start Reacting"):
		pyautogui.FAILSAFE = False
		wb.open(link)
		for i in range(11):
			time.sleep(5)
			pyautogui.press('j')
			time.sleep(3)
			pyautogui.press('l')
			pyautogui.press('right')
			pyautogui.press('enter')


if __name__ == "__main__":
	fb_auto_liking()
