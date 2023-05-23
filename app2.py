import streamlit as st

def main() :
    st.title('웹 대시보드') # web에 띄우고 싶은 글자 st.title("글") : text : st.text("글")

    name = "홍길동"
    print('제 이름은 {}입니다.'.format(name)) # print()를 사용하면 터미널에만 출력 됨
    st.text('제 이름은 {}입니다.'.format(name)) # formatting
    st.header('이 영역은 헤더 영역') # title보다 조금 작은 text 크기
    st.subheader('이 영역은 서브헤더 영역') # header보다 조금 작음
    st.success('성공했을 때 나타내고 싶은 문장')
    st.warning('경고하고 싶을 때')
    st.info('알림을 주고 싶을 때')
    st.error('문제가 발생했음을 알려주고 싶을 때')
    st.help(range) # 도움말 help(range) : range 함수 설명
    
if __name__ == '__main__': # app 실행 한게 main이면 위에 있는 main 함수를 실행하라.
    main()