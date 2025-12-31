import pandas as pd
import streamlit as st
import datetime
import random

st.title("オットリ―のアプリ部屋")
st.subheader("アプリケーションメニュー")

# ボタンごとに色を変えるCSS 
# st.markdown("""
#             <style> /* 左ボタン（緑） */ 
#             div[data-testid="stButton"][id="btn1"] button { 
#             background-color: #4CAF50; 
#             color: white; 
#             border-radius: 8px; 
#             height: 50px; width: 100%; font-size: 18px; border: none; } 

#             /* 真ん中ボタン（青） */ 
#             div[data-testid="stButton"][id="btn2"] button { 
#             background-color: #2196F3; color: white; border-radius: 8px; height: 50px; width: 100%; 
#             font-size: 18px; border: none; } 

#             /* 右ボタン（オレンジ） */
#              div[data-testid="stButton"][id="btn3"] button { 
#             background-color: #FF9800; color: white; border-radius: 8px; 
#             height: 50px; width: 100%; font-size: 18px; border: none; } 
#             </style> 
#             """, unsafe_allow_html=True) 

# left, middle, right = st.columns(3)
# with left: 
#     if st.button("適職診断", key="btn1"): 
#         st.switch_page("pages/app1.py") 
# with middle: 
#     if st.button("ハッピー占い", key="btn2"): 
#         st.switch_page("pages/page2.py") 
# with right: 
#     if st.button("Material button", key="btn3"): 
#             st.switch_page("pages/page3.py")


left, middle, right = st.columns(3)
if left.button("適正職業診断",icon= "👰" ,width="stretch"):
    st.switch_page("pages/app1.py")
if middle.button("ハッピー占い", icon="😃", width="stretch",type="secondary"):
    st.switch_page("pages/app2.py")
if right.button("作成中", icon=":material/mood:", width="stretch"):
    right.markdown("近日公開")


#複数ページ実装
# st.page_link("pages/app1.py", label="ページ1")