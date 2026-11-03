import pandas as pd
import unicodedata
import os

from datetime import datetime

from fpdf import FPDF
from fpdf.enums import XPos, YPos

from tabulate import tabulate

df=pd.read_csv('productos.csv', encoding='latin-1')
pedido={}

#
###### Menus
#

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def remover_acentos(texto):
    """Función para remover acentos y convertir a minúsculas."""
    if pd.isna(texto):
        return texto
    # Normaliza a una forma que separa caracteres base y acentos
    nfkd_form = unicodedata.normalize('NFKD', str(texto))
    # Codifica y decodifica para eliminar caracteres de diacríticos (acentos)
    solo_letras = "".join([c for c in nfkd_form if not unicodedata.combining(c)])
    return solo_letras.lower()

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('buscar producto',buscarProducto),
        '2': ('crear pedido', crearPedido),
        '3': ('Inventario', listarProductos),
        '4': ('Pendientes',gestionPendientes),
        '5': ('Caja',registroCaja),
        '6': ('salir',salir)
    }
    generar_menu(opciones, '6')

def menu_busqueda():
    opciones={
        '1':('Por nombre: ', busquedaNombre),
        '2':('Por pv',busquedaPv),
        '3':('Regresar',regresar)
    }
    generar_menu(opciones,'3')

def menu_caja():
    opciones={
        '1':('Registro ', registros),
        '2':('Ventas', ),
        '3':('Regresar',regresar)
    }
    generar_menu(opciones,'3')

def registros():
    opciones={
        '1':('Registro Gastos', ),
        '2':('Registro sin facturar',),
        '3':('Registro facturado sin registro de dinero',),
        '4':('Regresar',regresar),
    }
    generar_menu(opciones,'4')

# def menu_registro():
#     opciones={
#         '1':('tranferencia',),
#         '2':('Terminal',),
#         '3':('Arqueo',),
#         '4':('Facturado sin registro de dinero',),
#         '5':('Dinero para apartado y mercancia entregada',),
#         '6':('Gasto',),
#         '7':('Sin facturar',),
#         '8':('Entregar caja',)
#         }

def menu_cajaRegistro():
    opciones={
        '1':('TRANSFERENCIAS',),
        '2':('TERMINAL',),
        '3':('ARQUEO',)
    }
    generar_menu(opciones,'8')

def menu_pedido():
    opciones={
        '1':('Agregar | cambiar cantidad | Eliminar producto al pedido ',agregarProducto),
        '2':('Generar archivo', archivoPedidoPdf),
        '3':('regresar',regresar)
    }
    generar_menu(opciones,'3')

def menu_pendientes():
    opciones={
        '1':('Crear',crearPendiente),
        '2':('Listar',listar_pendientes),
        '3':('Editar',editarPendiente),
        '4':('Terminar',terminar_pendiente),
        '5':('regresar',regresar)
    }
    generar_menu(opciones,'5')

####
#Funciones
#
#####

def terminar_pendiente():
    df = pd.DataFrame()
    df = leer_pendientes()
    if df.empty:
        print("No hay pendientes.")
        return
    
    listar_pendientes()
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


def listar_pendientes():
    df = pd.DataFrame()
    df = leer_pendientes()
    if df.empty:
        print("No hay pendientes.")
        return
    
    print("\n=== LISTA DE PENDIENTES ===")
    for _, row in df.iterrows():
        # SOLO mostrar si TIENE fecha_fin (terminados) o está vacío (pendientes)
        if pd.isna(row['fecha_fin']) or row['fecha_fin'] == 'nan':
            status = "⏳ PENDIENTE"
        else:
            status = f"✅ TERMINADA el {row['fecha_fin']}"
        
        print(f"#{row['contador']} {status} | {row['membresia']} | {row['descripcion'][:50]}...")


def crearPendiente():
    df = pd.DataFrame()
    df = leer_pendientes()
    # Leer archivo existente o crear nuevo
    if os.path.exists('pendientes.csv'):
        df = pd.read_csv('pendientes.csv')
        contador = len(df) + 1  # Siguiente número
    else:
        df = pd.DataFrame()
        contador = 1
    
    print(f"\n=== NUEVA PENDIENTE #{contador} ===")
    
    # Contador (automático)
    print(f"Contador: {contador}")
    
    # Fecha de inicio (fecha actual por defecto)
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"Fecha de inicio sugerida: {fecha_actual}")
    usar_fecha_actual = input("¿Usar fecha actual? (s/n): ").lower()
    
    if usar_fecha_actual == 's':
        fecha_inicio = fecha_actual
    else:
        fecha_inicio = input("Ingresa fecha inicio (YYYY-MM-DD HH:MM): ")
    
    # Nombre o número de membresía
    membresia = input("Nombre o número de membresía: ")
    
    # Descripción
    descripcion = input("Descripción de la pendiente: ")
    
    # Crear nuevo registro
    nuevo_registro = {
        'contador': contador,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': '',  # Vacío hasta completar
        'descripcion': descripcion,
        'membresia': membresia
    }
    
    # Agregar al DataFrame
    df = pd.concat([df, pd.DataFrame([nuevo_registro])], ignore_index=True)
    
    # Guardar CSV
    df.to_csv('pendientes.csv', index=False, encoding='utf-8')
    print(f"\n✅ Pendiente #{contador} creada exitosamente!")
    
    print("\nRegistro creado:")
    print(f"Contador: {contador}")
    print(f"Fecha inicio: {fecha_inicio}")
    print(f"Membresía: {membresia}")
    print(f"Descripción: {descripcion}")

    return

