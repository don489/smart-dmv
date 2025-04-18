import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="DMV Assistant Vera", layout="centered")

st.markdown("<h1 style='text-align: center;'>DMV Personal Assistant - Vera</h1>", unsafe_allow_html=True)

st.markdown("### Hi, I’m Vera, your DMV Assistant.")
st.markdown("I can help you get a **Real ID**, **first-time driver’s license**, **out-of-state transfer**, or **restore your license**.")

with st.expander("Select Language / Seleccione el idioma"):
    language = st.radio("Language / Idioma", ["English", "Español"])

options = [
    "Get a Real ID",
    "First-Time Driver's License",
    "Out-of-State Transfer",
    "Restore My License",
    "Check My Suspensions",
    "Parking or Court Tickets",
    "CDL or CLP Help",
    "DUI or Ignition Interlock",
    "Study for Written Test",
    "Other Questions"
]

choice = st.selectbox("How can I help you today?", options)

if st.button("Continue"):
    st.success(f"You selected: {choice}")

# Embedded AI Avatar (Vera)
html(
    """
    <div style="margin-top: 30px;">
        <iframe src="https://vercel-widget-demo.vercel.app/vera-dmv.html" width="100%" height="500" frameborder="0" allow="microphone; autoplay"></iframe>
    </div>
    """,
    height=550,
)
