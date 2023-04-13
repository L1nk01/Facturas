from Facturas import Facturas

def main():
    tarifa = int(input("Ingrese la cantidad de kWh consumidos\n"))

    facturas = Facturas()
    print(facturas.nuevaFactura(1000))

if __name__ == "__main__":
    main()