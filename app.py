import streamlit as st

from src_state import init_state


st.set_page_config(
    page_title="Advansor Project Preparation",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_state()

st.title("⚡ Advansor Project Preparation")

st.write(
    """
    Project preparation tool for processing BOM, CUBIC,
    Kaunas stock allocation and NAV import files.
    """
)

st.subheader("Workflow")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("1. Enter project information")

with col2:
    st.info("2. Upload project files")

with col3:
    st.info("3. Process and export results")

st.markdown("---")

st.write("Use the menu on the left to continue.")