import streamlit as st
import os

file_path = "image"
files = os.listdir(file_path)
st.write(files)

size = st.number_input("圖片大小", step=50, min_value=50, max_value=500, value=300)

for image in files:
    if image.endswith(".jpg") or image.endswith(".png"):
        st.image(f"{file_path}/{image}", width=size)
