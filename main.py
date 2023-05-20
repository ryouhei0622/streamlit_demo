import time

import pandas as pd
import streamlit as st

st.title("Streamlit 超入門！！！")

st.write("プログレスバーの表示")

"Start!!!"
iteration = st.empty()
bar = st.progress(0)

for i in range(1, 101):
    iteration.write(f"iteration {i}")
    bar.progress(i)
    time.sleep(0.01)

"Done!!!!"

left_column, right_collumn = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_collumn.write("ここは右カラム")
    # button = False

expander = st.expander("お問い合わせ")
expander.write("ここにお問い合わせ内容を記述する")
