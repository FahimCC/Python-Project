import pyshorteners
import streamlit as st


st.title("Any link shorter")
st.subheader("Build with Python, Streamlit and pyshorteners")
link = st.text_input('Enter the link: ')
if st.button('Short'):
    short_obj = pyshorteners.Shortener()
    short_link = short_obj.tinyurl.short(link)
    print(short_link)
    st.success('Short link {}'.format(short_link))

