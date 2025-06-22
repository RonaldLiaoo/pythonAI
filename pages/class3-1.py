import streamlit as st

st.write(
    """
import streamlit as st
import os

folderPath = "markdown"
files = os.listdir(folderPath)
files_name = []

for f in files:
    if f.endswith(".md"):
        files_name.append(f)
    print(files_name)

for f in files_name:
    with open(f"{floderpath}/{f}", "r", encoding="utf-8") as file:
        content = file.read()
    with st.expander(f[:-3]):
        st.markdown(content)
    """)