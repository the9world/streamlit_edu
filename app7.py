import streamlit as st
import pandas as pd
import os # 파일, 디렉토리 등 작업하는 라이브러리
from datetime import datetime # 시간 관련 라이브러리

# 디렉토리 이름과 파일을 주면
# 해당 디렉토리에 파일을 저장해주는 함수
def save_uploaded_file(directory, file) :
    # 1. 저장할 디렉토리가 있는지 확인하고,
    #    없으면 디렉토리를 먼저 만든다.
    if not os.path.exists(directory) : 
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일 저장
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    return st.success('파일 저장 완료')

        
def main() :
    st.title('웹 대시보드') # web에 띄우고 싶은 글자 st.title("글") : text : st.text("글")

    menu= ['이미지업로드', 'csv업로드', 'About']
    choice= st.sidebar.selectbox('메뉴', menu)
    print(choice)
    if choice == menu[0]: # 이렇게 해야 변수 내에 요소 바꿔도 편리함
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
                        
    elif choice== menu[1]:
        st.warning('csv 파일 업로드')
        csv_file = st.file_uploader('CSV 파일 업로드', type=['csv'] )
        if csv_file is not None:
            current_time = datetime.now()
            filename = current_time.isoformat().replace(':', '_')
            
            csv_file.name = filename
            
            save_uploaded_file('csv', csv_file)
            df = pd.read_csv('csv/'+filename, index_col=0)
            st.dataframe(df)
    else:
        st.error('About')
        
        
    
if __name__ == '__main__': # app 실행 한게 main이면 위에 있는 main 함수를 실행하라.
    main()