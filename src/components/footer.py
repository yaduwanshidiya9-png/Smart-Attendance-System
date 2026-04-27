import streamlit as st

def footer_home():

    st.markdown(f"""
         
        <div style="margin-top: 2rem; text-align: center;">
            <p style="color: white; font-weight: bold; display: flex; justify-content: center; align-items: center; gap: 8px;">
                Created with ❤️ by Diya yadu1c
            </p>
        </div>

            """, unsafe_allow_html=True)
    
def footer_dashboard():
    logo_url = "https://i.imgflip.com/5yejcn.jpg"

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
            <<p style="color: black; font-weight: bold; display: flex; justify-content: center; align-items: center; gap: 8px;">
                Created with ❤️ by Diya yadu1c
            </p>
        
        </div>
    """, unsafe_allow_html=True)