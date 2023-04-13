class Facturas:
  def __init__(self):
    # self.empresa = empresa
    # self.fecha = fecha
    # self.tipoPropiedad = tipoPropiedad
    self.tarifas = {
      100 : 703.61,
      200 : 1446.29,
      300 : 2383.95,
      400 : 3810.17,
      500 : 5236.38,
      600 : 6662.59,
      700 : 8088.80,
      800 : 11714.77,
      900 : 13163.58,
      1000 : 14612.40
    }

  def nuevaFactura(self, tarifas):

    factura = int(input("¿Cuántos kWh consumió en el mes?"))
    resultado = 0

    def elementos(self):
      for key, value in self.tarifas.items():
          yield value

    while factura > 0:
      elementos()
      
      factura -= 100
  # Fecha
  # Tarifas
  # Total
  # Emisor