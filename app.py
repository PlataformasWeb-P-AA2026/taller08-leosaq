import streamlit as st
import pandas as pd

from configuracion import engine


st.set_page_config(
    page_title="Jugadores de fútbol",
    layout="wide"
)

st.title("Integración de datos con ORM")
st.subheader("Jugadores de fútbol")


consulta_jugadores = """
SELECT
    j.nombre_jugador,
    p.nombre AS pais_nacimiento,
    j.pais_donde_juega,
    j.posicion,
    j.edad,
    j.numero_partidos_seleccion,
    j.goles_seleccion,
    c.nombre AS continente
FROM jugadores j
JOIN paises p ON j.pais_nacimiento_id = p.id
JOIN continentes c ON p.continente_id = c.id
"""

df_jugadores = pd.read_sql(consulta_jugadores, engine)

st.write("Tabla general de jugadores")
st.dataframe(df_jugadores, use_container_width=True)


consulta_continentes = """
SELECT
    c.nombre AS continente,
    COUNT(j.id) AS numero_jugadores,
    SUM(j.goles_seleccion) AS numero_goles
FROM jugadores j
JOIN paises p ON j.pais_nacimiento_id = p.id
JOIN continentes c ON p.continente_id = c.id
GROUP BY c.nombre
"""

df_continentes = pd.read_sql(consulta_continentes, engine)

st.write("Resumen por continente")
st.dataframe(df_continentes, use_container_width=True)


consulta_paises = """
SELECT
    p.nombre AS pais,
    COUNT(j.id) AS numero_jugadores,
    SUM(j.goles_seleccion) AS numero_goles
FROM jugadores j
JOIN paises p ON j.pais_nacimiento_id = p.id
GROUP BY p.nombre
"""

df_paises = pd.read_sql(consulta_paises, engine)

st.write("Resumen por país")
st.dataframe(df_paises, use_container_width=True)