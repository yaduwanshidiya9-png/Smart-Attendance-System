import streamlit as st
from src.ui.base_layout import style_base_layout, style_background_home, style_background_dashboard
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image
import numpy as np


def student_screen():
    style_background_dashboard()
    style_base_layout() 

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')

    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='registerbackbtn', shortcut="control+backspace"):
            st.session_state['teacher_login_type'] = 'login'
            st.rerun()

    st.write("")
    st.write("")

    st.header("Login using faceID ", text_alignment='center')
    photo_source = st.camera_input("Position your face in the center")

    if photo_source:
        np.array(Image.open(photo_source))


    footer_dashboard()

