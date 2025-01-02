import mysql.connector
from faker import Faker

# Conexión a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="taller2"
)

cursor = conexion.cursor()

# Generar datos falsos
faker = Faker()
num_registros = 1000  # Número de registros a generar

for _ in range(num_registros):
        STRDSCORG=faker.unique.company()
        BITSUS=1
        DTEHOR=faker.date()
      

        cursor.execute("""
      INSERT INTO
    `tblcatorg`( `STRDSCORG`, `BITSUS`, `DTEHOR`)
   
         VALUES
         (
        
        %s,
        %s,
        %s
        )
    
       """, (
         STRDSCORG,
        BITSUS,
        DTEHOR
       
     ))



# Confirmar los cambios
conexion.commit()

# Cerrar la conexión
cursor.close()
conexion.close()

print(f"Se han insertado {num_registros} registros falsos en la tabla empleados.")