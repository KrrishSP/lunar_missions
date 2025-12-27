import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from plotly.graph_objs.layout.scene.camera import Center

st.set_page_config(page_title="Lunar missions", page_icon=":crescent_moon:")

#-------------------------------for google analyics...
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


#THEME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
st.markdown("""
<style>
.stApp {
    background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Aldrin_Looks_Back_at_Tranquility_Base_-_GPN-2000-001102.jpg/1280px-Aldrin_Looks_Back_at_Tranquility_Base_-_GPN-2000-001102.jpg");
    background-size: cover;
    background-attachment: fixed;
}

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.65);
    z-index: -1;
}
</style>
""", unsafe_allow_html=True)

#--------------------------------------------------------
#-------STUPID THICK WHITE LINE FIX
#st.markdown("""
#<style>
#/* Top header bar */
#[data-testid="stHeader"] {
#   background: transparent;
#    height: 0px;
#}
#</style>
#""", unsafe_allow_html=True)
#------------------------------------------------------------


#-------------------STUPID BLACK TEXT GETS HIDDEN
st.markdown("""
<style>
/* ===== MAIN CONTENT ONLY ===== */
section[data-testid="stMain"] h1,
section[data-testid="stMain"] h2,
section[data-testid="stMain"] h3 {
    color: #f2f4ff !important;
    text-shadow: 0 2px 8px rgba(0,0,0,0.7);
}

section[data-testid="stMain"] p,
section[data-testid="stMain"] span,
section[data-testid="stMain"] div,
section[data-testid="stMain"] label {
    color: #cfd3ff;
}

/* Slider label in main area only */
section[data-testid="stMain"] [data-testid="stSlider"] label {
    color: #e6e8ff;
}
</style>
""", unsafe_allow_html=True)
#---------------------------STUPID TOGGLE BUTTON OF SIDEBAR IS HIDDEN NOW!
st.markdown("""
<style>
/* Sidebar collapse button */
button[data-testid="collapsedControl"] {
    background-color: rgba(255, 255, 255, 0.15) !important;
    color: white !important;
    border-radius: 50%;
    box-shadow: 0 0 12px rgba(0,0,0,0.8);
}

/* Make the arrow brighter */
button[data-testid="collapsedControl"] svg {
    fill: white !important;
}
</style>
""", unsafe_allow_html=True)



#----------------caption too smolll
st.markdown("""
<style>
[data-testid="stImageCaption"] {
    font-size: 24px;      
    color: #	#FF0000;       
    font-style: italic;  
}
</style>
""", unsafe_allow_html=True)

#-----------------------------------------THEME ENDS


st.header('**All Lunar mission details**' )
st.subheader('Mission data from the year 1958 to the future?')
st.write('*Future lunar missions page coming soon!*')

### ---LOAD DATAFRAME HERE
excel_file = "data/lunar_missions(1).xlsx"

sheet_name = 'lunar missions'

df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols='A:B', header=0)

df_Launch_date = pd.read_excel(excel_file, sheet_name=sheet_name, usecols='B:C', header=0)

df_Launch_date.dropna(inplace=True)


#--- SLIDER SELECTION
df = pd.read_excel(
    excel_file,
    sheet_name=sheet_name,
    usecols='A:I',
    header=0
)

df['Launch Date'] = pd.to_datetime(df['Launch Date'], dayfirst=True)

years = df['Launch Date'].dt.year.dropna().astype(int)

year_selection = st.slider(
    'Mission year range:',
    min_value=int(years.min()),
    max_value=int(years.max()),
    value=(int(years.min()), int(years.max()))
)

df_filtered = df[
    (df['Launch Date'].dt.year >= year_selection[0]) &
    (df['Launch Date'].dt.year <= year_selection[1])
]

#--------------------To remove Time 00:00:00 ---------------HH:MM:SS FORMAT-----------PANDAS
df_filtered['Launch Date'] = df_filtered['Launch Date'].dt.date

