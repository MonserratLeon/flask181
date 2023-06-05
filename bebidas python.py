import sqlite3

# crear la tabla de bebidas en la base de datos
def crear_tabla():
    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bebidas
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nombre TEXT NOT NULL,
                  clasificacion TEXT NOT NULL,
                  marca TEXT NOT NULL,
                  precio REAL NOT NULL)''')
    conn.commit()
    conn.close()

#  agregar una nueva bebida
def agregar_bebida():
    nombre = input("Ingrese el nombre de la bebida: ")
    clasificacion = input("Ingrese la clasificación de la bebida: ")
    marca = input("Ingrese la marca de la bebida: ")
    precio = float(input("Ingrese el precio de la bebida: "))

    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("INSERT INTO bebidas (nombre, clasificacion, marca, precio) VALUES (?, ?, ?, ?)",
              (nombre, clasificacion, marca, precio))
    conn.commit()
    conn.close()
    print("Bebida agregada con éxito.")

# eliminar una bebida
def eliminar_bebida():
    id_bebida = int(input("Ingrese el ID de la bebida a eliminar: "))

    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("DELETE FROM bebidas WHERE id=?", (id_bebida,))
    conn.commit()
    conn.close()
    print("Bebida eliminada con éxito.")

# actualizar los datos de una bebida
def actualizar_bebida():
    id_bebida = int(input("Ingrese el ID de la bebida a actualizar: "))
    nombre = input("Ingrese el nuevo nombre de la bebida: ")
    clasificacion = input("Ingrese la nueva clasificación de la bebida: ")
    marca = input("Ingrese la nueva marca de la bebida: ")
    precio = float(input("Ingrese el nuevo precio de la bebida: "))

    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("UPDATE bebidas SET nombre=?, clasificacion=?, marca=?, precio=? WHERE id=?",
              (nombre, clasificacion, marca, precio, id_bebida))
    conn.commit()
    conn.close()
    print("Bebida actualizada con éxito.")

# mostrar todas las bebidas
def mostrar_bebidas():
    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bebidas")
    bebidas = c.fetchall()
    conn.close()

    if len(bebidas) == 0:
        print("No hay bebidas registradas.")
    else:
        print("ID  | Nombre                 | Clasificación   | Marca           | Precio")
        print("----|------------------------|-----------------|-----------------|-------")
        for bebida in bebidas:
            print(f"{bebida[0]:<4} | {bebida[1]:<23} | {bebida[2]:<15} | {bebida[3]:<15} | {bebida[4]:.2f}")

# calcular el precio promedio de las bebidas
def calcular_precio_promedio():
    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("SELECT AVG(precio) FROM bebidas")
    resultado = c.fetchone()[0]
    conn.close()

    if resultado is None:
        print("No hay bebidas registradas.")
    else:
        print(f"Precio promedio de las bebidas: {resultado:.2f}")
# contar la cantidad de bebidas de una marca
def contar_bebidas_marca():
    marca = input("Ingrese el nombre de la marca: ")

    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM bebidas WHERE marca=?", (marca,))
    resultado = c.fetchone()[0]
    conn.close()

    print(f"Cantidad de bebidas de la marca '{marca}': {resultado}")

# cantidad de bebidas por clasificación
def contar_bebidas_clasificacion():
    conn = sqlite3.connect('almacen_bebidas.db')
    c = conn.cursor()
    c.execute("SELECT clasificacion, COUNT(*) FROM bebidas GROUP BY clasificacion")
    resultados = c.fetchall()
    conn.close()

    if len(resultados) == 0:
        print("No hay bebidas registradas.")
    else:
        print("Clasificación     | Cantidad")
        print("------------------|---------")
        for resultado in resultados:
            print(f"{resultado[0]:<17} | {resultado[1]}")

# muestra el menú y maneja la interacción con el usuario
def main():
    crear_tabla()

    while True:
        print("\n--- Almacén de Bebidas ---")
        print("1. Agregar bebida")
        print("2. Eliminar bebida")
        print("3. Actualizar bebida")
        print("4. Mostrar todas las bebidas")
        print("5. Calcular precio promedio de bebidas")
        print("6. Cantidad de bebidas de una marca")
        print("7. Cantidad por clasificación")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_bebida()
        elif opcion == "2":
            eliminar_bebida()
        elif opcion == "3":
            actualizar_bebida()
        elif opcion == "4":
            mostrar_bebidas()
        elif opcion == "5":
            calcular_precio_promedio()
        elif opcion == "6":
            contar_bebidas_marca()
        elif opcion == "7":
            contar_bebidas_clasificacion()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
