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
        INTIDCAT=2
        STRNOMSBC=faker.unique.company()
        STRDESBC=faker.text()
        DTEHOR=faker.date()
        BITSUS=1
      

        cursor.execute("""
     INSERT INTO
     `tblcatsbc`(
        `INTIDCAT`,
        `STRNOMSBC`,
        `STRDESBC`,
        `DTEHOR`,
        `BITSUS`
      )
         VALUES
         (
        
        %s,
        %s,
        %s,
        %s,
        %s
        )
    
       """, (
       INTIDCAT,
       STRNOMSBC,
       STRDESBC,
       DTEHOR,
       BITSUS
       
     ))



# Confirmar los cambios
conexion.commit()

# Cerrar la conexión
cursor.close()
conexion.close()

print(f"Se han insertado {num_registros} registros falsos en la tabla empleados.")