'''Escriba un programa que lea de un fichero CSV con dos filas 
EDAD 
Frecuencia Maxima Cardiaca

Calcular:
1- frecuencia cardiaca media,  
2-  frecuencia cardiaca maxima y la frecuencia cardiaca media,  para pacientes de mas de 31 años

Guardar los resultadoados en resultadoados.txt'''

def promedioCardiaco(datos):
  prom = 0
  acum = 0
  promMayor = 0
  acumMayor = 0
  for i in datos:
    if i[0] > 31:
      acumMayor += i[1]
      promMayor += 1
    acum += i[1]
    prom += 1
  prom = acum/prom
  promMayor = acumMayor/promMayor
  return prom, promMayor

def mayorCardiaco(datos):
  mayor = 0
  for i in datos:
    if i[1] > mayor and i[1] > 31:
      mayor = i[1]
  return mayor

def leerDatos():
  info = []
  archivo = open('cardiaco.csv','r')
  for linea,_ in enumerate(archivo):
    if linea != 0:
      info.append(_.strip().split(','))
      for i,_ in enumerate(info[len(info)-1]):
        info[len(info)-1][i] = int(_)
  archivo.close()
  return info

response, resultado = "", ""
while True:
  print(f'''{resultado}
  [C] Cargar información
  [E] Exportar información
  [S] Salir
  ''')
  response = input('Ingrese la opción a continuación: ')
  response = response.lower()
  try:
    if response == 'c':
      info = leerDatos()
      promedio, promedioMayorA31 = promedioCardiaco(info)
      mayor = mayorCardiaco(info)
      resultado = f'''
      Promedio Frecuencia Cardiaca: {promedio}
      Mayor Frecuencia Cardiaca: {mayor}
      Promedio de mayores a 31 Frecuencia Maxima Cardiaca: {promedioMayorA31}
      '''
    elif response == 'e':
      resultadoados = open('resultadoados.txt', 'w')
      resultadoados.write(resultado)
      resultadoados.close()
    elif response == 's':
      break
  except Exception as e:
    print(f'Error: {e}')
    input('Presione enter para continuar. ')
    resultado = ''
  finally:
    response = ""


