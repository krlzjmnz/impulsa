from connection import conectar, cerrar
from tabulate import tabulate

from fpdf import FPDF
from fpdf.enums import XPos, YPos

pedido = {}

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def salir():
    print('Saliendo...')

def menu_principal():
    opciones = {
        '1': ('buscar producto', menu_busqueda),
        '2': ('crear pedido', crearPedido),
        '3': ('Inventario', menu_inventario),
        '4': ('Pendientes', lambda: print("Módulo en construcción")),
        '5': ('Caja', lambda: print("Módulo en construcción")),
        '6': ('salir', salir)
    }
    generar_menu(opciones, '6')

def menu_busqueda():
    opciones = {
        '1': ('Por nombre', busquedaNombre),
        '2': ('Por pv', busquedaPv),
        '3': ('Regresar', menu_principal)  # Retorna de forma limpia al menú anterior
    }
    generar_menu(opciones, '3')

def menu_inventario():
    opciones={
        '1':('Existencias',menu_existencias),
        '2':('Pendientes de entrega',),
        '3':('Regresar', menu_principal)
    }
    generar_menu(opciones,4)

def menu_existencias():
    opciones={
        '1':('Consultar existencias',consultar_existencias),
        '2':('Asiganar existencia',asignar_existencia),
        '3':('Regresar',menu_principal)
    }
    generar_menu(opciones,3)

def menu_pedido():
    opciones = {
        '1': ('Agregar | cambiar cantidad | Eliminar producto al pedido', agregarProducto),
        '2': ('Generar archivo', archivoPedidoPdf),
        '3': ('Regresar', menu_principal)  # Retorna de forma limpia al menú anterior
    }
    generar_menu(opciones, '3')


def crearPedido():
    verPedido()
    menu_pedido()

def agregarProducto():
    codigo_input = input('Código: ').strip()

    if not codigo_input:
        print("Debe ingresar un código válido.")
        return

    connection = conectar()
    if connection is None:
        return

    cursor = connection.cursor(dictionary=True)

    consulta = """
        SELECT codigo, nombre, precioDistribuidor, precioMenudeo, pv
        FROM PRODUCTO
        WHERE codigo = %s
    """
    
    cursor.execute(consulta, (codigo_input,))
    producto = cursor.fetchone()

    cursor.close()
    cerrar(connection)

    if not producto:
        print("\nNo se encontró ningún producto con ese código.")
        return
    
    try:
        cantidad = int(input('Cantidad: '))
    except ValueError:
        print("Debe ingresar un número entero válido para la cantidad.")
        return

    codigo = producto['codigo']
    nombre = producto['nombre']
    
    # 💡 CONVERTIMOS A FLOAT AQUÍ para asegurar que la multiplicación sea numérica
    precioPublico = float(producto['precioMenudeo'])
    precioSocio = float(producto['precioDistribuidor'])
    pv = float(producto['pv'])
    
    subtotalPublico = precioPublico * cantidad
    subtotalSocio = precioSocio * cantidad

    global pedido

    if cantidad <= 0:
        if codigo in pedido:
            del pedido[codigo]
            print(f"'{nombre}' eliminado del pedido.")
        else:
            print("La cantidad debe ser mayor a 0.")
        verPedido()
        return

    if codigo in pedido:
        pedido[codigo]['CANTIDAD'] = cantidad
        pedido[codigo]['SUBTOTALSocio'] = subtotalSocio
        pedido[codigo]['SUBTOTALPublico'] = subtotalPublico
        print(f"'{nombre}' actualizado en el pedido.")
    else:
        pedido[codigo] = {
            'NOMBRE': nombre,
            'PRECIOSocio': precioSocio,
            'PRECIOPublico': precioPublico,
            'PV': pv,
            'CANTIDAD': cantidad,
            'SUBTOTALSocio': subtotalSocio,
            'SUBTOTALPublico': subtotalPublico
        }
        print(f"'{nombre}' (Cód. {codigo}) agregado al pedido.")
    
    verPedido()

