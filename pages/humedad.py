import streamlit as st
import pandas as pd
from PIL import Image

st.title ('Analisis de Humedad')
image = Image.open('humedad.png')
st.image(image)

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
   df1=pd.read_csv(uploaded_file)

   st.subheader('Perfil gráfico de la variable medida.')
   df1 = df1.set_index('Time')
   st.line_chart(df1)
   
   st.write(df1)
   st.subheader('Estadísticos básicos de los sensores.')
   st.dataframe(df1["Humedad ESP32"].describe())
   
   min_hum = st.slider('Selecciona valor mínimo del filtro ', min_value=0, max_value=100, value=23, key=1)
   # Filtrar el DataFrame utilizando query
   filtrado_df_min = df1.query(f"`Humedad ESP32` > {min_hum}")
   # Mostrar el DataFrame filtrado
   st.subheader("Porcentajes de humedad superiores al valor configurado.")
   st.write('Dataframe Filtrado')
   st.write(filtrado_df_min)
   
   max_hum = st.slider('Selecciona valor máximo del filtro ', min_value=0, max_value=100, value=23, key=2)
   # Filtrar el DataFrame utilizando query
   filtrado_df_max = df1.query(f"`Humedad ESP32` < {max_hum}")
   # Mostrar el DataFrame filtrado
   st.subheader("Porcentajes de humedad inferiores al valor configurado.")
   st.write('Dataframe Filtrado')
   st.write(filtrado_df_max)
   

else:
 st.warning('Necesitas cargar un archivo csv excel.')
