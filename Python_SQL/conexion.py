"""Para conectar MYSQL o SQL con python, se realiza l siguiente codigo para configurarlo con SQLite"""

import sqlite3
# Este es el conector para MySQL
# import pymysql

#conexion = sqlite3.connect("bases_prueba.db")
#cursor = conexion.cursor()


def obtener_clientes():
    conexion = sqlite3.connect("bases_prueba.db")
    cursor = conexion.cursor()
    sql = "SELECT * FROM clientes;"
    cursor.execute(sql)
    # fetchall se utiliza cuando tengo más de un registro, fetchone es un solo registro
    clientes = cursor.fetchall()
    # print(clientes[5][1])
    # Imprime las tuplas por separado
    for cliente in clientes:
        print(cliente)
    conexion.commit()
    conexion.close()

# Agregar clientes directo a la base de datos


def agregar_cliente(nombre, apellido, email, fecha_registro, roles, telefono="None"):
    conexion = sqlite3.connect("bases_prueba.db")
    cursor = conexion.cursor()
    cliente = (
        nombre,
        apellido,
        email,
        fecha_registro,
        telefono,
        roles

)
    sql = f"INSERT INTO clientes (nombre, apellido, email, fecha_registro, telefono, roles) VALUES {cliente}"
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def obtener_un_cliente(id):
    conexion = sqlite3.connect("bases_prueba.db")
    cursor = conexion.cursor()
    sql = f"SELECT *FROM clientes WHERE id = {id}"
    cursor.execute(sql)
    cliente = cursor.fetchone()
    print(cliente)
    conexion.commit()
    conexion.close()

def editar_un_cliente(id, nombre):
    conexion = sqlite3.connect("bases_prueba.db")
    cursor = conexion.cursor()    
    sql = f"UPDATE clientes SET nombre = '{nombre}' WHERE id = {id}"
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def eliminar_cliente(id):
    conexion = sqlite3.connect("bases_prueba.db")
    cursor = conexion.cursor()    
    sql = f"DELETE FROM clientes WHERE id = {id}"
    cursor.execute(sql)
    conexion.commit()
    conexion.close()


def programa():
    try:
        menu = int(input("""
Ingrese la acción que desea realizar: \n
[1] Mostrar clientes
[2] Agregar un cliente
[3] Eliminar cliente
[4] Mostrar un cliente
[5] Editar un cliente
[6] Salir\n
>>>>>  """))
        print(f"Ha ingresado la opción {menu}")
        if menu >= 7 or menu <= 0:
           print("Está opción no es válida, ingrese un valor entre 1 y 6")

        if menu == 1:
           obtener_clientes()
           

        if menu == 2:
            nombre = str(input("Ingrese el nombre del usuario: "))
            apellido = str(input("Ingrese el apellido del usuario: "))
            correo = input("Ingrese el correo del usuario: ")
            fecha_ingreso = input("Ingrese la fecha de ingreso del usuario: ")
            rol = str(input("Ingrese el rol del usuario: "))
            agregar_cliente(nombre, apellido, correo, fecha_ingreso, rol)

        if menu == 3:
            id_1 = int(input("Ingrese el registro que quiere eliminar: "))
            seguro = input("Esta seguro que desea eliminar este registro, marque S si está seguro o N si quiere cancelar: ")
            if seguro == 'S':
                eliminar_cliente(id_1)
                print(f"Se elimino el registro {id_1}")
            else:
                print("No se elimino ningín registro ")
              
        if menu == 4:
            mostar_cl = int(input("Ingrese el id del cliente que quiere consultar: "))
            obtener_un_cliente(mostar_cl)

        if menu == 5:
            edit_id = int(input("Ingrese el id que desea editar: "))
            edit_no = input("Ingrese el nombre a cambiar: ") 
            editar_un_cliente(edit_id, edit_no)
            print(f"""El cliente con id = {edit_id} se edito correctamente.\n """)
            obtener_un_cliente(edit_id)
            

        if menu == 6:
           exit()
           

    except ValueError as error:
        print(f"\nNo puede ingresar este dato, error: {error}")

#Permite que el menu se vuelva a repetir hasta que de la opción de salir 5
while True:
   programa()
