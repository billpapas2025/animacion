import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
import time

# Función para generar los datos
def generate_data(frame, function, frequency, amplitude):
    x = np.linspace(0, 4 * np.pi, 100)
    if function == 'Seno':
        y = amplitude * np.sin(frequency * x + frame / 10)
    elif function == 'Coseno':
        y = amplitude * np.cos(frequency * x + frame / 10)
    elif function == 'Tangente':
        y = amplitude * np.tan(frequency * x + frame / 10)
        y = np.clip(y, -10, 10)  # Clipping para evitar valores extremos
    return pd.DataFrame({'x': x, 'y': y})

# Función principal de Streamlit
def main():
    st.title("Animación de Funciones Trigonométricas con Altair")

    # Controles de usuario
    function = st.sidebar.selectbox("Selecciona la función", ["Seno", "Coseno", "Tangente"])
    frequency = st.sidebar.slider("Frecuencia", 0.1, 2.0, 1.0, 0.1)
    amplitude = st.sidebar.slider("Amplitud", 0.1, 2.0, 1.0, 0.1)

    # Contenedor para la gráfica
    chart_placeholder = st.empty()

    # Animación
    for frame in range(100):
        data = generate_data(frame, function, frequency, amplitude)
        chart = alt.Chart(data).mark_line().encode(
            x=alt.X('x', title='x'),
            y=alt.Y('y', title='y', scale=alt.Scale(domain=[-2 * amplitude, 2 * amplitude]))
        ).properties(
            width=600,
            height=400
        )
        chart_placeholder.altair_chart(chart)
        time.sleep(0.1)  # Pausa para simular la animación

if __name__ == "__main__":
    main()
