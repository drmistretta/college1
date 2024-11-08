import streamlit as st

def show_navigation():
    with st.container(border=True):
        col1,col2,col3,col4=st.columns(4)
        col1.page_link("streamlit_app.py", label="Home", icon="🏠")
        col2.page_link("pages/01_college_without_region.py", label="Without Region", icon="1️⃣")
        col3.page_link("pages/02_college_with_region.py", label="With Region", icon="2️⃣")
        col4.page_link("pages/03_code_sharon.py", label="Sharon's code", icon="🏠")