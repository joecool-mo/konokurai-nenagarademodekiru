import streamlit as st

#やりたいこと
#事故らないシュミレーター
#変数的なもの　睡眠時間　起き続けている時間　日中の活動の激しさ　お助けアイテム，もの，人　変わってもらえる人　乗っている人数　乗れる人数＋急いでいるか
#結果　事故　死亡　運転手変更　遅刻　逮捕　ちょっと危なかった　到着
st.title('nemai')
st.subheader('運転時に事故るかどうかをシュミレートできます')
st.subheader('1人～8人乗りまでの運転に対応しています')
st.subheader('入力内容によって10種類の演算結果が出ます')
st.subheader('ぜひご活用ください')

text=st.text_input('あなたの名前を教えてください')
st.write('あなたの名前は'+text+'です')

text_a=st.text_input('睡眠時間を教えてください')
st.write('睡眠時間：'+text_a+'時間')

text_b=st.text_input('起きてから今まで何時間経ったかを教えてください')
st.write('連続起床時間：'+text_b+'時間')

option=st.selectbox('今日の活動について教えてください',list(['激しく運動した','軽い運動をした','運動はしていない','一歩も動いた記憶がない']))
st.write('あなたが選択したのは'+option+'です')
if option=='激しく運動した':
    text_c=4
if option=='軽い運動をした':
    text_c=3
if option=='運動はしていない':
    text_c=2
if option=='一歩も動いた記憶がない':
    text_c=1

option_have=st.selectbox('眠気を覚ます物を持っていますか？',list(['なし','エナジードリンク','うるさい友達','いびきのうるさい友達','スマートフォン','音楽']))
st.write('あなたが選択したのは'+option_have+'です')
if option_have=='なし':
    text_d=4
if option_have=='エナジードリンク':
    text_d=2
if option_have=='うるさい友達':
    text_d=-2
if option_have=='いびきのうるさい友達':
    text_d=1
if option_have=='スマートフォン':
    text_d=0

option_change=st.selectbox('運転を変わってくれる人はいますか？',list(['いる','いない']))
st.write('あなたが選択したのは'+option_change+'です')
if option_change=='いる':
    text_e=-4
if option_change=='いない':
    text_e=0

option_hurry=st.selectbox('今回の運転は急いでいますか？',list(['急いでいる','急いでいない']))
st.write('あなたが選択したのは'+option_hurry+'です')
if option_hurry=='急いでいる':
    text_g=2
if option_hurry=='急いでいない':
    text_g=0

option_can=st.selectbox('何人乗りの車ですか？',list(['1','2','3','4','5','6','7','8',]))
st.write('あなたが選択したのは'+option_can+'です')

option_actual=st.selectbox('車に乗っているのは何人ですか？',list(['1','2','3','4','5','6','7','8',]))
st.write('あなたが選択したのは'+option_actual+'です')
if option_actual=='1':
    text_f=2
if option_actual in ['2','3','4']:
    text_f=0
if option_actual in['4','5','6','7','8']:
    text_f=-2



st.title('演算結果')

#数字が大きいほど事故りやすいようにする
st.write(10-int(text_a)+int(text_b)-6+int(text_c)+int(text_d)+int(text_e)+int(text_f)+int(text_g))

text_x=(10-int(text_a)+int(text_b)-6+int(text_c)+int(text_d)+int(text_e)+int(text_f)+int(text_g))

if int(option_can)-int(option_actual)<0:
    st.header('逮捕')
    st.write('乗りすぎです')
    st.write('反省してください')

elif option_have=='スマートフォン' and int(text_x)%2==0:
    st.header('逮捕')
    st.write('バレないとでも思いましたか？')
    st.write('事故らなくてよかったですね')

elif text_x>9 and option_change=='いる':
    st.header('運転手交代')
    st.write('己の無力さに泣いてください')
    st.write('あなたはきっとまだ強くなれます')

elif text_x>9 and option_change=='いる':
    st.header('運転手交代')
    st.write('己の無力さに泣いてください')
    st.write('あなたはきっとまだ強くなれます')

elif option_actual=='1' and option_have in ['うるさい友達','いびきのうるさい友達']:
    st.write('，，，')
    st.write('見苦しいですね')
    st.write('あなたに友達がいないことはわかってるんです')
    st.write('強がらないで')
    st.write('1人だってたのしいことありますよ')
    st.write('ほら元気出して')
    st.write('私が友達になってあげますから')

elif text_x<10:
    st.header('運転成功')
    st.write('無事に目的地まで到着しました')

elif 10>text_x>7 and option_hurry=='急いでいない':
    st.header('遅刻')
    st.write('休憩したため事故らずに着きましたね')
    st.write('ですがあなたへの信頼は地に落ちてしまいました')

elif text_x>9:
    st.header('運転失敗')
    st.write('ドンマイ，大破')

if option_can==1:
    st.write('そんな事よりも珍しい車に乗っていますね')
    st.write('goodです')

if int(text_b)>24:
    st.write('普通に早く寝てください')
    st.write('しんぱいだヨ')

if text_c==1:
    st.write('そんなことより車なんて使わずに歩けやデブ')
    st.write('演算するの嫌でした')




