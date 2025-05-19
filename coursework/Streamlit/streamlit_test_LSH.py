import streamlit as st

st.set_page_config(layout = 'wide') # 넓은 화면면

st.title('This is my first webpage')
st.header('What is this?')
st.subheader('This is the new home')

# layout 짜기
col1, col2 = st.columns([2,3])

with col1:
    # column 1 에 담을 내용
    st.title('Here comes the Sung')
    st.markdown('---')
with col2:
    st.title('Who come?')
    st.checkbox('press one')
        
col1.subheader('I am who I am')
col1.subheader('Remember who you are')
col2.checkbox('press two')

# tab
# tab은 이미 데이터가 주어져서 다른 내용 출력 불가가
tab1, tab2, tab3 = st.tabs(['Tab A','Tab B','Tab D'])

with tab1:
    st.write('Do not give up')
    
with tab2:
    st.write('Rejoice')
    
with tab3:
    st.write('Do not look back')

# Sidebar
st.sidebar.title('Select your Lunch')
st.sidebar.checkbox('Korean')
st.sidebar.checkbox('Chinese')
st.sidebar.checkbox('Japanese')
st.sidebar.checkbox('Vietnam')

st.sidebar.selectbox('선호하는 식당',['','필동순대국','온수반','명궁','119','버거킹'])
st.sidebar.selectbox('점심 메뉴 선택',['','순대국','힘줄온반','모둠돈까스','아무거나','와퍼','짜장면','볶음밥밥'])

# 이미지 불러오기
from PIL import Image
lunch_img = Image.open('lunch.jpg')

col3, col4 = st.columns(2)
col3.image(lunch_img)

