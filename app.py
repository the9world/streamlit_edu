import streamlit as st # error 밑줄이 있어야 정상
# 코드 처리해주는 인터프리터는 'base':conda

def main() :
    st.title('내 앱 대시보드') # web에 띄우고 싶은 글자 st.title("글") : text : st.text("글")
    st.text('데이터 분석 앱입니다.')
    st.text('테스트 앱입니다.')
if __name__ == '__main__': # app 실행 한게 main이면 위에 있는 main 함수를 실행하라.
    main()
# $ streamlit run app.py
# Ctrl + C 누르면 서버를 끈다.(server OFF)

