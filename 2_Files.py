import streamlit as st

from src.state import init_state


st.set_page_config(
    page_title="Files",
    page_icon="📁",
    layout="wide",
)

init_state()

st.title("📁 Project Files")

st.info("File upload functionality will be added here.")
