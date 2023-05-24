import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() :
    st.title('내 앱 대시보드') # web에 띄우고 싶은 글자 st.title("글") : text : st.text("글")

    df = pd.read_csv('data/iris.csv')
    st.dataframe(df)
    
    # sepal_length, sepal_width 의 관계를 차트로 -> scatter // plt.show()는 주피터용
    
    fig = plt.figure() #여기부터 차트 영역이다?
    plt.scatter(data=df, x='sepal_length', y='sepal_width')
    plt.title('sepal length VS width')
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    st.pyplot(fig)
    
    fig2= plt.figure()
    sns.regplot(data= df, x='sepal_length', y='sepal_width') # regression(리그레션): 회귀
    st.pyplot(fig2)
    
    correlation = df[['sepal_length', 'sepal_width']].corr() # Correlation(corr): 상관분석: 어떤 선형적 관계를 갖고 있는 지를 분석하는 방법
    st.dataframe(correlation) # 피어슨 상관 계수: -1~0~1로 표현 https://ko.wikipedia.org/wiki/%EC%83%81%EA%B4%80_%EB%B6%84%EC%84%9D

    # sepal_length 로 히스토그램 그리자
    # bin의 갯수는?
    fig3 = plt.figure(figsize= (10, 4) ) # 가로, 세로 사이즈
    plt.subplot(1, 2, 1) # 1행 2열 중에 1번 차트는
    plt.hist(data=df, x='sepal_length', rwidth=0.8, bins=20) # rwidth 간격, bins= 그래프수
    plt.subplot(1, 2, 2) # 1행 2열 중에 2번 차트는
    plt.hist(data=df, x='sepal_length', rwidth=0.8, bins=20) # rwidth 간격, bins= 그래프수
    st.pyplot(fig3)
    
    # species 컬럼에는 종에 대한 정보가 들어있다.
    # 각 종별로 몇개씩의 데이터가 있는지 차트로 나타내시오.
    
    st.dataframe(df['species'].value_counts() ) # 몇개씩 있는지
    
    fig4= plt.figure()
    sns.countplot(data=df, x='species')
    st.pyplot(fig4) # fig1~ fig4가 정의되는 원리 모르겠음

    ## 데이터프레임의 차트 그리는 코드도 실행 가능 ( pandas )
    fig5= plt.figure()
    df['species'].value_counts().plot(kind='bar') # df plot 디폴트는 선 그래프
    st.pyplot(fig5)

    # 데이터 프레임의 자체 plot 함수는 streamlit 에서 안됨.
    # fig6= plt.figure()
    # df.plot()
    # st.pyplot(fig6)

    fig7= plt.figure()
    df['sepal_length'].hist(rwidth=0.8) # 색(color)
    st.pyplot(fig7)

if __name__ == '__main__': # app 실행 한게 main이면 위에 있는 main 함수를 실행하라.
    main()