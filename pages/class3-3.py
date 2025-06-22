import streamlit as st

st.title("自動點餐機")

# 初始化餐點清單
if "menu" not in st.session_state:
    st.session_state.menu = []

# 使用者輸入餐點
col1, col2 = st.columns(2)
with col1:
    text = st.text_input("請輸入餐點")

with col2:
    if st.button("加入"):
        if text:
            st.session_state.menu.append(text)
            st.rerun()

# 顯示點餐列表與刪除按鈕
for idx, item in enumerate(st.session_state.menu):
    col_a, col_b = st.columns([5, 1])
    with col_a:
        st.write(f"{item}")
    with col_b:
        # 每個刪除按鈕都有獨特 key
        if st.button("刪除", key=f"del_{idx}"):
            del st.session_state.menu[idx]
            st.rerun()
