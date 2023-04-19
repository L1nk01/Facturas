class Facturas:
  def __init__(self):
    global tarifas
    tarifas = {
      "sub200" : 5.55,
      "sub300" : 7.88,
      "sub700" : 11.46,
      "over700" : 11.68
    }

  def nuevaFactura(self, consumo):

    actual = 0
    resultado = 0
    
    while consumo > 0:
      if consumo > 700:                             # 836
        actual = consumo - 700                      # 136
        resultado += actual * tarifas["over700"]
        consumo -= actual                           # 700

      elif consumo > 300 and consumo <= 700:        # 700
        actual = consumo - 300                      # 400
        resultado += actual * tarifas["sub700"]
        consumo -= actual                           # 300

      elif consumo > 200 and consumo <= 300:        # 300
        actual = consumo - 200                      # 100
        resultado += actual * tarifas["sub300"]
        consumo -= actual                           # 200

      elif consumo <= 200:                          # 200
        actual = consumo                            # 200
        resultado += actual * tarifas["sub200"]
        consumo -= actual                           # 0

    return resultado
  
  # Fecha
  # Tarifas
  # Total
  # Emisor