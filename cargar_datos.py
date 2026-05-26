import pandas as pd

from configuracion import Session
from entidades import Continente, Pais, Jugador


def obtener_continente(nombre_pais):
    europa = ["Alemania", "España", "Francia", "Inglaterra", "Portugal"]
    america = ["Argentina", "Brasil", "Ecuador", "Estados Unidos", "México"]
    asia = ["Japón"]
    africa = ["Marruecos", "Nigeria", "Senegal"]

    if nombre_pais in europa:
        return "Europa"
    elif nombre_pais in america:
        return "América"
    elif nombre_pais in asia:
        return "Asia"
    elif nombre_pais in africa:
        return "África"
    else:
        return "Sin continente"


session = Session()

df = pd.read_csv("data/jugadores_futbol.csv")

for fila in df.itertuples():

    nombre_continente = obtener_continente(fila.pais_nacimiento)

    continente = session.query(Continente).filter_by(
        nombre=nombre_continente
    ).first()

    if continente is None:
        continente = Continente(nombre=nombre_continente)
        session.add(continente)
        session.commit()

    pais = session.query(Pais).filter_by(
        nombre=fila.pais_nacimiento
    ).first()

    if pais is None:
        pais = Pais(
            nombre=fila.pais_nacimiento,
            continente=continente
        )
        session.add(pais)
        session.commit()

    jugador = Jugador(
        nombre_jugador=fila.nombre_jugador,
        pais_donde_juega=fila.pais_donde_juega,
        posicion=fila.posicion,
        edad=int(fila.edad),
        numero_partidos_seleccion=int(fila.numero_partidos_seleccion),
        goles_seleccion=int(fila.goles_seleccion),
        pais_nacimiento=pais
    )

    session.add(jugador)

session.commit()
session.close()

print("Datos cargados correctamente desde el CSV.")