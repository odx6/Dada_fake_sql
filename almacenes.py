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
num_registros = 10000  # Número de registros a generar

for _ in range(num_registros):
        STRNOMALM=faker.unique.company()
        DTEHOR=faker.date()
        BITSUS=1
        STRDESALM=faker.text()
      

        cursor.execute("""
        INSERT INTO
       `tblcatalm`(
       
        `STRNOMALM`,
        `DTEHOR`,
        `BITSUS`,
        `STRDESALM`
         )
   
         VALUES
         (
        
        %s,
        %s,
        %s,
        %s
        )
    
       """, (
         STRNOMALM,
        DTEHOR,
        BITSUS,
        STRDESALM
     ))



# Confirmar los cambios
conexion.commit()

# Cerrar la conexión
cursor.close()
conexion.close()

print(f"Se han insertado {num_registros} registros falsos en la tabla empleados.")