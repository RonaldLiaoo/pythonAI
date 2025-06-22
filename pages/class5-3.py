import streamlit as st
import random

st.title("丟骰子遊戲")

def roll_dice(n):
    dice = []
    for i in range(n):
        dice.append(random.randint(1, 6))
    return dice

cnt = st.number_input('輸入丟骰子的次數', min_value=1, max_value=100, value=1, step=1, key='dice_count')

st.write(f"你丟了 {cnt} 次骰子，結果如下：")
dice_results = roll_dice(cnt)
st.write(dice_results)