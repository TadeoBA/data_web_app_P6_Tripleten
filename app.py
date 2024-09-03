import pandas as pd
import streamlit as st
import plotly.express as px

# Leer los datos desde el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')  # Asegúrate de que la ruta sea correcta

# Crear el encabezado de la aplicación
st.header('Análisis Exploratorio de Datos de Anuncios de Venta de Coches by Tadeo Bayona Araque')

# Botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión entre odómetro y precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
