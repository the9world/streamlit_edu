# 차트 라이브러리
# plotly : Plotly Python Graphing Library (pip install plotly==5.14.)
# altair viz : Vega-Altair

import streamlit as st
import plotly as px
import altair as alt
import pandas as pd 
import matplotlib.pyplot as plt

def main() :
    st.title('내 앱 대시보드') # web에 띄우고 싶은 글자 st.title("글") : text : st.text("글")
    
    df1= pd.read_csv('data/lang_data.csv')
    st.dataframe(df1)
    st.write(df1. shape) # st.write(["hi", df1, shape]) 이거 신기하네
    st.text(["행렬 text: ",df1. shape]) 
    
    
    print(df1.columns[1:])
    lang_list= df1.columns[1:]
    choice_list= st.multiselect('언어를 선택하세요', lang_list)
    
    # 사용자가 아무것도 선택하지 않았을 때 : empty 처리
    print(choice_list)
    
    if len(choice_list) > 0 :
        choice_df= df1[choice_list]
        st.dataframe(choice_df)
        
        # streamlit이 제공하는 라인차트
        st.line_chart(choice_df)
        # stramlit이 제공하는 영역차트
        st.area_chart(choice_df)
    
    
    df2 = pd.read_csv('data/iris.csv')
    
    # streamLit이 제공하는 bar차트
    df3 = df2[['sepal_length', 'sepal_width']]
    st.bar_chart(df3)
    
    # Altair 이용 :  Cahrt : "C"대문자 확인
    chart = alt.Chart(df2).mark_circle().encode(
        x = 'petal_length',
        y = 'petal_width',
        color = 'species')
    st.altair_chart(chart)
        
    # streamlit의 map 차트
    df4 = pd.read_csv('data/location.csv', index_col=0)
    print(df4) # lat(latitude), lon(longitude) : 위'경도
    st.map(df4, zoom=4) # zoom 숫자가 작을수록 멀다
    
    df5 = pd.read_csv('data/prog_languages_data.csv', index_col=0)
    st.dataframe(df5)
    
    # plotly 의 pie 차트 (파이차트는 비율을 보고 싶을 때)
    fig1= px.pie(df5, 'lang', 'Sum', title='각 언어별 비율')
    st.plotly_chart(fig1)
    
    # plotly 의 bar 차트
    fig2 = px.bar(df5, x='lang', y='Sum')
    st.plotly_chart(fig2)

if __name__ == '__main__': # app 실행 한게 main이면 위에 있는 main 함수를 실행하라.
    main()