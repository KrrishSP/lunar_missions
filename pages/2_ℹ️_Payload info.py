import streamlit as st

st.title("Payload data archive on lunar missions")

st.markdown("""
**Early missions (1958–1963) had:**

- Very limited payloads  
- Often telemetry + radiation counters only  
- Many missions failed before lunar encounter  

**So for those missions:**
- Payload Type = Technology Demonstration / Particle Detector / Other  
- Description explicitly says *“limited scientific payload”*
""")

#----------------
# ➡️ For `use_container_width=True`, use `width='stretch'`. For `use_container_width=False`, use `width='content'`
#-------------------
import pandas as pd

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Lunar Mission Payload Explorer",
    layout="wide"
)

#---------for google analytics,,,,
import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-HRBHNW2DZJ"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-HRBHNW2DZJ');
    </script>
    """,
    height=0,
)

#--------------------------------------------
st.title("Lunar Mission Payload Explorer")
st.write("")

# -------------------- LOAD EXCEL --------------------
EXCEL_PATH = r"data/lunar_mission_payloads.xlsx"

@st.cache_data
def load_data(path):
    return pd.read_excel(path, sheet_name="Sheet1")

df = load_data(EXCEL_PATH)

# -------------------- FILTERS (MAIN PAGE) --------------------
st.subheader("🔎 Filters")

col1, col2 = st.columns(2)

# ✅ Country filter (NEW)
with col1:
    country_options = sorted(df["Country"].dropna().unique())
    selected_countries = st.multiselect(
        "Select Country(s)",
        options=country_options,
        default=country_options
    )

# Payload type filter (UNCHANGED)
with col2:
    payload_type_options = [
        "Camera",
        "HSI (Hyperspectral Imaging)",
        "Spectrometer",
        "Radar",
        "Magnetometer",
        "Laser Altimeter (LIDAR)",
        "Radiometer",
        "Plasma / Particle Detector",
        "Seismometer",
        "Technology Demonstration",
        "Navigation / Tracking",
        "Communication Relay",
        "Biological Experiment",
        "Other"
    ]

    selected_payload_types = st.multiselect(
        "Select Payload Type(s)",
        options=payload_type_options,
        default=payload_type_options
    )

# -------------------- APPLY FILTERS --------------------
filtered_df = df[
    (df["Country"].isin(selected_countries)) &
    (df["Payload Type"].isin(selected_payload_types))
]

# -------------------- MAIN TABLE --------------------
st.subheader("📊 Payload Data")
st.write(f"Showing **{len(filtered_df)}** payload records")

st.dataframe(
    filtered_df,
    width="stretch",
    hide_index=True
)

# -------------------- FOOTER --------------------
st.markdown("---")
st.caption("Lunar payload dataset")









