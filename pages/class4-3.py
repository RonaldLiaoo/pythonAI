import streamlit as st
import os
import time

st.title("購物平台")

if "product" not in st.session_state:
    st.session_state.product = {}

number = st.number_input("欄位數：", step=1, min_value=1, max_value=4, value=3)

file_path = "image"
files = os.listdir(file_path)

for img in files:
    if img[:-4] not in st.session_state.product:
        st.session_state.product[img[:-4]] = {
            "image": f"{file_path}/{img}",
            "price": 10,
            "stock": 10,
        }

cols = st.columns(number)

index = 0
for name, detail in st.session_state.product.items():
    with cols[index % number]:
        st.image(st.session_state.product[name]["image"], use_container_width=True)
        st.write(name)
        st.write(f"價格：${st.session_state.product[name]['price']}")
        st.write(f"庫存：{st.session_state.product[name]['stock']}")

        if st.button("購買", key=name):
            if st.session_state.product[name]["stock"] <= 0:
                st.error(f"{name}已售完")
            else:
                st.session_state.product[name]["stock"] -= 1
                st.success(f"已購買 {name}")
                time.sleep(1)
                st.rerun()
    index += 1

cola, colb = st.columns(2)
with cola:
    selected_product = st.selectbox("選擇商品", list(st.session_state.product.keys()))
with colb:
    add_num = st.number_input(
        "輸入購買數量", min_value=1, max_value=10, value=1, step=1
    )

if st.button("新增"):
    st.session_state.product[selected_product]["stock"] += add_num

for name, detail in st.session_state.product.items():
    st.write(f"{name}：{st.session_state.product[name]['stock']}")
