import streamlit as st
from datetime import datetime
from app_utils import save_uploaded_file

def run_app_image() :
    st.success('이미지 파일 업로드')
    img_file= st.file_uploader('이미지를 업로드 하세요', type=['png', 'jpg', 'jpeg'])
    # st.file_uploader() 파일 업로드 // type=[]확장자 제한    

    if img_file is not None : 
        print( type(img_file)) # <class 'streamlit.runtime.uploaded_file_manager.UploadeFile'>
        print(img_file.name) # 파일 이름 출력
        print(img_file.size) # 파일 용량 출력
        print(img_file.type) # 파일 확장자 출력

    # 유저가 올린 파일을 서버에서 유니크하게 처리하기 위해
    # 파일명을 현재시간 조합으로 해서 만든다.
        current_time= datetime.now()
        print(current_time) # isoformat() 정의 모름
        print(current_time.isoformat().replace(':', '_')+ '.jpg')
        filename= current_time.isoformat().replace(':', '_')+ '.jpg'

        img_file.name= filename
        save_uploaded_file('image', img_file)

    # 밑에 이미지 나오게 해주세요.
        st.image('image/'+filename)