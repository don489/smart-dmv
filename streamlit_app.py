
import streamlit as st

# Set page config
st.set_page_config(page_title="DMV Personal Assistant", layout="centered")

# Language options
language = st.selectbox("Select Language / Seleccione el idioma", ["English", "Español"])

# Title and subtitle
if language == "English":
    st.title("DMV Personal Assistant")
    st.subheader("How can I help you with your motor vehicle needs today?")
    options = [
        "Get a License", "Restore a License", "Parking Tickets", "Book Written Test",
        "Book Road Test", "Change Address", "Lost or Stolen ID", "Replace License",
        "Renew License or ID", "Registration Help", "DUIs and Interlock"
    ]
    choice = st.selectbox("Please select an option below:", options)
elif language == "Español":
    st.title("Asistente Personal del DMV")
    st.subheader("¿En qué puedo ayudarte con tus necesidades vehiculares hoy?")
    options = [
        "Obtener una Licencia", "Restaurar una Licencia", "Multas de Estacionamiento", "Reservar Examen Escrito",
        "Reservar Examen Práctico", "Cambiar Dirección", "ID Perdido o Robado", "Reemplazar Licencia",
        "Renovar Licencia o ID", "Ayuda con Registro", "DUIs e Interlock"
    ]
    choice = st.selectbox("Por favor, selecciona una opción:", options)

# Response area
st.success(f"You selected: {choice}")
