import mysql.connector as sql

db = sql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="laravel"
)

cursor = db.cursor()

import pandas as pd
from sqlalchemy import create_engine

opcion = 0

def menu():
    opc = int(input("Menu Principal \n" +
        "1. Carga masiva a DB \n" +
        "2. Consultar tarjeta \n" +
        "3. Finalizar  \n" +
        "Elija una Opcion... \n")) 
    return opc

def cargar_datos():
    df = pd.read_excel('DataPrueba.xlsx')

    engine = create_engine('mysql://root:@localhost/laravel')
    df.to_sql('tarjetas_credito', con=engine, if_exists='append', index=False)

    print ("CARGA TERMINADA!") 
        
def consulta(codigo,nombre,apellido1,apellido2,no_tarjeta):

    consulta = """
        SELECT * FROM `prueba` WHERE `COD_SOCIO`= {0}
        and `NOMBRE`='{1}' 
        and `APELLIDO1` = '{2}' 
        and `APELLIDO 2`='{3}' 
        and `#_TC`= {4}""".format(codigo,nombre,apellido1,apellido2,no_tarjeta)

    cursor.execute(consulta)

    for dato in cursor:
        print(dato)
    
while opcion != 3:
    opcion = menu()
    if opcion == 1:
        cargar_datos()

    if opcion == 2:
        print("* EL NOMBRE DEBE DE IR EN MAYUSCULAS")

        codigo = int(input("Codigo: \n"))
        nombre = str(input("Nombre: \n"))  
        apellido1 = str(input("Apellido: \n"))
        apellido2 = str(input("Apellido: \n"))
        no_tarjeta = int(input("Numero de tarjeta: \n"))

        resultado = consulta(codigo, nombre, apellido1, apellido2, no_tarjeta)
  
    if opcion == 3:    
        print("Programa terminado")
        
    if opcion > 3:
        print("opcion invalida")