import os, messages

def move(path:str):
  try:
      os.chdir(path)
      os.chroot(path)
  except Exception as exc:
      print("Incapaz de ir a la carpeta. ({exc})".format(exc = exc))

def back():
   while True:
      try:
        x = input('Ingrese la cantidad de carpetas que quiere volver (DEFAULT 1): ')
        if x == '':
           x = 1
        else:
           x = int(x)
        break
      except Exception as exc:
        print("Incapaz de volver esa cantidad. ({exc})".format(exc = exc))
   for i in range(x):
      try:
         os.chdir('..')
      except:
        break

def createDir():
  try:
    dirname = input("Ingrese el nombre del directorio a continuación: ")
    os.mkdir(f'{dirname}')
    #if os.path.isdir({dirname}):
    #  raise Exception('[DEV] El directorio ya existe.') #ESTO IRIA SI LA EXCEPCION NO SE MANEJARA SOLA
    input('Directorio creado. Presione enter para continuar. ')
  except Exception as exc:
    input(f'{exc}. Presione enter para continuar. ')
  
def deleteDir():
  try:
    dirname = input("Ingrese el nombre del directorio a continuación: ")
    os.rmdir(f'{dirname}')
    input('Directorio borrado. Presione enter para continuar. ')
  except Exception as exc:
    print()
    input(f'{exc}. Presione enter para continuar. ')

def renameDir():
  try:
    dirname = input("Ingrese el nombre del directorio original a continuación: ")
    newdirname = input("Ingrese el nombre nuevo del directorio a continuación: ")
    os.rename(f'{dirname}',f'{newdirname}')
    input('Directorio renombrado. Presione enter para continuar. ')
  except Exception as exc:
    input(f'{exc}. Presione enter para continuar. ')

def main():
  while True:
    messages.showPathAndFiles()
    messages.optionsMenu(tipo='directorio')
    response = input('Ingrese la opción a continuación (ENTER PARA RECARGAR): ')
    if response.lower() == 'v':
      break
    elif response.lower() == 'c':
      createDir()
    elif response.lower() == 'r':
      renameDir()
    elif response.lower() == 'b':
      deleteDir()