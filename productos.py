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
num_registros = 5000  # Número de registros a generar

for _ in range(num_registros):
    
        STRSKU=faker.isbn10()
        STRCOD=faker.isbn13()
        STRDESPRO=faker.name()
        INTIDSBC=1
        MONPCOS=1
        INTIDUNI=2
        STRIMG=''
        INTTIPUSO=1
        BITSUS=1
        INTIDCAT=1
        CREATE_AT=faker.date()
        loked=0
        Editor=0
        
      

        cursor.execute("""
    INSERT INTO
    `tblcatpro`(
        `STRSKU`,
        `STRCOD`,
        `STRDESPRO`,
        `INTIDSBC`,
        `MONPCOS`,
        `INTIDUNI`,
        `STRIMG`,
        `INTTIPUSO`,
        `BITSUS`,
        `INTIDCAT`,
        `CREATE_AT`,
        `loked`,
        `Editor`
    )
         VALUES
         (
        
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
        )
    
       """, (
        STRSKU,
        STRCOD,
        STRDESPRO,
        INTIDSBC,
        MONPCOS,
        INTIDUNI,
        STRIMG,
        INTTIPUSO,
        BITSUS,
        INTIDCAT,
        CREATE_AT,
        loked,
        Editor
       
     ))



# Confirmar los cambios
conexion.commit()

# Cerrar la conexión
cursor.close()
conexion.close()

print(f"Se han insertado {num_registros} registros falsos en la tabla empleados.")