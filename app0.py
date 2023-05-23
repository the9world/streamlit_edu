import streamlit as st
import pandas as pd

def main():
    st.title("내 앱 대시보드")
    st.text("데이터 분석 앱 입니다.")
    st.text("테스트 앱 입니다.")
    
    name="홍길동"; sound="뿡"
    st.text(f"내 이름은 {name}입니다 {sound}")
    st.header('이 영역은 Header')
    st.subheader('이 영역은 SubHeader')
    st.success(f'성공했을 때 나타내고 싶은 문장{sound}')
    st.warning(f'경고{sound}하고 싶을 때')
    st.info(f'알림을 주고 {sound}싶을 때')
    st.error(f'문제가 발생했음{sound}을 알려주고 싶을 때')
    st.help(set)
    
    df= pd.read_csv("data/iris.csv")
    st.dataframe(df)
    species= df['species'].unique()
    st.text(f'아이리스 꽃은 {species}로 되어있다.')
    st.write(df.head())
    
    if st.button('데이터 보기'):
       st.dataframe(df)
    name1="Mike"
    if st.button("대문자"):
       st.text(name1.upper())
    if st.button("소문자"):
       st.text(name1.lower())
       
    st.dataframe(df)
    status = st.radio("정렬을 선택하세요", ['오름차순', "내림차순"])
    if status =="오름차순":
       st.dataframe(df.sort_values('petal_length'))
    elif status =="내림차순":
       st.dataframe(df.sort_values('petal_length', ascending=False))
    if st.checkbox("데이터프레임 보이기"):
       st.dataframe(df.head(3))
    else:
       st.write("체크하면 데이터가 출력됩니다.")
       
    language=['선택', 'Python', 'Java', 'C', 'Go', 'PHP']
    selected_lang= st.selectbox(f'선호하는 언어를 선택:{name}', language)
    if selected_lang == '선택' :
        st.write('원하는 언어를 입력하세요')
    elif selected_lang == 'Python' :
        st.success('Python을 선택하다니 대단해')
    elif selected_lang == 'Java' :
        st.title('Java 말고 Python을 배워')
    elif selected_lang == 'C' :
        st.header('C말고 Python을 배워')
    elif selected_lang == 'Go' :
        st.subheader('Go말고 Python을 배워')
    elif selected_lang == 'PHP' :
        st.warning('PHP말고 Python을 배워')
if __name__=="__main__":
    main()