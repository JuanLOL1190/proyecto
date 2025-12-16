import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

st.set_page_config(page_title="Proyecto Final - Estadística", layout="centered")

st.title("📊 Proyecto Final de Estadística")
st.subheader("Análisis Estadístico e Inferencia")

# Creamos las pestañas
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Calculadora",
    "📈 Medidas",
    "🔍 Inferencia",
    "👥 Dos poblaciones",
    "ℹ️ Acerca de"
])

# --------------------
# PESTAÑA 1: CALCULADORA
# --------------------
with tab1:
    st.header("Ingreso de Datos")
    st.write("Ingresa una lista de números separados por comas:")

    st.code("10, 20, 15, 30, 25")

    data_input = st.text_area("Datos:")

    if st.button("Cargar datos"):
        try:
            data = [float(x.strip()) for x in data_input.split(",")]
            st.session_state["datos"] = data
            st.success("Datos cargados correctamente")
            st.write("Tamaño de la muestra:", len(data))
        except:
            st.error("Error al leer los datos")

# --------------------
# PESTAÑA 2: MEDIDAS
# --------------------
with tab2:
    st.header("Medidas de Tendencia Central y Dispersión")

    if "datos" in st.session_state:
        data = st.session_state["datos"]

        media = np.mean(data)
        mediana = np.median(data)
        desviacion = np.std(data, ddof=1)
        varianza = np.var(data, ddof=1)

        st.write(f"**Media:** {media:.4f}")
        st.write(f"**Mediana:** {mediana:.4f}")
        st.write(f"**Desviación estándar:** {desviacion:.4f}")
        st.write(f"**Varianza:** {varianza:.4f}")

        st.subheader("Histograma")
        fig, ax = plt.subplots()
        ax.hist(data, bins=10)
        st.pyplot(fig)

        st.markdown("""
        ### 📌 Conceptos:
        - **Media:** promedio de los datos  
        - **Mediana:** valor central  
        - **Desviación estándar:** dispersión de los datos  
        - **Histograma:** representación gráfica de la distribución  
        """)

    else:
        st.warning("Primero carga datos en la pestaña Calculadora")

# --------------------
# PESTAÑA 3: INFERENCIA
# --------------------
with tab3:
    st.header("Inferencia Estadística")

    st.markdown("""
    ### Temas incluidos:
    - Error estándar  
    - Intervalo de confianza de la media  
    - Intervalo de confianza de una proporción  
    - Cálculo de **Z** y **t**  
    - Tamaño de muestra  
    """)

    if "datos" in st.session_state:
        data = st.session_state["datos"]
        n = len(data)
        media = np.mean(data)
        desviacion = np.std(data, ddof=1)
        error_estandar = desviacion / np.sqrt(n)

        st.write(f"**Error estándar:** {error_estandar:.4f}")

        nivel = st.selectbox("Nivel de confianza:", [90, 95, 99])
        alpha = 1 - nivel / 100

        t_crit = stats.t.ppf(1 - alpha / 2, df=n - 1)
        li = media - t_crit * error_estandar
        ls = media + t_crit * error_estandar

        st.write(f"**Intervalo de confianza ({nivel}%):**")
        st.write(f"[{li:.4f}, {ls:.4f}]")

    else:
        st.warning("Carga datos para aplicar inferencia")

# --------------------
# PESTAÑA 4: DOS POBLACIONES
# --------------------
with tab4:
    st.header("Análisis de Dos Poblaciones")

    st.markdown("""
    ### Contenido:
    - Diferencia de medias  
    - Diferencia de proporciones  
    - Pruebas de hipótesis  
    """)

    st.write("Ingresa datos para dos poblaciones:")

    col1, col2 = st.columns(2)

    with col1:
        data1 = st.text_area("Población 1")

    with col2:
        data2 = st.text_area("Población 2")

    if st.button("Analizar poblaciones"):
        try:
            p1 = np.array([float(x) for x in data1.split(",")])
            p2 = np.array([float(x) for x in data2.split(",")])

            diff_medias = np.mean(p1) - np.mean(p2)

            st.success("Cálculo exitoso")
            st.write(f"**Diferencia de medias:** {diff_medias:.4f}")

        except:
            st.error("Error en los datos")

# --------------------
# PESTAÑA 5: ACERCA DE
# --------------------
with tab5:
    st.header("Acerca del Proyecto")

    st.markdown("""
    **Proyecto Final de Estadística**

    Esta aplicación integra los temas vistos en clase:
    - Medidas de tendencia central  
    - Distribuciones muestrales  
    - Teorema del Límite Central  
    - Inferencia estadística  
    - Intervalos de confianza  
    - Pruebas de hipótesis  
    - Análisis de dos poblaciones  

    Desarrollado con **Python, Streamlit, NumPy y SciPy**.
    """)
