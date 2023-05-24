import streamlit as st

def main() :
    st.title('웹 대시보드') # web에 띄우고 싶은 글자 st.title("글") : text : st.text("글")

    name= st.text_input('이름을 입력하세요!', max_chars=20)
    st.text('입력하신 이름은 '+ name) # (f'입력하신 이름은{}')
    
    message = st.text_area('메시지를 입력하세요', height=100) # 모름 알아봅시다
    st.text(message)
    
    # 숫자 입력
    number= st.number_input('숫자를 입력하세요.', 1, 100, 90, 5) # 민, 맥스, 최초값, 스텝, int 변환
    st.text(number * 3)
    
    number2= st.number_input('숫자를 입력하세요.', 1.0, 10.0) # 민, 맥스, 외에 파라미터 넣으면 error 이유 찾기
    st.text(number2 * 3)
    
    # 날짜
    my_date= st.date_input('약속 날짜 입력') # 달력 보여줌,
    print(my_date)
    print(type(my_date))
    st.text(my_date) # 선택한 날짜 text 출력
    
    # 시간
    my_time= st.time_input('시간 선택', ) # 시간 선택창
    print( type(my_time ) )
    st.text(my_time) # 선택한 시간 출력
    
    # 비밀번호 처리방법
    password= st.text_input('비밀번호 입력', type='password') # 비밀번호 입력
    st.text(password) # 비밀번호 보여줌
    
    # 색 입력
    color = st.color_picker('색을 선택하세요')   # 색상(색넘버) 선택
    st.text(color) # 색 넘버 보여줌
    
    
    
    
if __name__ == '__main__': # app 실행 한게 main이면 위에 있는 main 함수를 실행하라.
    main()