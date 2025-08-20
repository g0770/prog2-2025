import os, messages

def createFile():
  try:
    filename = input("Ingrese el nombre del archivo sin la extension a continuación: ")
    fileextension = input("Ingrese la extension del archivo (sin el punto) a continuación: ")
    with open(f'{filename}.{fileextension}', 'w') as fp:
      pass
    input('Archivo creado. Presione enter para continuar. ')
  except Exception as exc:
    input(f'{exc}. Presione enter para continuar. ')
  
def deleteFile():
  try:
    filename = input("Ingrese el nombre del archivo sin la extension a continuación: ")
    fileextension = input("Ingrese la extension del archivo (sin el punto) a continuación: ")
    os.remove(f'{filename}.{fileextension}')
    input('Archivo borrado. Presione enter para continuar. ')
  except Exception as exc:
    input(f'{exc}. Presione enter para continuar. ')

def renameFile():
  try:
    filename = input("Ingrese el nombre del archivo original sin la extension a continuación: ")
    fileextension = input("Ingrese la extension del archivo original (sin el punto) a continuación: ")
    newfilename = input("Ingrese el nombre nuevo del archivo sin la extension a continuación: ")
    newfileextension = input("Ingrese la extension nueva del archivo (sin el punto) a continuación (DEJAR EN BLANCO PARA UTILIZAR EL ANTERIOR): ")
    if newfileextension == "":
      newfileextension = fileextension
    os.rename(f'{filename}.{fileextension}',f'{newfilename}.{newfileextension}')
    input('Archivo renombrado. Presione enter para continuar. ')
  except Exception as exc:
    input(f'{exc}. Presione enter para continuar. ')

def main():
  while True:
    messages.showPathAndFiles()
    messages.optionsMenu(tipo='archivo')
    response = input('Ingrese la opción a continuación (ENTER PARA RECARGAR): ')
    if response.lower() == 'v':
      break
    elif response.lower() == 'c':
      createFile()
    elif response.lower() == 'r':
      renameFile()
    elif response.lower() == 'b':
      deleteFile()