import pandas as pd
import streamlit as st
import datetime
import random

st.title("オットリ―のアプリケーションメニュー")

left, middle, right = st.columns(3)
if left.button("適職診断", width="stretch", color ="green"):
    st.switch_page("pages/app1.py")
if middle.button("ハッピー占い", icon="😃", width="stretch",type="secondary"):
    st.switch_page("pages/page2.py")
if right.button("Material button", icon=":material/mood:", width="stretch"):
    right.markdown("You clicked the Material button.")


#複数ページ実装
# st.page_link("pages/app1.py", label="ページ1")