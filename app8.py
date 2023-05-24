# app7 파일을 3개로 분리하기

import streamlit as st

from app_image import run_app_image # import app_image 해도 됨
from app_csv import run_app_csv
from app_about import run_app_about

def main() :
    st.title('웹 대시보드') # web에 띄우고 싶은 글자 st.title("글") : text : st.text("글")

    menu= ['이미지업로드', 'csv업로드', 'About']
    choice= st.sidebar.selectbox('메뉴', menu)
    print(choice)
    if choice == menu[0]: # 이렇게 해야 변수 내에 요소 바꿔도 편리함
        run_app_image()
                        
    elif choice== menu[1]:
        run_app_csv()
        
    else:
        run_app_about()
        
        
    
if __name__ == '__main__': # app 실행 한게 main이면 위에 있는 main 함수를 실행하라.
    main()