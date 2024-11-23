from openai import OpenAI
import streamlit as st

def chatbot(q):
    client = OpenAI(api_key=st.secrets['OPEN_API_KEY'])
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "너는 안동의 명물인지를 판별하는 봇이야. 맞다면 y 틀리면 n으로만 대답해줘"},
            {
                "role": "user",
                "content": q
            }
        ]
    )
    return(completion.choices[0].message.content)


answer=st.text_input('안동에서 유명한 것은?')
if st.button("확인"):
    ans=chatbot(answer)
    if ans=='y':
        st.success('정답!')
    else:
        st.error('오답ㅠ')