st.dataframe(df_filtered)




#----------Country/Operator
df_country = df['Country / Operator'].value_counts().reset_index()
df_country.columns = ['Country / Operator', 'Missions']

country_bar = px.bar(
    df_country,
    x='Country / Operator',
    y='Missions',
    title='Missions by Country / Operator'
)

st.plotly_chart(country_bar)

#-----------Mission Type
df_mission_type = df['Mission Type'].value_counts().reset_index()
df_mission_type.columns = ['Mission Type', 'Missions']

mission_type_bar = px.bar(
    df_mission_type,
    x='Mission Type',
    y='Missions',
    title='Missions by Type'
)

st.plotly_chart(mission_type_bar)


#------------Outcome
df_outcome = df['Outcome'].value_counts().reset_index()
df_outcome.columns = ['Outcome', 'Missions']

outcome_bar = px.bar(
    df_outcome,
    x='Outcome',
    y='Missions',
    title='Mission Outcomes'
)

st.plotly_chart(outcome_bar)

#----------FILTER DATAFRAME
##CHATGPT-------------------------------------------------------------

st.sidebar.header("Filters")
st.sidebar.subheader("*Note: select one or more of the available options in the given filters*")

# Country / Operator filter
country_selection = st.sidebar.multiselect(
    "Select Country / Operator",
    options=df['Country / Operator'].unique(),
    default=df['Country / Operator'].unique()
)

# Mission Type filter
mission_type_selection = st.sidebar.multiselect(
    "Select Mission Type",
    options=df['Mission Type'].unique(),
    default=df['Mission Type'].unique()
)

# Outcome filter
outcome_selection = st.sidebar.multiselect(
    "Select Outcome",
    options=df['Outcome'].unique(),
    default=df['Outcome'].unique()
)

# Optional: Launch Year filter
if 'Launch Date' in df.columns:
    df['Launch Year'] = pd.to_datetime(df['Launch Date'], errors='coerce').dt.year
    year_selection = st.sidebar.slider(
        "Select Launch Year Range",
        int(df['Launch Year'].min()),
        int(df['Launch Year'].max()),
        (int(df['Launch Year'].min()), int(df['Launch Year'].max()))
    )
    year_mask = df['Launch Year'].between(*year_selection)
else:
    year_mask = True

# Combine filters
mask = (
    df['Country / Operator'].isin(country_selection) &
    df['Mission Type'].isin(mission_type_selection) &
    df['Outcome'].isin(outcome_selection) &
    year_mask
)

filtered_df = df[mask]

st.markdown(f"**Available Results: {filtered_df.shape[0]}**")

# Show filtered table
st.dataframe(filtered_df)



###-------------
#st.dataframe(df_Launch_date)

#pie_chart = px.pie(df_Launch_date, title='Launch dates', values='Launch Date', names='Mission Name')

#st.plotly_chart(pie_chart)
###-------------


df_Launch_date['Year'] = pd.to_datetime(df_Launch_date['Launch Date'], dayfirst=True).dt.year
year_counts = df_Launch_date['Year'].value_counts().reset_index()
year_counts.columns = ['Year', 'Missions']

pie_chart = px.pie(
    year_counts,
    names='Year',
    values='Missions',
    title='Missions per Year'
)

st.plotly_chart(pie_chart, width="content")

image = Image.open("assets/lunar_missions.png")

st.image(image, width='content', caption='Moon soft landings')

#-------------Interactive moon sphere test1
import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("🌕 Interactive Moon Soft Landing Sites")
st.markdown(
    "**Rotate, zoom, and hover to explore coords of different missions.**"
)

# ---------------------------------
# Moon Sphere
# ---------------------------------
R = 1

phi = np.linspace(0, np.pi, 120)
theta = np.linspace(0, 2 * np.pi, 240)
phi, theta = np.meshgrid(phi, theta)

