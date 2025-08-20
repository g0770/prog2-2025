import webbrowser

archivo = open('ej14.html', 'w')
archivo.write('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Programacion</title>
</head>
<body>
  <h1>Programacion</h1>
  <ul>
    <li href='Condicionales.html'>Condicionales</li>
    <li href='Bucles.html'>Bucles</li>
    <li href='Listas.html'>Listas</li>
    <li href='Funciones.html'>Funciones</li>
  </ul>
</body>
</html>
''')
archivo.close()

webbrowser.open_new(
  'ej14.html'
)