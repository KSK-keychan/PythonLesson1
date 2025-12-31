import streamlit as st
import random
from PIL import Image

print("りんご")

st.title("ハッピー占い")
st.header("あなたの運勢を占います！")

if st.button("占いスタート"):
    randomNumber = random.randint(0,4)

    if randomNumber == 0:
        st.badge("大吉")
        st.balloons()
        st.balloons()
        st.write("迷ったら辛いと思う選択肢を選びなさい")

    elif randomNumber == 1:
        st.badge("中吉")
        st.balloons()
        st.write("人生の分岐点が1か月後に訪れるでしょう")

    elif randomNumber == 2:
        st.badge("小吉")
        st.balloons()

    elif randomNumber == 3:
        st.badge("吉")
        st.write("今年のラッキーアイテムは「くまのぬいぐるみ」")
        st.link_button("ラッキーアイテム","https://fulmo-img-server.com/yawaraka-collection/d496f3eb22ea4dd5b38a947ac9929f45.jepg")
    else :
        st.badge("凶")
        st.link_button("不幸だったあなたはここを押して！","https://i.pinimg.com/736x/9f/da/e4/9fdae46ce8f2976bec5bf1e8ccbc8227.jpg")