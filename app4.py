from numpy import column_stack
import streamlit as st # 코드 처리해주는 인터프리터는 'base':conda
import pandas as pd

def main() :
    st.title('내 앱 대시보드') # web에 띄우고 싶은 글자 st.title("글") : text : st.text("글")

    df = pd.read_csv('data/iris.csv')
    
    # web에 버튼 만들기
    if st.button('데이터 보기') : # 버튼을 누르면 True가 된다.
        st.dataframe(df) # 버튼을 누르면 dataframe(df)가 실행 됨
    
        
    name = "Mike"
    # 대문자 버튼을 누르면, 대문자로 표시하고
    # 소문자 버튼을 누르면, 소문자로 나오게 하자
    if st.button('대문자'):
        st.text(name.upper())
    if st.button('소문자'):
        st.text(name.lower())
    
        
    st.dataframe(df)
    # petal_length 컬럼을 정렬하고 싶다.
    # 오름차순 정렬, 내림차순 정렬 두 가지 옵션 선택하도록
    status = st.radio('정렬을 선택하세요.', ['오름차순', '내림차순']) # radio 선택창
    print(status) # web에서 선택한 것을 터미널에 출력
     
    if status == '오름차순':
        st.dataframe(df.sort_values('petal_length'))
    elif status == '내림차순':
        st.dataframe(df.sort_values('petal_length', ascending=False))
    
        
    if st.checkbox('데이터프레임 보이기') : # st.checkbox('글')체크박스를 표현
        st.dataframe(df.head(3))
    else :
        st.write('체크하면 데이터가 출력됩니다.')
    

    # 여러개 중에 1개를 선택
    language = ['선택','Python', 'Java', 'C', 'Go', 'PHP']
    selected_lang = st.selectbox('선호하는 언어를 선택!', language)
    if selected_lang == '선택' :
        st.text('원하는 언어를 선택하세요')
    elif selected_lang == 'Python' :
        st.text('Python을 선택하다니 대단해')
    elif selected_lang == 'Java' :
        st.text('Java 말고 Python을 배워')
    elif selected_lang == 'C' :
        st.text('C말고 Python을 배워')
    elif selected_lang == 'Go' :
        st.text('Go말고 Python을 배워')
    elif selected_lang == 'PHP' :
        st.text('PHP말고 Python을 배워')

    # 데이터 프레임의 컬럼이름을 보여주고,
    # 유저가 컬럼을 선택하면
    # 해당 컬럼만 가져와서 데이터프레임을 보여주고 싶다.
    column_list= st.multiselect('컬럼을 선택하세요', df.columns)
    print(column_list)
    
        # 선택한 컬럼으로 데이터프레임을 보여주고 싶다.
    st.dataframe(df[column_list])
     # slider(좌우드래그볼) (최소치, 맥스치, 스탭, 최초값)
    age= st.slider("나이", min_value=10, max_value=150, step=2, value=50)
    st.text(f'나이는 {age} 입니다.') # or ('나이는'+ str(age)+ '입니다.') 문자+숫자 유의
    
    with st.expander('hello'): # with 알아보기// hello 누르면 밑에 실행?
        st.text('안녕하세요')
                    
if __name__ == '__main__': # app 실행 한게 main이면 위에 있는 main 함수를 실행하라.
    main()
# $ streamlit run app.py
# Ctrl + C 누르면 서버를 끈다.(server OFF)