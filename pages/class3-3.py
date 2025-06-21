import streamlit as st

st.title("自動點餐機")
number = 1

col1, col2 = st.columns(2)

with col1:
    text = st.text_input("請輸入餐點")

with col2:
    if st.button("加入", key="btn"):
        col1.text(text)
