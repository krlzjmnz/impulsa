import pandas as pd
from datetime import datetime
import os

def leer_pendientes():
    if os.path.exists('pendientes.csv'):
        df = pd.read_csv('pendientes.csv')
        # FORZAR tipos compatibles para evitar warnings
        if 'fecha_inicio' in df.columns:
            df['fecha_inicio'] = df['fecha_inicio'].astype(str)
        if 'fecha_fin' in df.columns:
            df['fecha_fin'] = df['fecha_fin'].astype(str)
        return df
    return pd.DataFrame()


def guardar_pendientes(df):
    df.to_csv('pendientes.csv', index=False, encoding='utf-8')

def crear_pendiente(df):
    contador = len(df) + 1
    print(f"\n=== NUEVA PENDIENTE #{contador} ===")
    
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"Fecha sugerida: {fecha_actual}")
    usar_fecha = input("¿Usar fecha actual? (s/n): ").lower()
    fecha_inicio = fecha_actual if usar_fecha == 's' else input("Fecha inicio (YYYY-MM-DD HH:MM): ")
    
    membresia = input("Nombre o número de membresía: ")
    descripcion = input("Descripción: ")
    
    nuevo_registro = {
        'contador': contador,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': '',
        'descripcion': descripcion,
        'membresia': membresia
    }
    
    df = pd.concat([df, pd.DataFrame([nuevo_registro])], ignore_index=True)
    guardar_pendientes(df)
    print("✅ Pendiente creada!")

def listar_pendientes(df):
    if df.empty:
        print("No hay pendientes.")
        return
    
    print("\n=== LISTA DE PENDIENTES ===")
    for _, row in df.iterrows():
        # SOLO mostrar si TIENE fecha_fin (terminados) o está vacío (pendientes)
        if pd.isna(row['fecha_fin']) or row['fecha_fin'] == 'nan':
            
            status = "⏳ PENDIENTE"
        else:
            print(f'el campo es {row['fecha_fin']}')
            status = f"✅ TERMINADA el {row['fecha_fin']}"
        
        print(f"#{row['contador']} {status} | {row['membresia']} | {row['descripcion'][:50]}...")

def editar_pendiente(df):
    if df.empty:
        print("No hay pendientes.")
        return
    
    listar_pendientes(df)
    try:
        num = int(input("\nNúmero de pendiente a editar: "))
        indice = df[df['contador'] == num].index[0]
        
        print("\nCampos disponibles:")
        print("1. fecha_inicio  2. fecha_fin  3. descripcion  4. membresia")
        
        campo = input("Campo a editar (1-4): ")
        campo_map = {
            '1': 'fecha_inicio', '2': 'fecha_fin', 
            '3': 'descripcion', '4': 'membresia'
        }
        
        nuevo_valor = input(f"Nuevo valor para {list(campo_map.keys())[list(campo_map.values()).index(campo_map[campo])]}: ")
        df.at[indice, campo_map[campo]] = nuevo_valor
        guardar_pendientes(df)
        print("✅ Editado!")
        
    except:
        print("Error: Número no válido.")

def terminar_pendiente(df):
    if df.empty:
        print("No hay pendientes.")
        return
    
    listar_pendientes(df)
    try:
        num = int(input("\nNúmero de pendiente a terminar: "))
        indice = df[df['contador'] == num].index[0]
        
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"Fecha sugerida: {fecha_actual}")
        usar_fecha = input("¿Usar fecha actual? (s/n): ").lower()
        fecha_fin = fecha_actual if usar_fecha == 's' else input("Fecha fin (YYYY-MM-DD HH:MM): ")
        
        df.at[indice, 'fecha_fin'] = fecha_fin
        guardar_pendientes(df)
        print("✅ Pendiente terminada!")
        
    except:
        print("Error: Número no válido.")

def menu():
    df = pd.DataFrame()
    
    while True:
        print("\n=== GESTOR DE PENDIENTES ===")
        print("1. Crear")
        print("2. Listar")
        print("3. Editar")
        print("4. Terminar")
        print("0. Salir")
        
        opcion = input("Elige opción: ")
        
        df = leer_pendientes()  # Recargar datos
        
        if opcion == '1':
            crear_pendiente(df)
        elif opcion == '2':
            listar_pendientes(df)
        elif opcion == '3':
            editar_pendiente(df)
        elif opcion == '4':
            terminar_pendiente(df)
        elif opcion == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
