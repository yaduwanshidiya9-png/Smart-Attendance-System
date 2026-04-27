import streamlit as st

def header_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""

        <div style="display:flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:130px;' />
            <h1 style='text-align:center; color: #E0E3FF'>SNAP<br/> CLASS</h1>
        </div>
                
            """, unsafe_allow_html=True)
    

def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""

        <div style="display:flex; align-items: center; gap: 10px; ">
            <img src='{logo_url}' style='height:124px;' />
            <h2 style='text-align:left; color: #5B45F2; line-height: 3; margin: 0; padding: 0;'>SNAP<br/>CLASS</h2>
        </div>
                
            """, unsafe_allow_html=True)