def editarPendiente():
    df = pd.DataFrame()
    df = leer_pendientes()
    if df.empty:
        print("No hay pendientes.")
        return
    
    listar_pendientes()
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

def guardar_pendientes(df):
    df.to_csv('pendientes.csv', index=False, encoding='utf-8')


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

def registroCaja():
    menu_caja()

def gestionPendientes():
    menu_pendientes()
    return

def buscarProducto():
    menu_busqueda()

def busquedaNombre():
    codigo_busqueda = input('Buscar: ').strip().lower()
    
    if not codigo_busqueda:
        print("Error: Búsqueda no puede estar vacía")
        return
    
    # Filtrar y ELIMINAR columna_normalizada
    resultados = df[df['columna_normalizada'].str.contains(codigo_busqueda, na=False)].copy()
    resultados = resultados.drop('columna_normalizada', axis=1)  # ← Eliminar columna
    
    if resultados.empty:
        print("No se encontraron resultados.")
    else:
        # TABLA SIN columna_normalizada
        print(tabulate(
            resultados, 
            headers='keys', 
            tablefmt='fancy_grid',
            showindex=False,  # Sin índices
            maxcolwidths=[10, 30, 15, 10]  # Ajusta según tus columnas
        ))

def busquedaPv():
    try:
        pv = int(input('PV: '))
        
        # Crear filtro
        resultado = df['PV'] % pv
        filtro = (resultado >= 0) & (resultado <= 1) & (df['PV'] >= pv) & (df['PV'] <= pv+2)
        df_f = df[filtro].sort_values(by='PV', ascending=True)
        
        # Eliminar columna_normalizada si existe
        if 'columna_normalizada' in df_f.columns:
            df_f = df_f.drop('columna_normalizada', axis=1)
        
        if df_f.empty:
            print("No se encontraron resultados.")
        else:
            # TABLA BONITA sin índices
            print(tabulate(
                df_f.reset_index(drop=True),  # reset_index elimina índices originales
                headers='keys',
                tablefmt='fancy_grid',
                showindex=False,  # Sin columna de índices
                floatfmt=".2f"
            ))
            
    except ValueError:
        print("Error: Ingresa un número válido para PV")

def crearPedido():
    verPedido()
    menu_pedido()


def listarProductos():
    datos=pd.read_csv('inventario.csv',encoding='latin-1')
    for index, row in datos.iterrows():
        print(f"\nRegistro actual: ")
        print(f"codigo: {row['codigo']}")
        print(f"nombre: {row['Nombre']}")
        print(f"cantidad sistema: {row['enSistema']}")
        print(f"cantidad fisico: {row['fisico']}")

        editar=int(input("¿Editar cantidad? (si=1/no=2): "))
        if editar == 1:
            try:
                cantidad1=int(input("cantidad en sistema: "))
                datos.at[index, 'enSistema']=cantidad1
                cantidad2=int(input("cantidad en fisico: "))
                datos.at[index, 'fisico']=cantidad2
            except ValueError:
                print("valor no valido")
        
        continuar=input("cerrar el archivo si=1/no=2: \n")
        if continuar!= '2':
            break
    datos.to_csv('inventario.csv', index=False)
    print("\n cambios guardados")

def verPedido():
    if not pedido:
        print("No hay pedidos.")
        return
    
    # Crear lista de datos para la tabla
    datos_tabla = []
    total = 0.0
    pv_total = 0.0
    
    for codigo, item in sorted(pedido.items()):
        subtotal = item['SUBTOTAL']
        pvi = item['PV']
        cantidad = item['CANTIDAD']
        
        # Agregar fila a la tabla
        datos_tabla.append([
            codigo,
            item['NOMBRE'],
            f"${item['PRECIOSOCIO']:.2f}",
            cantidad,
            pvi,
            f"${subtotal:.2f}"
        ])
        
        total += subtotal
        pv_total += pvi * cantidad
    
    # Headers de la tabla
    headers = ["Código", "Nombre", "Precio Socio", "Cantidad", "PV", "Subtotal"]
    
    # MOSTRAR TABLA BONITA
    print(tabulate(datos_tabla, headers=headers, tablefmt='psql', floatfmt=".2f"))
    
    # Totales
    print(f"\n{'='*50}")
    print(f"TOTAL: ${total:.2f}")
    print(f"PV TOTALES: ${pv_total:.2f}")
    print(f"{'='*50}")

