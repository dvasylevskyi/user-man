import streamlit as st

st.title("🎈 Dmytro")
st.write("My first python app")
name = st.text_inout("Please enter your name")
st.write("Welcome ", name)
