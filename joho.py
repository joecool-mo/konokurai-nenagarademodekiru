import streamlit as st
#streamlit run ファイル名   .pyで最初の実行  
st.title('はじめてのすとりーむりっと')
st.title('これから作品を作っていきまっす')

#名前を表示させる
text=st.text_input('あなたの名前を教えてください')
st.write('あなたの名前は，'+text+'です')

#調子のシークバーを作る
conndition=st.slider('あなたの今の調子は？',0,100,50)
                         #最小値,最大値,スタート位置
st.write('コンディション：',conndition)

option=st.selectbox('好きな数字を教えてください',list(['１番','2番','3番','4番']))
st.write('あなたが選択したのは,'+option+'です')

import time
st.sidebar.write('プログレスバーの表示')

latest_iteration=st.empty()#空コンテンツと一緒に変数を作成
bar=st.progress(0)#プログレスを作る 値は0

for i in range(100):
    latest_iteration.text(f'lteration{i+1}')#空のIterationにテキストを入れていく
    bar.progress(i+1)#barの中身をぐいぐい増やしていく
    time.sleep(0.01)


left_column,right_column=st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')


from PIL import Image
img=Image.open('えがお亀.jpg')

st.image(img,caption='生活場面',use_column_width=True)

#地図について
import pandas as pd
import numpy as np

df = pd.DataFrame(
np.random.rand(100,2)/[50,50] + [35.69,139.70],
columns = ['lat','lon',]#lat lon 緯度と経度
)
#緯度と経度から地図に書き込む
st.map(df)
st.table(df)