import streamlit as st

st.title("點餐機")

# 初始化餐點清單
if "menu" not in st.session_state:
    st.session_state.menu = []

# 使用者輸入餐點
col1, col2 = st.columns([5, 1])
with col1:
    text = st.text_input("請輸入餐點")
with col2:
    if st.button("加入"):
        st.session_state.menu.append(text)
        st.rerun()

st.write("### 購物籃")

# 顯示點餐列表與刪除按鈕
for i in range(len(st.session_state.menu)):
    col_a, col_b = st.columns([5, 1])
    with col_a:
        st.write(st.session_state.menu[i])
    with col_b:
        if st.button("刪除", key=f"del_{i}"):
            st.session_state.menu.pop(i)
            st.rerun()
