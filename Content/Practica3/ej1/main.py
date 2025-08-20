'''
1- Codificar en Python una función que calcule e imprima el promedio de tres calificaciones. Las
calificaciones se reciben por parámetro y el promedio debe retornarse y mostrarse en el programa
que llamó a la función.
'''

import os

def clearCmd():
  try:
    os.system('cls') 
  except:
    os.system('clear')

def promedio(notas):
  acum = 0
  cantNotas = len(notas)
  for i,_ in enumerate(notas):
    acum += _
  return (acum/cantNotas)

def reescribirNotas(notas):
  while True:
    try:
      numNota = int(input('Ingrese el numero de la nota [de 1 a 3] a editar a continuación: '))
      if numNota < 1 or numNota > 3:
        raise Exception('El numero de nota no esta en el rango permitido')
      break
    except Exception as exc:
      print(exc)
  while True:
    try:
      notatemp = int(input(f'Ingrese la nota numero {numNota} a continuación: '))
      notas[numNota-1] = notatemp
      break
    except Exception as exc:
      print(f'El valor ingresado no es correcto: {exc}')
  return notas


notas = []
for i in range(3):
  while True:
    try:
      notatemp = int(input(f'Ingrese la nota numero {i+1} a continuación: '))
      notas.append(notatemp)
      break
    except Exception as exc:
      print(f'El valor ingresado no es correcto: {exc}')


while True:
  clearCmd()
  promedioActual = promedio(notas)
  print(f'''
Notas ingresadas: {notas}
Promedio actual: {promedioActual}

Escriba REESCRIBIR para reescribir las notas.
Escriba SALIR para salir del programa.
''')
  response = input('Ingrese su respuesta a continuación: ')
  if response.lower() == 'salir':
    break
  elif response.lower() == 'reescribir':
    notas = reescribirNotas(notas)
