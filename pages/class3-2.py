import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)  # 2欄
col1.button("按鈕1")
col2.button("按鈕2")

with col1:
    st.markdown("這是欄1")
    st.button("左邊按鈕")
with col2:
    st.markdown("這是欄2")
    st.button("右邊按鈕")
