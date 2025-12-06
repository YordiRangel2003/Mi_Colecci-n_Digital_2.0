import os
import pickle
from datetime import datetime

coleccion = []
try:
    if os.path.isfile("armas_mw2.bin"):
        with open("armas_mw2.bin", "rb") as bf:
            coleccion = pickle.load(bf)
except:
    pass  

def registrar_errores(mensaje):
    with open("errores.log", "a", encoding="utf-8") as log:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{fecha}] {mensaje}\n")

def agregar_elemento():
    try:
        print("\n--- Agregar arma (COD MW2) ---")
        nombre = input("Nombre del arma: ").strip()
        if nombre == "":
            raise ValueError("El nombre no puede estar vacío.")

        categoria = input("Categoría (Rifle, SMG, etc.): ").strip()
        fabricante = input("Fabricante: ").strip()

        while True:
            try:
                anio = int(input("Año de lanzamiento: "))
                break
            except:
                print("Error: debe ingresar un número.")

        while True:
            try:
                dano = int(input("Daño: "))
                break
            except:
                print("Debe ingresar un número.")

        while True:
            try:
                precision = float(input("Precisión (0-100): "))
                if precision < 0 or precision > 100:
                    print("Debe estar entre 0 y 100.")
                    continue
                break
            except:
                print("Debe ingresar un número válido.")

        rareza = int(input("Rareza (1-100): "))
        if rareza < 1 or rareza > 100:
            raise ValueError("La rareza debe estar entre 1 y 100.")

        arma = {
            "nombre": nombre,
            "categoria": categoria,
            "fabricante": fabricante,
            "anio": anio,
            "dano": dano,
            "precision": precision,
            "rareza": rareza
        }
        coleccion.append(arma)

        existe = os.path.isfile("armas_mw2.txt")
        with open("armas_mw2.txt", "a", encoding="utf-8") as archivo:
            if not existe:
                archivo.write("nombre,categoria,fabricante,anio,dano,precision,rareza\n")
            archivo.write(f"{nombre},{categoria},{fabricante},{anio},{dano},{precision},{rareza}\n")

        print("Elemento agregado correctamente.")

    except Exception as e:
        registrar_errores(f"Error en agregar_elemento: {e}")
        print("Ocurrió un error al agregar el elemento.")

def mostrar_coleccion():
    print("\n--- Colección completa (archivo TXT) ---")
    try:
        with open("armas_mw2.txt", "r", encoding="utf-8") as f:
            contenido = f.read()
            if contenido.strip() == "":
                print("El archivo está vacío.")
            else:
                print(contenido)
    except FileNotFoundError:
        print("El archivo armas_mw2.txt no existe.")
    except Exception as e:
        registrar_errores(f"Error en mostrar_coleccion: {e}")
        print("Error al leer archivo.")
    finally:
        print("--- Lectura finalizada ---")

def buscar_elemento():
    try:
        print("\n--- Buscar arma por nombre ---")
        nombre_buscar = input("Nombre: ").strip().lower()
        encontrado = False

        for arma in coleccion:
            if arma["nombre"].lower() == nombre_buscar:
                print("\nElemento encontrado:")
                print(f"Nombre: {arma['nombre']}")
                print(f"Categoría: {arma['categoria']}")
                print(f"Fabricante: {arma['fabricante']}")
                print(f"Año: {arma['anio']}")
                print(f"Daño: {arma['dano']}")
                print(f"Precisión: {arma['precision']}")
                print(f"Rareza: {arma['rareza']}")
                encontrado = True

        if encontrado == False:
            print("No se encontró el elemento.")

    except Exception as e:
        registrar_errores(f"Error en buscar_elemento: {e}")
        print("Error al buscar.")

def mostrar_binario():
    print("\n--- Mostrar datos binarios ---")
    try:
        if not os.path.isfile("armas_mw2.bin"):
            print("No existe el archivo binario. Guarda datos primero.")
            return

        with open("armas_mw2.bin", "rb") as bf:
            datos = pickle.load(bf)

        for arma in datos:
            print(arma["nombre"], arma["dano"], arma["precision"], arma["rareza"])

    except Exception as e:
        registrar_errores(f"Error en mostrar_binario: {e}")
        print("Error al leer datos binarios.")

def guardar_binario():
    try:
        with open("armas_mw2.bin", "wb") as bf:
            pickle.dump(coleccion, bf)
        print("\nCatálogo guardado en BINARIO.\n")
    except Exception as e:
        registrar_errores(f"Error en guardar_binario: {e}")

def cargar_binario():
    try:
        if not os.path.isfile("armas_mw2.bin"):
            print("\nNo existe un archivo binario para cargar.\n")
            return

        with open("armas_mw2.bin", "rb") as bf:
            data = pickle.load(bf)

        coleccion.clear()
        coleccion.extend(data)
        print("\nCatálogo cargado desde BINARIO.\n")

    except Exception as e:
        registrar_errores(f"Error en cargar_binario: {e}")
        print("Error al cargar binario.")

def exportar():
    try:
        with open("exportado_armas_mw2.txt", "w", encoding="utf-8") as archivo:
            archivo.write("======= CATÁLOGO DE ARMAS MW2 =======\n\n")
            for arma in coleccion:
                archivo.write(
                    f"Nombre: {arma['nombre']}\n"
                    f"Categoría: {arma['categoria']}\n"
                    f"Fabricante: {arma['fabricante']}\n"
                    f"Año de lanzamiento: {arma['anio']}\n"
                    f"Daño: {arma['dano']}\n"
                    f"Precisión: {arma['precision']}\n"
                    f"Rareza: {arma['rareza']}\n"
                    "-------------------------------------\n"
                )
        print("\nCatálogo exportado correctamente (formato detallado).\n")

    except Exception as e:
        registrar_errores(f"Error en exportar: {e}")
        print("Error al exportar.")


def menu():
    while True:
        print("\n>>>>> COLECCIÓN DE ARMAS: CALL OF DUTY MW2 <<<<<")
        print("1. Agregar elemento")
        print("2. Mostrar colección completa")
        print("3. Buscar elemento por nombre")
        print("4. Mostrar datos binarios")
        print("5. Guardar catálogo en binario")
        print("6. Cargar catálogo en binario")
        print("7. Exportar catálogo a TXT")
        print("8. salir")   

        try:
            opcion = int(input("Elige una opción: "))
        except:
            print("Debes ingresar un número.")
            continue

        if opcion == 1:
            agregar_elemento()
        elif opcion == 2:
            mostrar_coleccion()
        elif opcion == 3:
            buscar_elemento()
        elif opcion == 4:
            mostrar_binario()
        elif opcion == 5:
            guardar_binario()
        elif opcion == 6:
            cargar_binario()
        elif opcion == 7:
            exportar()
        elif opcion == 8:
            print(" Saliendo.......")
            break         
        else:
            print("Opción inválida.")

menu()
