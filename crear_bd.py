from configuracion import engine
from entidades import Base

Base.metadata.create_all(engine)

print("Base de datos y tablas creadas correctamente.")