x = R * np.sin(phi) * np.cos(theta)
y = R * np.sin(phi) * np.sin(theta)
z = R * np.cos(phi)

moon = go.Surface(
    x=x, y=y, z=z,
    colorscale="Gray",
    showscale=False,
    opacity=0.75
)

# Mission data with country

missions = [
    # name, lat, lon, country
    ("Luna 9", 7.08, -64.37, "USSR"),
    ("Surveyor 1", -2.47, -43.34, "USA"),
    ("Luna 13", 18.87, -62.05, "USSR"),
    ("Surveyor 3", -3.02, -23.42, "USA"),
    ("Surveyor 5", 1.46, 23.19, "USA"),
    ("Surveyor 6", 0.47, -1.43, "USA"),
    ("Surveyor 7", -40.98, -11.51, "USA"),
    ("Apollo 11", 0.67, 23.47, "USA"),
    ("Apollo 12", -2.94, -23.42, "USA"),
    ("Luna 16", -0.51, 56.36, "USSR"),
    ("Luna 17", 38.24, -35.00, "USSR"),
    ("Apollo 14", -3.64, -17.48, "USA"),
    ("Apollo 15", 26.13, 3.63, "USA"),
    ("Luna 20", 3.79, 56.62, "USSR"),
    ("Apollo 16", -8.97, 15.50, "USA"),
    ("Apollo 17", 20.19, 30.77, "USA"),
    ("Luna 21", 26.00, 30.41, "USSR"),
    ("Luna 24", 12.71, 62.21, "USSR"),

    ("Chang'e 3", 44.12, -19.51, "China"),
    ("Chang'e 4", -45.45, 177.60, "China"),
    ("Chang'e 5", 43.10, -51.80, "China"),
    ("Chang'e 6 (target)", -85.0, 0.0, "China"),

    ("Chandrayaan-3", -69.37, 32.32, "India"),
    ("SLIM", 1.04, 9.06, "Japan"),
    ("Blue Ghost M1", 18.56, 61.81, "USA (Commercial)"),
    ("IM-2 Athena", -72.0, 35.0, "USA (Commercial)")
]

country_colors = {
    ""  : "",
    ""  : "",
    ""  : "",
    "USA": "dodgerblue",
    "USA (Commercial)": "deepskyblue",
    "USSR": "red",
    "China": "gold",
    "India": "limegreen",
    "Japan": "orange"
}

# ---------------------------------
# Create traces per country (LEGEND)
# ---------------------------------
traces = []

for country, color in country_colors.items():
    xs, ys, zs, labels = [], [], [], []

    for name, lat, lon, c in missions:
        if c != country:
            continue

        lat_r = np.radians(lat)
        lon_r = np.radians(lon)

        xs.append(R * np.cos(lat_r) * np.cos(lon_r))
        ys.append(R * np.cos(lat_r) * np.sin(lon_r))
        zs.append(R * np.sin(lat_r))

        labels.append(f"{name}<br>{country}<br>Lat: {lat}°<br>Lon: {lon}°")

    if xs:
        traces.append(
            go.Scatter3d(
                x=xs, y=ys, z=zs,
                mode="markers",
                name=country,              # <-- Legend entry
                marker=dict(
                    size=6,
                    color=color,
                    line=dict(width=0.5, color="black")
                ),
                hoverinfo="text",
                text=labels
            )
        )


# ---------------------------------
# Plot

fig = go.Figure(data=[moon] + traces)  # Use your actual data: moon + traces

# Move legend
fig.update_layout(
    legend=dict(
        x=0.9,      # horizontal position (0=left, 1=right)
        y=0.5,      # vertical position (0=bottom, 1=top)
        xanchor='center',
        yanchor='middle',
    ),
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode="data"
    ),
    margin=dict(l=0, r=0, t=0, b=0),
)

st.plotly_chart(fig, width="content")

#--------------------------------------------------------------3d moon render trial1








