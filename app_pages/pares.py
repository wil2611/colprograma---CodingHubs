import streamlit as st
import pandas as pd
import plotly.express as px
from actions.chart_actions import graficador
from constants.footer_constants import FOOTER_HTML, IMAGENES_BASE64
from constants.header_constants import LOGO_NAVBAR_BASE64, HIDE_STREAMLIT_STYLE, NAVBAR_TEMPLATE, generar_css_personalizado
from utils.chart_config import get_chart_config
chart_config = get_chart_config()

# Configuración de la página
st.set_page_config(layout="wide")

# Ocultar elementos de Streamlit
st.markdown(HIDE_STREAMLIT_STYLE, unsafe_allow_html=True)

# Generar el CSS personalizado con el color deseado
color_fondo_navbar = "#1DB2E8"  # Cambia este valor según lo necesites
custom_css = generar_css_personalizado(color_fondo_navbar)

# Aplicar el CSS en Streamlit
st.markdown(custom_css, unsafe_allow_html=True)

# Navbar personalizado con logo
navbar = NAVBAR_TEMPLATE.format(LOGO_NAVBAR_BASE64=LOGO_NAVBAR_BASE64)
st.markdown(navbar, unsafe_allow_html=True)

# URL del CSV
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQQh-hLxRDowudvBj8gYjlieqdlVilmobcI5UtFOMMvgkqs3JYrjWv2eObbRcOViA/pub?output=csv"

# --- Cargar Datos con Cache ---
@st.cache_data(ttl=600)
def load_data(file):
    df = pd.read_csv(file)
    df.columns = df.columns.str.strip()
    return df

df = load_data(CSV_URL)


st.title("Graficador de datos de pares expertos")

graficador(df)
# def convertir_csv(dataframe):
#     return dataframe.to_csv(index=False).encode('utf-8')

# st.download_button("Descargar datos filtrados", convertir_csv(df_filtrado), "datos_filtrados.csv", "text/csv")
# st.download_button("Descargar datos completos", convertir_csv(df), "datos_completos.csv", "text/csv")

# Pie de página
st.markdown("---")
st.write("© 2025 Colombia Programa - Ministerio de Tecnologías de la Información y las Comunicaciones (MinTIC)")

# Formatear el HTML con las imágenes convertidas a base64
formatted_footer = FOOTER_HTML.format(imagenes_base64=IMAGENES_BASE64)

# Mostrar el footer en Streamlit
st.markdown(formatted_footer, unsafe_allow_html=True)