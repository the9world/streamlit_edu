# 가상환경 세팅
# $ python --version  버전확인  
# $ conda create -n app_dash python=3.9 openssl numpy scipy matplotlib ipython scikit-learn pandas pillow jupyter seaborn  
# $ pip install streamlit 
# $ pip install plotly==5.14.
# 스트림릿 웹 접속 streamlit run 파일명
# import plotly.express as px

import streamlit as st # error 밑줄이 있어야 정상
# 코드 처리해주는 인터프리터는 'base':conda

def main() :
    st.title('내 앱 대시보드') # web에 띄우고 싶은 글자 st.title("글") : text : st.text("글")
    st.text('데이터 분석 앱입니다.')
    st.text('테스트 앱입니다.')
if __name__ == '__main__': # app 실행 한게 main이면 위에 있는 main 함수를 실행하라.
    main()

# Ctrl + C 누르면 서버를 끈다.(server OFF)

