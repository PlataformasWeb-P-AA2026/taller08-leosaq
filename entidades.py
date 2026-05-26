from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Continente(Base):
    __tablename__ = "continentes"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False, unique=True)

    paises = relationship("Pais", back_populates="continente")


class Pais(Base):
    __tablename__ = "paises"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False, unique=True)

    continente_id = Column(Integer, ForeignKey("continentes.id"))
    continente = relationship("Continente", back_populates="paises")

    jugadores = relationship("Jugador", back_populates="pais_nacimiento")


class Jugador(Base):
    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True)

    nombre_jugador = Column(String(120), nullable=False)
    pais_donde_juega = Column(String(80), nullable=False)
    posicion = Column(String(80), nullable=False)
    edad = Column(Integer)
    numero_partidos_seleccion = Column(Integer)
    goles_seleccion = Column(Integer)

    pais_nacimiento_id = Column(Integer, ForeignKey("paises.id"))
    pais_nacimiento = relationship("Pais", back_populates="jugadores")