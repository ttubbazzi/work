import streamlit as st
import pandas as pd
with st.echo():
    st.title('This is Title:smile::cat:')
    st.header('I am Header')
    st.subheader('This is subgeader')
    st.text('안녕하세요.')
    st.markdown('[google](https://www.google.com)')
    df=pd.DataFrame({'col1':[1,2,3,4,],
                     'col2':[11,12,13,14]})
    st.table(df)
    st.dataframe(df)
    st.image('https://www.google.com/images/')
st.video('https://www.youtube.com/watch?v=mi52kHcyu6c')
st.audio('교원연수.mp3')
#streamlit run home.py