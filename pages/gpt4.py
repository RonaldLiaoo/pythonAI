# 網頁上傳檔案元件

import streamlit as st

uploaded_file = st.file_uploader("上傳圖片", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="已上傳的圖片", width=300)