def consultar_existencias():

    conexion = conectar()
    cursor = conexion.cursor()

    try:
        codigo = input("Ingrese el código del producto: ")

        sql = """
            SELECT
                p.id,
                p.codigo,
                p.nombre,
                e.cantidad_existencias,
                e.stock_minimo
            FROM PRODUCTO AS p
            INNER JOIN existencia AS e
                ON p.id = e.fk_producto
            WHERE p.codigo = %s
        """

        cursor.execute(sql, (codigo,))
        resultado = cursor.fetchone()

        if resultado:

            print("\n===== EXISTENCIAS DEL PRODUCTO =====")
            print(f"Código: {resultado[1]}")
            print(f"Producto: {resultado[2]}")
            print(f"Existencias: {resultado[3]}")
            print(f"Stock mínimo: {resultado[4]}")

        else:
            print("Producto sin registro de existencias o código inexistente.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conexion.close()


def asignar_existencia():

    conexion = conectar()

    if conexion is None:
        print("No fue posible conectar con MySQL.")
        return

    cursor = conexion.cursor()

    try:
        print("\n========== ASIGNAR EXISTENCIAS ==========")

        # 1. Solicitar código del producto
        codigo = input("Ingrese el código del producto: ").strip()

        if not codigo:
            print("Debe ingresar un código.")
            return

        # 2. Buscar producto
        sql_producto = """
            SELECT id, codigo, nombre
            FROM PRODUCTO
            WHERE codigo = %s
        """

        cursor.execute(sql_producto, (codigo,))
        producto = cursor.fetchone()

        if producto is None:
            print("\nEl producto no existe.")
            return

        id_producto = producto[0]
        codigo_producto = producto[1]
        nombre_producto = producto[2]

        print("\n========== PRODUCTO ENCONTRADO ==========")
        print(f"Código: {codigo_producto}")
        print(f"Nombre: {nombre_producto}")

        # 3. Consultar cantidad actual
        sql_existencia = """
            SELECT id_existencia, cantidad_existencias
            FROM existencia
            WHERE fk_producto = %s
        """

        cursor.execute(sql_existencia, (id_producto,))
        existencia = cursor.fetchone()

        # 4. Solicitar nuevas existencias
        while True:
            try:
                cantidad = int(
                    input("\n¿Cuántas unidades hay en existencia?: ")
                )

                if cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    continue

                break

            except ValueError:
                print("Ingrese una cantidad válida.")


        # 6. Mostrar operación que se realizará
        if existencia:

            print("\nEl producto ya tiene un registro de existencia.")
            print(f"Existencias anteriores: {existencia[1]}")
            print(f"Nuevas existencias: {cantidad}")

        else:

            print("\nEl producto todavía no tiene registro de existencia.")
            print(f"Existencias iniciales: {cantidad}")

        confirmar = input(
            "\n¿Desea guardar los cambios? (S/N): "
        ).strip().upper()

        if confirmar != "S":
            print("Operación cancelada.")
            return

        # 7. Actualizar o insertar
        if existencia:

            sql_actualizar = """
                UPDATE existencia
                SET cantidad_existencias = %s
                WHERE fk_producto = %s
            """

            cursor.execute(
                sql_actualizar,
                (cantidad, id_producto)
            )

            mensaje = "Existencias actualizadas correctamente."

        else:

            sql_insertar = """
                INSERT INTO existencia (
                    fk_producto,
                    cantidad_existencias
                )
                VALUES (%s, %s)
            """

            cursor.execute(
                sql_insertar,
                (id_producto, cantidad)
            )

            mensaje = "Existencias registradas correctamente."

        # 8. Confirmar transacción
        conexion.commit()

        print(f"\n{mensaje}")

    except Exception as e:
        conexion.rollback()
        print(f"Error al asignar existencias: {e}")

    finally:
        cursor.close()
        conexion.close()


def busquedaPv():
    entrada = input("Ingrese el Pv del producto: ").strip()
    if not entrada:
        print("Debe ingresar un valor de Pv válido.")
        return

    try:
        pv_val = float(entrada)
    except ValueError:
        print("El Pv debe ser un número válido.")
        return

    connection = conectar()
    if connection is None:
        return
    
    cursor = connection.cursor()
    
    consulta = """
        SELECT codigo, nombre, precioDistribuidor, precioMenudeo, pv
        FROM PRODUCTO
        WHERE pv BETWEEN %s AND %s + 1
        ORDER BY pv ASC;
    """
    
    cursor.execute(consulta, (pv_val, pv_val))
    productos = cursor.fetchall()
    
    if not productos:
        print("\nNo se encontraron productos en ese rango de Pv.")
    else:
        print(tabulate(
            productos, 
            headers=["Codigo", "Nombre", "Precio socio", "Precio público", "PV"], 
            tablefmt='fancy_grid',
            showindex=False,
            maxcolwidths=[10, 30, 15, 10]
        ))
    
    cursor.close()
    cerrar(connection)
    

def busquedaNombre():
    nombre = input("Ingrese el nombre o parte del nombre del producto: ").strip()

    if not nombre:
        print("Debe ingresar un nombre válido.")
        return

    connection = conectar()
    if connection is None:
        return

    cursor = connection.cursor()

    consulta = """
        SELECT codigo, nombre, precioDistribuidor, precioMenudeo, pv
        FROM PRODUCTO
        WHERE nombre LIKE %s
        ORDER BY pv ASC
    """

    parametro = f"%{nombre}%"

    cursor.execute(consulta, (parametro,))
    productos = cursor.fetchall()

    if not productos:
        print("\nNo se encontraron productos con ese nombre.")
    else:
        print(tabulate(
            productos, 
            headers=["Codigo", "Nombre", "Precio socio", "Precio público", "PV"], 
            tablefmt='fancy_grid',
            showindex=False,
            maxcolwidths=[10, 30, 15, 10]
        ))

    cursor.close()
    cerrar(connection)


def verPedido():
    global pedido
    
    if not pedido:
        print("\nNo hay productos en el pedido.")
        return
    
    datos_tabla = []
    totalSocio = 0.0
    totalPublico = 0.0
    pv_total = 0.0
    
    for codigo, item in sorted(pedido.items()):
        subtotalSocio = item.get('SUBTOTALSocio', 0.0)
        subtotalPublico = item.get('SUBTOTALPublico', 0.0)
        
        pvi = float(item.get('PV', 0.0))
        cantidad = int(item.get('CANTIDAD', 0))
        
        preciosocio = item.get('PRECIOSocio', 0.0)
        preciopublico = item.get('PRECIOPublico', 0.0)

        datos_tabla.append([
            codigo,
            item['NOMBRE'],
            f"${preciosocio:.2f}",
            f"${preciopublico:.2f}",
            cantidad,
            pvi,
            f"${subtotalSocio:.2f}",
            f"${subtotalPublico:.2f}"
        ])
        
        totalSocio += subtotalSocio
        totalPublico += subtotalPublico
        pv_total += pvi * cantidad
    
    headers = ["Código", "Nombre", "Precio Socio", "Precio Publico", "Cantidad", "PV", "Subtotal Socio", "SubTotal Publico"]
    
    print("\n" + "="*20 + " RESUMEN DEL PEDIDO " + "="*20)
    print(tabulate(datos_tabla, headers=headers, tablefmt='psql'))
    
    print(f"\n{'='*50}")
    print(f"TOTAL SOCIO: ${totalSocio:.2f}")
    print(f"TOTAL PÚBLICO: ${totalPublico:.2f}")
    print(f"PV TOTALES: {pv_total:.2f}")
    print(f"{'='*50}\n")


def archivoPedidoPdf():
    global pedido

    if not pedido:
        print("Awan ti laman ti pedido tapno maiprint a PDF.")
        return

    totalPrecio = 0.0
    totalPv = 0.0

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=10)

    # Titulo
    pdf.set_font("helvetica", style="B", size=14)
    pdf.cell(0, 10, "PEDIDO", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.set_font("helvetica", size=11)
    pdf.cell(
        0,
        8,
        "Detalle del Pedido",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
        align="C",
    )
    pdf.ln(5)

    # Cabecera ti Tabla (Ancho total: 180)
    pdf.set_font("helvetica", style="B", size=9)
    pdf.cell(20, 8, "CODIGO", border=1, align="C")
    pdf.cell(60, 8, "NOMBRE", border=1, align="C")
    pdf.cell(20, 8, "CANTIDAD", border=1, align="C")
    pdf.cell(20, 8, "PRECIO", border=1, align="C")
    pdf.cell(30, 8, "SUBTOTAL", border=1, align="C")
    pdf.cell(30, 8, "SUBTOTAL PV", border=1, align="C")
    pdf.ln(8)

    # Laman ti Tabla
    pdf.set_font("helvetica", size=9)

    for codigo, datos in sorted(pedido.items()):
        # Siguraduen a numero amin tapno awan ti error ti karkulo
        precio = float(datos.get("PRECIOSocio", datos.get("PRECIO", 0.0)))
        cantidad = int(datos.get("CANTIDAD", 0))
        pv = float(datos.get("PV", 0.0))
        nombre = str(datos.get("NOMBRE", ""))

        subprecio = precio * cantidad
        subpv = pv * cantidad

        totalPrecio += subprecio
        totalPv += subpv

        pdf.cell(20, 8, str(codigo), border=1)
        pdf.cell(60, 8, nombre[:30], border=1)  # Limitartay ti kaatiddog
        pdf.cell(20, 8, str(cantidad), border=1, align="C")
        pdf.cell(20, 8, f"${precio:.2f}", border=1, align="R")
        pdf.cell(30, 8, f"${subprecio:.2f}", border=1, align="R")
        pdf.cell(30, 8, f"{subpv:.2f}", border=1, align="R")
        pdf.ln(8)

    # Dagiti Totales
    pdf.ln(5)
    pdf.set_font("helvetica", style="B", size=11)
    pdf.cell(
        0,
        8,
        f"TOTAL PRECIO FINAL: ${totalPrecio:.2f}",
        border=0,
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )
    pdf.cell(
        0,
        8,
        f"TOTAL PV FINAL: {totalPv:.2f}",
        border=0,
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
    )

    # Mangidulin ti archivo PDF
    nombre_archivo = "ticket_basePedido.pdf"
    pdf.output(nombre_archivo)
    print(f"\nNaiprotektaran ken naidulin ti PDF kas '{nombre_archivo}'.")

    # Dalusan ti pedido
    pedido.clear()


# Bloque de ejecución principal
if __name__ == "__main__":
    menu_principal()