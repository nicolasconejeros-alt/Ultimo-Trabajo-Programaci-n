import streamlit as st

st.title("Titulo del proyecto")
st.image("https://img.magnific.com/vector-premium/configuracion-moderna-computadoras-escritorio-productividad-creativa_1089479-30424.jpg?semt=ais_hybrid&w=740&q=80")
st.write("Hecho por Nicolás Conejeros")

df = pd.read_csv('pokemon.csv')
st.write(df)