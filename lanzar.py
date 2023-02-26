import os

def CrearArchivo(NombreArchivo):
	archivo=open(NombreArchivo, 'w')
	archivo.close()
ruta_local = os.path.dirname(os.path.abspath(__file__))

try:
	os.stat('actualizar')
except:
	os.mkdir('actualizar')
try:
	os.stat('bitmaps')
except:
	os.mkdir('bitmaps')
try:
	os.stat('data')
except:
	os.mkdir('data')
try:
	os.stat('forms')
except:
	os.mkdir('forms')
try:
	os.stat('libs')
except:
	os.mkdir('libs')
try:
	os.stat('menus')
except:
	os.mkdir('menus')
try:
	os.stat('progs')
except:
	os.mkdir('progs')
try:
	os.stat('txrx')
except:
	os.mkdir('txrx')
try:
	os.stat('reports')
except:
	os.mkdir('reports')
try:
	os.stat('ocx')
except:
	os.mkdir('ocx')

##Creo los mismos directorios en Actualizar

os.chdir(ruta_local+'\\actualizar')

try:
	os.stat('bitmaps')
except:
	os.mkdir('bitmaps')
try:
	os.stat('data')
except:
	os.mkdir('data')
try:
	os.stat('forms')
except:
	os.mkdir('forms')
try:
	os.stat('libs')
except:
	os.mkdir('libs')
try:
	os.stat('menus')
except:
	os.mkdir('menus')
try:
	os.stat('progs')
except:
	os.mkdir('progs')
try:
	os.stat('txrx')
except:
	os.mkdir('txrx')
try:
	os.stat('reports')
except:
	os.mkdir('reports')
try:
	os.stat('ocx')
except:
	os.mkdir('ocx')
	##Creo un archivo para que lista_local tenga contenido
CrearArchivo('ftp.txt')
os.chdir(ruta_local+'\\actualizar\\bitmaps')
CrearArchivo('ftp.txt')
os.chdir(ruta_local+'\\actualizar\\data')
CrearArchivo('ftp.txt')
os.chdir(ruta_local+'\\actualizar\\forms')
CrearArchivo('ftp.txt')
os.chdir(ruta_local+'\\actualizar\\libs')
CrearArchivo('ftp.txt')
os.chdir(ruta_local+'\\actualizar\\menus')
CrearArchivo('ftp.txt')
os.chdir(ruta_local+'\\actualizar\\progs')
CrearArchivo('ftp.txt')
os.chdir(ruta_local+'\\actualizar\\txrx')
CrearArchivo('ftp.txt')
os.chdir(ruta_local+'\\actualizar\\reports')
CrearArchivo('ftp.txt')
os.chdir(ruta_local+'\\actualizar\\ocx')
CrearArchivo('ftp.txt')