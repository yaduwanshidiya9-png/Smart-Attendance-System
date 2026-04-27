import time
import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

from src.Database.db import check_teacher_exists, create_teacher, teacher_login


# ---------------- MAIN ENTRY ----------------
def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif (
        'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login"
    ):
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()


# ---------------- DASHBOARD ----------------
def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    st.header(f"Welcome, {teacher_data['name']}")


# ---------------- LOGIN LOGIC ----------------
def login_teacher(username, password):
    if not username or not password:
        return False

    teacher = teacher_login(username, password)

    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True

    return False


# ---------------- LOGIN SCREEN ----------------
def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='large')

    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="ctrl+backspace"):
            st.session_state['teacher_login_type'] = None
            st.rerun()

    st.header('Login using password', text_alignment='center')
    st.write("")
    st.write("")

    with st.form('login_form'):
        teacher_username = st.text_input("Enter username", placeholder="xyz@gmail.com")
        teacher_pass = st.text_input(
            "Enter Password", type='password', placeholder="Enter your password"
        )

        st.divider()

        btnc1, btnc2 = st.columns(2)
        with btnc1:
            login_clicked = st.form_submit_button(
                "Login", use_container_width=True
            )
        with btnc2:
            register_clicked = st.form_submit_button(
                "Register Now", type="primary", use_container_width=True, 
            )

        if login_clicked:
            if login_teacher(teacher_username, teacher_pass):
                st.toast("Welcome back!", icon="👋")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid username or password")

        if register_clicked:
            st.session_state.teacher_login_type = 'register'
            st.rerun()

    footer_dashboard()


# ---------------- REGISTER LOGIC ----------------
def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass or not teacher_pass_confirm:
        return False, "All fields are required!"
    elif check_teacher_exists(teacher_username):
        return False, "Username already taken"
    elif teacher_pass != teacher_pass_confirm:
        return False, "Passwords don't match"

    try:
        create_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Successfully created! Login now"
    except Exception as e:
        return False, f"Unexpected error: {e}"


# ---------------- REGISTER SCREEN ----------------
def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')

    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='registerbackbtn'):
            st.session_state['teacher_login_type'] = 'login'
            st.rerun()

    st.header("Register your teacher profile", text_alignment='center')
    st.write("")
    st.write("")

    with st.form('register_form'):
        teacher_username = st.text_input("Enter username", placeholder='ananyaroy')
        teacher_name = st.text_input("Enter name", placeholder='Ananya Roy')
        teacher_pass = st.text_input(
            "Enter password", type='password', placeholder="Enter password"
        )
        teacher_pass_confirm = st.text_input(
            "Confirm your password", type='password', placeholder="Re-enter password"
        )

        st.divider()

        btnc1, btnc2 = st.columns(2)
        with btnc1:
            register_clicked = st.form_submit_button(
                'Register now', use_container_width=True
            )
        with btnc2:
            login_clicked = st.form_submit_button(
                "Login instead", type='primary', use_container_width=True
            )

        if register_clicked:
            success, message = register_teacher(
                teacher_username, teacher_name, teacher_pass, teacher_pass_confirm
            )
            if success:
                st.success(message)
                time.sleep(2)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)

        if login_clicked:
            st.session_state.teacher_login_type = 'login'
            st.rerun()

    footer_dashboard()
