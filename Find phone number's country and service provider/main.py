import streamlit as st
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier


def track_number():
    st.title("Find Phone Number Location & Service Provider")
    st.subheader("Build with Python and Streamlit")
    number = st.text_input("Enter Your Phone Number: ", type="password")
    if st.button("Track"):
        ch_number = phonenumbers.parse(number, "CH")
        st.success("Country Name: {}".format(geocoder.description_for_number(ch_number, 'en')))
        service_provider = phonenumbers.parse(number, "RO")
        st.success("Service Provider: {}".format(carrier.name_for_number(ch_number, 'en')))


if __name__ == "__main__":
    track_number()