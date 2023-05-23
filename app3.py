import streamlit as st # 코드 처리해주는 인터프리터는 'base':conda
import pandas as pd

def main() :
    st.title('내 앱 대시보드') # web에 띄우고 싶은 글자 st.title("글") : text : st.text("글")

    df = pd.read_csv("data/iris.csv")
    # print(df) # df가 터미널에 나타남 X
    st.dataframe(df) # web에 dataframe을 출력 st.dataframe(변수)   

    species = df['species'].unique() # species에 df['species]에 값을 중복을 제외하고 세어줌
    st.text('아이리스 꽃은 ' + species + '으로 되어있다.') # 문자열 + 변수 + 문자열
    
    st.write(df.head())
    
if __name__ == '__main__': # app 실행 한게 main이면 위에 있는 main 함수를 실행하라.
    main()
# $ streamlit run app.py
# Ctrl + C 누르면 서버를 끈다.(server OFF)