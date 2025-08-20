'''10- Realizar un programa usando funciones que permita administrar carpetas y archivos. De acuerdo
a la función seleccionada llamar a la función correspondiente.'''

import os, messages, files, directories, webbrowser

rutaOriginal = os.getcwd()

while True:
  messages.showPathAndFiles()
  messages.menu()
  response = input('Ingrese la opcion a continuación (ENTER PARA RECARGAR): ')
  if response.lower() == 's':
    break

  elif response.lower() == 'd':
    directories.main()
  elif response.lower() == 'a':
    files.main()

  elif response.lower() == 'm':
    directories.move(path=input('Ingrese la carpeta a la que quiere ingresar: '))
  elif response.lower() == 'v':
    directories.back()
  elif response.lower() == 'r':
    directories.move(path=rutaOriginal)

  elif response.lower() == 'easteregg':
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    break
  