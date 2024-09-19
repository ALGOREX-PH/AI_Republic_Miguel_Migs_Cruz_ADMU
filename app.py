import streamlit as st
import pandas as pd

st.set_page_config(page_title="Miguel Cruz's News Articles", layout="centered")

dataframed = pd.read_csv("https://raw.githubusercontent.com/ALGOREX-PH/AI_Republic_Anna_Anya_Garcia_UST/main/Dataset/Articles_AI.csv")

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'
if 'story_index' not in st.session_state:
    st.session_state.story_index = 0

if st.session_state.current_page == "Home":
    st.subheader("Miguel Cruz's News Articles")
    st.markdown("---")
    for x in range(0, 10):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(dataframed["Title"][x])
        with col2:
            if st.button("Read Story", key = "Read Story : " + str(x + 1)):
                st.session_state.current_page = "Story"
                st.session_state.story_index = x
                st.rerun()

elif st.session_state.current_page == "Story":
    if st.button("Go Back"):
        st.session_state.current_page = "Home"
        st.rerun()
    st.title(dataframed["Title"][st.session_state.story_index])
    st.write(dataframed["ADMU"][st.session_state.story_index])
    st.markdown("---")
    st.write("Reference : " + dataframed["Link"][st.session_state.story_index])

