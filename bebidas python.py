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

