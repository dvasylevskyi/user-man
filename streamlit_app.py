import streamlit as st

st.title("🎈 Dmytro")
st.write("The best site ever")
name = st.text_input("Please enter your name")
birthday = st.text_input("Please enter your birthday date")
st.write("Welcome ", name)
