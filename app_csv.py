import streamlit as st
import pandas as pd
from datetime import datetime
from app_utils import save_uploaded_file

def run_app_csv() :
    st.warning('csv 파일 업로드')
    csv_file = st.file_uploader('CSV 파일 업로드', type=['csv'] )
    if csv_file is not None:
        current_time = datetime.now()
        filename = current_time.isoformat().replace(':', '_')
        
        csv_file.name = filename
        
        save_uploaded_file('csv', csv_file)
        df = pd.read_csv('csv/'+filename, index_col=0)
        st.dataframe(df)