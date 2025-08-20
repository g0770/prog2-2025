import os

def clearCmd():
  try:
    os.system('cls') 
  except:
    os.system('clear')

def menu():
  print('''
[D] Opciones de directorios
[A] Opciones de archivos
        
[M] Moverse a carpeta
[V] Volver X carpetas atrás
[R] Volver a carpeta raíz original

[S] Salir
''')
  
def optionsMenu(tipo: str):
  print(f'''
[C] Crear {tipo}
[R] Renombrar {tipo}
[B] Borrar {tipo}
        
[V] Volver al menu anterior
''')
  
def showFiles():
  dirs = []
  files = []
  for i,_ in enumerate(os.listdir()):
    try:
      if os.path.isfile(_):
        files.append(_)
      else:
        dirs.append(_)
    except:
      pass

  dirs.sort()
  files.sort()

  dirs += files

  for i in dirs:
    if os.path.isfile(i):
      print(f'  - {i}')
    else:
      print(f' / {i}')

def showPathAndFiles():
  clearCmd()
  print(f'Ruta actual: {os.getcwd()}')
  showFiles()