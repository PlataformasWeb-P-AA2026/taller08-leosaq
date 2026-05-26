# Integración de datos y uso de ORM

## Crear entorno virtual

### Windows (Git Bash)

```bash
python -m venv .venv
source .venv/Scripts/activate
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Uso con SQLite

## Crear base de datos

```bash
python crear_bd.py
```

Se generará automáticamente:

```text
paises.db
```

## Cargar información del CSV

```bash
python cargar_datos.py
```

## Ejecutar la aplicación Streamlit

```bash
streamlit run app.py
```

---

# Uso con MariaDB

## Levantar contenedor Docker

```bash
docker compose up -d
```

Verificar:

```bash
docker ps
```

Debe aparecer:

```text
orm_paises_mariadb
```

---

## Cambiar conexión

Modificar temporalmente el archivo:

```python
# configuracion.py
cadena_base_datos = "mysql+pymysql://root:root@localhost:3307/paises"
```

---

## Crear tablas

```bash
python crear_bd.py
```

---

## Cargar datos

```bash
python cargar_datos.py
```

---

## Verificar tablas

Ingresar al contenedor:

```bash
winpty docker exec -it orm_paises_mariadb mariadb -u root -proot
```

Dentro de MariaDB:

```sql
USE paises;

SHOW TABLES;

SELECT COUNT(*) FROM jugadores;
```

---

## Ejecutar Streamlit con MariaDB

```bash
streamlit run app.py
```

---


## Evidencia de SQLite con Fronted Streamlit 
<img width="1600" height="955" alt="image" src="https://github.com/user-attachments/assets/4e42ec3a-1eba-4a85-855a-cb69b45c709b" />


## Evidencia de MariaDB con Fronted Streamlit 
<img width="1600" height="954" alt="image" src="https://github.com/user-attachments/assets/852d9cbb-59b7-4360-990c-cf0acfb77599" />
