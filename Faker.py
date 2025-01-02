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
        STRNSS=faker.name()
        STRRFC=faker.ssn()
        STRCUR=faker.ssn()
        STRNDL=faker.vin()
        DTHLIC=faker.postcode()
        STRNOM=faker.first_name_nonbinary()
        STRAPE=faker.last_name()
        STRDOM=faker.address()
        STRLOC=faker.name()
        STRMUN=faker.name()
        STREST=faker.name()
        STRCP=faker.postcode()
        STRPAI=faker.country()
        STRTEL=faker.phone_number()
        STRCOR=faker.email()
        STRPWS=faker.password()
        BITSUS=1
        STRIMG='NULL'
        CREATE_AT=faker.date()
        TOKEN='NULL'
        VERIFICATE_AT=faker.date()
        numsesion=50

        cursor.execute("""
        INSERT INTO `tblcatemp`( `STRNSS`, `STRRFC`, `STRCUR`, `STRNDL`, `DTHLIC`, `STRNOM`, `STRAPE`, `STRDOM`, `STRLOC`, `STRMUN`, `STREST`, `STRCP`, `STRPAI`, `STRTEL`, `STRCOR`, `STRPWS`, `BITSUS`, `STRIMG`, `CREATE_AT`, `TOKEN`, `VERIFICATE_AT`, `numsesion`)
   
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
         STRNSS,
        STRRFC,
        STRCUR,
        STRNDL,
        DTHLIC,
        STRNOM,
        STRAPE,
        STRDOM,
        STRLOC,
        STRMUN,
        STREST,
        STRCP,
        STRPAI,
        STRTEL,
        STRCOR,
        STRPWS,
        BITSUS,
        STRIMG,
        CREATE_AT,
        TOKEN,
        VERIFICATE_AT,
        numsesion
     ))



# Confirmar los cambios
conexion.commit()

# Cerrar la conexión
cursor.close()
conexion.close()

print(f"Se han insertado {num_registros} registros falsos en la tabla empleados.")

