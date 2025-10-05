import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")

st.header('Analisis de Anuncios de Coches')

hist_button = st.button('Construir histograma') 
     
if hist_button: # al hacer clic en el botón
         
    st.write('Creación de un histograma')
         
    fig = px.histogram(car_data, x="odometer")
     
    st.plotly_chart(fig, use_container_width=True)

dispersion_button = st.button('Construir gráfico de dispersión')

if dispersion_button:
        
    st.write('Creación de un gráfico de dispersión')
        
    fig_dispersion = px.scatter(car_data,x="odometer",y="price")
        
    st.plotly_chart(fig_dispersion, use_container_width=True)
