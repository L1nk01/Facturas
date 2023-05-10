from Facturas import Facturas
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from datetime import date
import sqlite3
import os

def main():

    proyecto = os.path.dirname(os.path.abspath(__file__))
    os.chdir(proyecto)
    
    facturas = Facturas()

    conn = sqlite3.connect('./facturas.db')
    cursor = conn.cursor()
    
    root = ttk.Window(themename="minty")
    root.title("Facturas")
    root.geometry("400x380")
    root.resizable(False, False)

    # Sections
    program = ttk.Frame(root)
    program.pack()
    
    # Functions
    def generarFactura():
        try:
            nombreEmisor = str(emisor.get())
        
            nombreCliente = str(cliente.get())
            cliente.delete(0, "end")
        
            consumokWh = int(consumido.get())
            consumido.delete(0, "end")
        
            precio = round(facturas.nuevaFactura(consumokWh), 3)
        
            conn.execute('''INSERT INTO listaFacturas (Emisor, Cliente, Consumo_kWh, Precio) VALUES (?, ?, ?, ?)''', (nombreEmisor, nombreCliente, consumokWh, precio))
            conn.commit()

        except ValueError:
            messagebox.showinfo(title="Error", message="Asegurate de que ingresar el tipo de dato correspondiente y de no dejar espacios vacios.")

    # Nueva ventana 
    def verFacturas():
        
        ventanaFacturas = ttk.Toplevel(pady=(10))
        ventanaFacturas.title("Lista de Facturas")
        ventanaFacturas.geometry("400x520")
        ventanaFacturas.resizable(False, False)
        
        # Nueva ventana
        def factura(event):
            
            # Widgets dentro de la ventana
            factura = ttk.Toplevel(padx=10, pady=10)
            factura.title("Factura")
            factura.geometry("250x310")
            factura.resizable(False, False)
            
            itemSeleccionado = event.widget.selection()[0]
            columnaId = event.widget.item(itemSeleccionado, "values")[0]
            
            cursor.execute(f"SELECT Fecha, Cliente, Emisor, Consumo_kWh, Precio FROM listaFacturas WHERE idFactura={columnaId}")
            datos = cursor.fetchone()
            
            titulo = ttk.Label(factura, text="FACTURA", font=("Helvetica", 20, "bold"))
            titulo.pack()
            
            fecha = ttk.Label(factura, text=datos[0], font=("Helvetica", 13))
            fecha.pack()
            
            clienteString = f"\nCliente\n{datos[1]}\n\nConsumió"
            cliente = ttk.Label(factura, text=clienteString, font=("Helvetica", 13))
            cliente.pack()
            cliente.configure(justify="center", anchor="center")
            
            consumoString = f"{datos[3]}kWh"
            consumo = ttk.Label(factura, text=consumoString, font=("Helvetica", 13, "bold"))
            consumo.pack()
            consumo.configure(justify="center", anchor="center")
            
            precioString = f"\nDebe pagar RD${datos[4]}"
            precio = ttk.Label(factura, text=precioString, font=("Helvetica", 13))
            precio.pack()
            precio.configure(justify="center", anchor="center")
            
            emisorString = f"\nFue atendido por:\n{datos[2]}\n"
            emisor = ttk.Label(factura, text=emisorString, font=("Helvetica", 13))
            emisor.pack()
            emisor.configure(justify="center", anchor="center")
        
        # Funciones
        def cargarFilas():
            cursor.execute(f"SELECT idFactura, Cliente, Fecha FROM listaFacturas")
            fila = cursor.fetchone()
        
            while fila != None:
                tabla.insert(parent="", index="end", values=(fila[0], fila[1], fila[2]))
                fila = cursor.fetchone()
                
        def recargar():
            tabla.delete(*tabla.get_children())
            cargarFilas()
            
        def actualizar():
            return
        
        def eliminar():
            return
        
        # Tabla
        tabla = ttk.Treeview(ventanaFacturas, columns=("ID", "cliente", "fecha"), bootstyle="INFO", height="20")
        
        tabla.heading("ID", text="ID", anchor="w")
        tabla.heading("cliente", text="Clientes", anchor="w")
        tabla.heading("fecha", text="Fecha", anchor="w")
        
        tabla.column("#0", width=0, stretch=False)
        tabla.column("ID", width="80")
        tabla.column("cliente", width="150")
        tabla.column("fecha", width="120") 
        
        tabla.bind("<Double-1>", factura)
        
        tabla.pack(padx=20, pady=5)
        
        cargarFilas()
        
        # Widgets dentro de la ventana
        footer = ttk.Label(ventanaFacturas, text="Haz doble clic en cualquiera de los clientes\n para visualizar su factura", justify="center")
        footer.pack(pady=(10, 10))
        
        buttonContainer = ttk.Frame(ventanaFacturas)
        buttonContainer.pack(side="bottom")
        
        recargar = ttk.Button(buttonContainer, text="Recargar", command=recargar, padding=(20, 10))
        recargar.pack(side="left", padx=(0, 5))
        
        actualizar = ttk.Button(buttonContainer, text="Actualizar", bootstyle="WARNING", command=actualizar, padding=(20, 10))
        actualizar.pack(side="left", padx=(5, 5))
        
        eliminar = ttk.Button(buttonContainer, text="Eliminar", bootstyle="SECONDARY", command=eliminar, padding=(20, 10))
        eliminar.pack(side="right", padx=(5, 0))
        
    # Widgets
    fechaActual = date.today().strftime("%d/%m/%Y")
    fecha = ttk.Label(program, text=fechaActual, font=("Helvetica", 12, "bold"), padding=(0, 15, 0, 10))
    fecha.pack()
    
    emisorTitle = ttk.Label(program, text="Ingrese su nombre *", font=("Helvetica", 12), padding=(0, 0, 0, 15))
    emisorTitle.pack()
    
    emisor = ttk.Entry(program, width="40")
    emisor.pack()
    
    clienteTitle = ttk.Label(program, text="Ingrese el nombre del cliente *", font=("Helvetica", 12), padding=(0, 15, 0, 15))
    clienteTitle.pack()
    
    cliente = ttk.Entry(program, width="40")
    cliente.pack()
    
    consumidoTitle = ttk.Label(program, text="¿Cuánto consumió el cliente? *", font=("Helvetica", 12), padding=(0, 15, 0, 15))
    consumidoTitle.pack()
    
    consumido = ttk.Entry(program, width="40")
    consumido.pack(pady=(0, 30))

    generarFactura = ttk.Button(program, text="Generar Factura", padding=(20, 10), command=generarFactura)
    generarFactura.pack(side=LEFT, padx=(0, 10))
    
    verFacturas = ttk.Button(program, text="Ver Facturas", bootstyle="INFO", padding=(30, 10), command=verFacturas)
    verFacturas.pack(side=RIGHT, padx=(10, 0))
    
    root.mainloop()
    
if __name__ == "__main__":
    main()