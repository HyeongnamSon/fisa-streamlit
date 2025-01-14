import streamlit as st

# text를 입력하는 검색창을 하나 만듭니다.
# ani_list에 있는 글자가 일부라도 들어가면
# img_list에 있는 해당 그림이 출력되는 검색창을 하나 만들어주세요
ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']


search_term = st.text_input("검색하실 애니메이션을 입력하세요:")

if search_term:
    matched_ani = [ani for ani in ani_list if search_term in ani]

    if matched_ani:
        # 매칭되는 애니메이션 이름에 해당하는 이미지 출력
        for ani in matched_ani:
            index = ani_list.index(ani)
            st.image(img_list[index])