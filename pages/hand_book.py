import streamlit as st
import os

file_path = "markdown"
files = os.listdir(file_path)
files.sort()
for i in files:
    if i.endswith(".md"):
        with open(f"{file_path}/{i}", "r", encoding="utf-8") as file:
            content = file.read()
        with st.expander(i):
            st.write(content)
