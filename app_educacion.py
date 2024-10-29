import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.title("Aplicación de Consultas Educativas")

# Opción para cargar un archivo CSV de manera externa
uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")

if uploaded_file is not None:
    datos = pd.read_csv(uploaded_file)  # Cargar el archivo CSV subido
    st.write("Datos cargados exitosamente:")
    st.dataframe(datos)
else:
    # Cargar el archivo por defecto
    ruta_csv = os.path.join("static", "educacion.csv")
    datos = pd.read_csv(ruta_csv)
    st.write("Datos cargados por defecto:")
    st.dataframe(datos)
    
# Filtrado de datos
st.sidebar.header("Filtrar Datos")

# Filtrar por nivel educativo
nivel_educativo = st.sidebar.selectbox("Selecciona el Nivel Educativo", options=datos['Nivel_Educativo'].unique())
datos_filtrados = datos[datos['Nivel_Educativo'] == nivel_educativo]

# Filtrar por carrera
carrera = st.sidebar.selectbox("Selecciona la Carrera", options=datos_filtrados['Carrera'].unique())
datos_filtrados = datos_filtrados[datos_filtrados['Carrera'] == carrera]

# Filtrar por institución
institucion = st.sidebar.selectbox("Selecciona la Institución", options=datos_filtrados['Institución'].unique())
datos_filtrados = datos_filtrados[datos_filtrados['Institución'] == institucion]

# Mostrar los datos filtrados
st.write("Datos filtrados:")
st.dataframe(datos_filtrados)

# Estadísticas descriptivas
st.subheader("Estadísticas Descriptivas")
if not datos_filtrados.empty:
    # Edad promedio
    edad_promedio = datos_filtrados['Edad'].mean()
    st.write(f"Edad Promedio: {edad_promedio:.2f} años")
    
    # Conteo de estudiantes por nivel educativo
    conteo_nivel = datos_filtrados['Nivel_Educativo'].value_counts()
    st.write("Conteo de Estudiantes por Nivel Educativo:")
    st.bar_chart(conteo_nivel)

    # Histograma de la distribución de la edad
    st.subheader("Distribución de Edad")
    fig, ax = plt.subplots()
    ax.hist(datos_filtrados['Edad'], bins=10, color='blue', alpha=0.7)
    ax.set_title('Distribución de Edad')
    ax.set_xlabel('Edad')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)
else:
    st.write("No hay datos disponibles para mostrar estadísticas.")
