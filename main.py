import streamlit as st

st.write("Forest Fire Prediction")

name = st.text_input("Enter Your name", "Type Here ...")

if(st.button('Submit')):
    result = name.title()
    st.success(result)