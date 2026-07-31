import streamlit as st


def init_state() -> None:
    defaults = {
        "project_number": "",
        "panel_type": "A",
        "grounding": "TT",
        "main_switch": "C160S4FM",
        "swing_frame": False,
        "ups": False,
        "rittal": False,
        "uploaded_files": {},
        "bom_result": None,
        "cubic_result": None,
        "mechanics_result": None,
        "calculation_result": None,
        "export_file": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
