import streamlit as st

from src_state import init_state

st.set_page_config(
    page_title="Project Files",
    page_icon="📁",
    layout="wide",
)

init_state()

st.title("📁 Project Files")

files = {
    "data": ("DATA.xlsx", ["xlsx", "xlsm"]),
    "bom": ("Project BOM", ["xlsx", "xlsm"]),
    "cubic": ("CUBIC BOM", ["xlsx", "xlsm"]),
    "stock": ("Kaunas Stock", ["xlsx", "xlsm"]),
}

if "uploaded_files" not in st.session_state:
    st.session_state["uploaded_files"] = {}

for key, (title, ext) in files.items():

    uploaded = st.file_uploader(
        title,
        type=ext,
        key=f"upload_{key}",
    )

    if uploaded:
        st.session_state["uploaded_files"][key] = uploaded

    if key in st.session_state["uploaded_files"]:
        st.success(f"✅ {title} loaded")
    else:
        st.warning(f"⚪ {title} not loaded")

st.divider()

loaded = len(st.session_state["uploaded_files"])

st.progress(loaded / len(files))

st.write(f"Loaded {loaded} of {len(files)} required files")

if loaded == len(files):
    st.success("All required files are loaded.")
else:
    st.info("Upload all files to continue.")