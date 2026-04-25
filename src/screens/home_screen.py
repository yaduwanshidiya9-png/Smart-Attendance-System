import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout, style_background_home
from src.components.footer import footer_home

def home_screen():


    header_home()
    style_base_layout()
    style_background_home()



    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("## I'm <br> Student", unsafe_allow_html=True)
        st.image("https://static.vecteezy.com/system/resources/thumbnails/059/925/181/small_2x/dramatic-rustic-graduate-student-in-cap-and-gown-premium-free-png.png", width=135)
        if st.button("Sudent portal", type="primary", icon=':material/chevron_right:', icon_position='right'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.markdown("## I'm <br> Teacher", unsafe_allow_html=True)
        st.image("https://static.vecteezy.com/system/resources/thumbnails/059/608/779/small_2x/vibrant-artistic-teacher-explaining-lesson-enthusiastic-gesture-4k-free-png.png", width=130)
        if st.button("Teacher Portal", type="primary", icon=':material/chevron_right:', icon_position='right'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    footer_home()
