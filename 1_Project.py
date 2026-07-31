import re

import streamlit as st

from src.state import init_state


st.set_page_config(
    page_title="Project",
    page_icon="📋",
    layout="wide",
)

init_state()

st.title("📋 Project Information")

with st.form("project_form"):
    project_number = st.text_input(
        "Project number",
        value=st.session_state["project_number"],
        placeholder="1234-567",
    )

    col1, col2, col3 = st.columns(3)

    panel_types = [
        "A", "B", "B1", "B2",
        "C", "C1", "C2", "C3", "C4", "C4.1", "C5", "C6", "C7", "C8",
        "F", "F1", "F2", "F3", "F4", "F4.1", "F5", "F6", "F7",
        "G", "G1", "G2", "G3", "G4", "G5", "G6", "G7",
        "Custom",
    ]

    main_switches = [
        "C160S4FM",
        "C125S4FM",
        "C080S4FM",
        "31115",
        "31113",
        "31111",
        "31109",
        "31107",
        "C404400S",
        "C634630S",
        "Custom",
    ]

    with col1:
        panel_type = st.selectbox(
            "Panel type",
            panel_types,
            index=panel_types.index(st.session_state["panel_type"]),
        )

    with col2:
        grounding = st.selectbox(
            "Grounding",
            ["TT", "TN-S", "TN-C-S"],
            index=["TT", "TN-S", "TN-C-S"].index(
                st.session_state["grounding"]
            ),
        )

    with col3:
        main_switch = st.selectbox(
            "Main switch",
            main_switches,
            index=main_switches.index(
                st.session_state["main_switch"]
            ),
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        swing_frame = st.checkbox(
            "Swing frame",
            value=st.session_state["swing_frame"],
        )

    with col5:
        ups = st.checkbox(
            "UPS",
            value=st.session_state["ups"],
        )

    with col6:
        rittal = st.checkbox(
            "Rittal",
            value=st.session_state["rittal"],
        )

    submitted = st.form_submit_button(
        "Save project information",
        type="primary",
    )

if submitted:
    normalized_project_number = re.sub(
        r"\s*[-–—]\s*",
        "-",
        project_number.strip(),
    )

    if not re.fullmatch(r"\d{4}-\d{3}", normalized_project_number):
        st.error("Project number must use format 1234-567.")
    else:
        st.session_state["project_number"] = normalized_project_number
        st.session_state["panel_type"] = panel_type
        st.session_state["grounding"] = grounding
        st.session_state["main_switch"] = main_switch
        st.session_state["swing_frame"] = swing_frame
        st.session_state["ups"] = ups
        st.session_state["rittal"] = rittal

        st.success("Project information saved.")

st.markdown("---")

st.subheader("Current project")

st.json(
    {
        "Project number": st.session_state["project_number"],
        "Panel type": st.session_state["panel_type"],
        "Grounding": st.session_state["grounding"],
        "Main switch": st.session_state["main_switch"],
        "Swing frame": st.session_state["swing_frame"],
        "UPS": st.session_state["ups"],
        "Rittal": st.session_state["rittal"],
    }
)