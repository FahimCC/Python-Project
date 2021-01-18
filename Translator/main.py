import streamlit as st
import goslate


def en_to_bn_translator():
    st.title("Translate English to Bangla")
    st.subheader("Build with Python and goslate module")
    text = st.text_input("Enter Your Text: ")
    if st.button("Translate"):
        obj = goslate.Goslate()
        translated_text = obj.translate(text, "bn")
        st.success("{}".format(translated_text))


if __name__ == "__main__":
    en_to_bn_translator()