def salir():
    print('Saliendo')

def regresar():
    menu_principal()

def agregarProducto():
    codigo=input('Coigo: ').strip()
    resultados=df[df['CODIGO'].str.contains(codigo.upper())]
    
      # 3. Verificar si se encontró exactamente UN producto

    if resultados.empty and not codigo:
        print(f"Producto con código {codigo} no encontrado.")
        return
    elif len(resultados) > 1 or len(resultados) < 1:
        # Esto nunca debería pasar si los códigos son únicos, pero es buena práctica
        print(f"Error: Múltiples productos encontrados para el código {codigo}.")
        return
    
    del resultados['columna_normalizada']
    
    cantidad=int(input('Cantidad: '))

    if cantidad < 1 and not pedido:
        print("El pedido está vacío. Ingresa una cantidad mayor a 0 para empezar un nuevo pedido.")
        return

    fila = resultados.iloc[0]

 
    codigo = fila['CODIGO']
    nombre = fila['NOMBRE']
    precio = fila['PRECIOSOCIO']
    pv = fila['PV']
    subtotal=precio*cantidad

    if codigo in pedido:
        if cantidad > 0:
            pedido[codigo]['CANTIDAD']=cantidad
            pedido[codigo]['SUBTOTAL']=subtotal
        else:
            del pedido[codigo]
            print(f"'{codigo}' eliminado del pedido (cantidad 0).")
            verPedido()
            return 
    else:
        if cantidad < 1:
            print("El pedido está vacío. Ingresa una cantidad mayor a 0 para empezar un nuevo pedido.")
            return
        pedido[codigo]={
            'NOMBRE': nombre,
            'PRECIOSOCIO': precio,
            'PV': pv,
            'CANTIDAD':cantidad,
            'SUBTOTAL':subtotal
        }
    print(f"'{nombre}' (Cód. {codigo}) agregado al pedido.")
    verPedido()


def archivoPedido():
    totalprecio=0.0
    totalPv=0.0
    with open('pedido.txt','w', encoding='utf-8') as f:
        f.write(f"Pedido \n")
        f.write(f"Detalle de pedido \n")
        f.write(f"| Codigo | nombre \t\t\t | cantidad | precio | subtotal | subtotal pv |\n")

        for codigo, datos in pedido.items():
            precio=datos['PRECIOSOCIO']
            cantidad=datos['CANTIDAD']
            pv=datos['PV']
            nombre=datos['NOMBRE']

            subprecio=precio*cantidad
            subpv=pv*cantidad

            totalprecio+=subprecio
            totalPv+=subpv

            f.write(f"| {codigo}  | {nombre} \t\t| {cantidad} \t | {precio} | {subprecio} | {subpv} | \n")
            
        f.write("-" * 35 + "\n")
        f.write(f"\nTOTAL PRECIO FINAL: ${totalprecio:.2f}\n")
        f.write(f"TOTAL PV FINAL: {totalPv:.2f}\n")
        f.write("-" * 35 + "\n")

        pedido.clear()


def archivoPedidoPdf():
    totalPrecio = 0.0
    totalPv=0.0

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=12)

    pdf.cell(0,10, "Pedido",  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.cell(0,10,"Detalle de pedido",  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.ln(10)

    pdf.cell(20,10, "CODIGO", border=1)
    pdf.cell(60,10, "NOMBRE", border=1)
    pdf.cell(20,10, "CANTIDAD", border=1)
    pdf.cell(20,10, "PRECIO", border=1)
    pdf.cell(20,10, "SUBTOTAL", border=1)
    pdf.cell(20,10, "SUBTOTAL PV", border=1)
    pdf.ln(10)

    for codigo, datos in sorted(pedido.items()):
        precio=datos['PRECIOSOCIO']
        cantidad=datos['CANTIDAD']
        pv =datos['PV']
        nombre=datos['NOMBRE']

        subprecio=precio*cantidad
        subpv=pv*cantidad

        totalPrecio+=subprecio
        totalPv+=subpv

        pdf.cell(20, 10, str(codigo), border=1)
        pdf.cell(60, 10, nombre, border=1)
        pdf.cell(20, 10, str(cantidad), border=1)
        pdf.cell(20, 10, f"{precio:.2f}", border=1)
        pdf.cell(30, 10, f"{subprecio:.2f}", border=1)
        pdf.cell(30, 10, f"{subpv:.2f}", border=1)
        pdf.ln(10)

    # Totales
    pdf.ln(10)
    pdf.cell(0, 10, f"TOTAL PRECIO FINAL: ${totalPrecio:.2f}", border=0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, f"TOTAL PV FINAL: {totalPv:.2f}", border=0,new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Guardar PDF
    pdf.output("ticket_pedido.pdf")

    # Limpiar pedido
    pedido.clear()

if __name__ == '__main__':
    df['columna_normalizada'] = df['NOMBRE'].apply(remover_acentos)
    menu_principal()
