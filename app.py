import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el dataset
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal de la app
st.header("Análisis de Anuncios de Vehículos – Dashboard Interactivo")

# ----- Botón para histograma -----
hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Creación de un histograma para la columna 'odometer'.")

    # Crear histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)

# ----- Botón para scatter plot -----
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Gráfico de dispersión entre 'odometer' y 'price'.")

    # Crear scatter
    fig2 = px.scatter(
        car_data,
        x="odometer",
        y="price",
        opacity=0.5,
        title="Precio vs. Odómetro"
    )

    # Mostrar gráfico
    st.plotly_chart(fig2, use_container_width=True)