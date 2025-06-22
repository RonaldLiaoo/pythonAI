import streamlit as st
import random

st.title("猜數字遊戲")
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)

number = st.text_input("請輸入數字 (1-100)：")
number = int(number) if number.isdigit() else 0  # 確保輸入是數字

if number > st.session_state.answer:
    st.write("再大一點")
elif number < st.session_state.answer:
    st.write("再小一點")
elif number == st.session_state.answer:
    st.write("猜中了")
    st.session_state.answer = random.randint(1, 100)
