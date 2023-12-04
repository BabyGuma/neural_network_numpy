import pandas as pd
import numpy as np
import streamlit as st

# Coordenadas del centro de Canadá (56.1304, -106.3468)
canada_data = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [56.1304, -106.3468],
    columns=['lat', 'lon'],
    index=range(500))

# Coordenadas del centro de India (20.5937, 78.9629)
india_data = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [20.5937, 78.9629],
    columns=['lat', 'lon'],
    index=range(500, 1000))

# Combina los datos de Canadá e India en un solo DataFrame
map_data = pd.concat([canada_data, india_data])

# Crea el título para la aplicación web
st.title("Canada and India Map")
st.header("Using Streamlit and Mapbox")

# Muestra ambos países en el mapa
st.map(map_data)

def circulo(num_datos=100, R=1, minimo=0, maximo=1):
    pi = np.pi
    r = R * np.sqrt(np.random.truncnorm(minimo, maximo, size=num_datos)) * 10
    theta = np.random.truncnorm(minimo, maximo, size=num_datos) * 2 * pi + 10

    x = np.cos(theta) * r
    y = np.sin(theta) * r

    y = y.reshape((num_datos, 1))
    x = x.reshape((num_datos, 1))

    x = np.round(x, 3)
    y = np.round(y, 3)

    df = np.column_stack((x, y))
    return df
