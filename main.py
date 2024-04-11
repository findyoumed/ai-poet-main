# 환경 변수
# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st

# OpenAI의 completeion 모드
# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("내가 좋아하는 동물은")
# print(result)

# ChatOpenAI의 chat 모드
from langchain.chat_models import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI
chat_model = ChatOpenAI()


st.title('인공지능 시인')
# content = "봄날"
content = st.text_input('시의 주제를 제시해주세요.')

# st.button("Reset", type="primary")
# if st.button('Say hello'):
#     st.write('Why hello there')
# else:
#     st.write('Goodbye')
if st.button('시 작성 요청하기'):
    with st.spinner('시 작성중...'):
    # time.sleep(5)
    # st.success('Done!')
        result = chat_model.predict(content + "에 대한 시를 써줘")
        # print(result)
        st.write(result)


# result = chat_model.predict("Hi!")
# result = chat_model.predict(content + "에 대한 시를 써줘")
# print(result)

# title = st.text_input('시의 주제를 제시해주세요.')
# st.write('시의 주제 :', title)
# st.title('_Streamlit_ is :blue[cool] :sunglasses:')