import time

import pandas as pd
import streamlit as st

st.title("Streamlit 超入門！！！")

st.write("プログレスバーの表示")

"Start!!!"
num = 0
iteration = st.empty()
bar = st.progress(0)

if num == 0:
    for i in range(1, 101):
        iteration.write(f"iteration {i}")
        bar.progress(i)
        time.sleep(0.01)

"Done!!!!"

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
# if button:
#     right_collumn.write("ここは右カラム")
# button = False
if button:
    if "show_text" not in st.session_state:
        st.session_state["show_text"] = True

    if st.session_state["show_text"]:
        right_column.write("ここは右カラム")
        st.session_state["show_text"] = False

expander = st.expander("お問い合わせ")
expander.write("ここにお問い合わせ内容を記述する")

text = st.text_input("表示したい単語を入力してください")

if "text_list" not in st.session_state:
    st.session_state["text_list"] = []

col1, col2 = st.columns(2)

with col1:
    if st.button("追加", key=2):
        st.session_state["text_list"].append(text)

with col2:
    if st.button("削除", key=3):
        try:
            st.session_state["text_list"].remove(text)
        except ValueError as e:
            print("ValueError!!")


for output_text in st.session_state["text_list"]:
    st.write("", output_text)

num += 1
print(num)
