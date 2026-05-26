from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


cadena_base_datos = "sqlite:///paises.db"

#cadena_base_datos = "mysql+pymysql://root:root@localhost:3307/paises"

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)