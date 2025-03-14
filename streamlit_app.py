import streamlit as st

st.set_page_config(
    page_title="Quỹ đội bóng Eurofins",
    page_icon="💰",
    layout="wide",
    menu_items={
        'Get help': None,
        'Report a bug': None,
        'About': None
    }
)

# Ẩn các trang khỏi sidebar
st.sidebar.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)