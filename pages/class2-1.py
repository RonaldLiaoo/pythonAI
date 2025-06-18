import streamlit as st

number = st.number_input("請輸入數字", step=1)
# step=1 表示單位以及增減的數字, min_value 表示最小值, max_value 表示最大值
st.write(f"你輸入的數字是：{number}")

score = st.number_input("Please input score: ", step=1, min_value=0, max_value=100)
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"
st.write("Your grade is: ", grade)
