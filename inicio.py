import streamlit as st
import pandas as pd

st.title("Titulo del proyecto")
st.image("https://img.magnific.com/vector-premium/configuracion-moderna-computadoras-escritorio-productividad-creativa_1089479-30424.jpg?semt=ais_hybrid&w=740&q=80")
st.write("Hecho por Nicolás Conejeros")

df = pd.read_csv('https://raw.githubusercontent.com/nicolasconejeros-alt/Trabajo-Final-Programacion/refs/heads/main/pokemon.csv')
st.write(df)