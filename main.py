import streamlit as st
import time

'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

left_column, right_column = st.columns(2)

button = left_column.button("右からカラムに文字を表示")
if button:
    right_column.write('わーお')

# option = st..text_input("あなたの趣味を教えて")
# 'あなたの好きな数字は',option,'です。'


#スライダー
# condition = st..slider('あなたの今の調子は？',0,100,50)
# '数値；',condition

# if st.checkbox('レイアウト有無'):
#     Image = Image.open('このすば.jpg')
#     st.image(Image, caption='konosuba')

# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40]
# })

#マップを作成
# df = pd.DataFrame(
#     [[35.53136, 139.69695]],
#     columns = ['lat', 'lon']
# )

# st.map(df, size=5, color="#ff5900")

#サイドバーにメニューを作る 
# menu = st.sidebar.selectbox( "メニュー", ["Log_out", "settings", "最新情報", "過去情報", "search"] ) 
# st.write("選択中のメニュー:", menu) 
# st.table(df.style.highlight_max(axis=0))

