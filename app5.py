import streamlit as st
from PIL import Image # 이미지 처리 라이브러리 (PIL: Python Image Library)
def main() :
    st.title('웹 대시보드') # web에 띄우고 싶은 글자 st.title("글") : text : st.text("글")
    
    # 사진과 영상을 보여주는 방법
    img= Image.open('data/image_03.jpg') # i=I 대문자 # 안됨
    print(img)
    st.image(img)
    st.image(img, use_column_width= True)
    
    # 이미지를 URL로 불러와서 보여주기
    st.image('https://cdn.pixabay.com/photo/2019/10/13/13/19/landscape-4546121_960_720.jpg')
    
    video_file= open('data/video1.mp4', 'rb' ) # rb read bydery 리드바이더리
    st.video(video_file) # 비디오 열기
    
if __name__ == '__main__': # app 실행 한게 main이면 위에 있는 main 함수를 실행하라.
    main()