from __future__ import with_statement
from contextlib import closing
from zipfile import ZipFile, ZIP_DEFLATED
from ftplib import FTP
import shutil,time,os,configparser,fileinput,time,glob
from tqdm import tqdm
from time import gmtime, strftime
from dateutil import parser



#Variables para dato.ini
info=0
ruta_local = os.path.dirname(os.path.abspath(__file__))
src_dato=ruta_local+'\\dato.ini' #Variable para editar dato.ini
ruta_version = "public_html/actualizar"
ftp_version = FTP()
configuracion = configparser.ConfigParser()
configuracion.read(ruta_local+'\\dato.ini')
archivo='version.ini'
encabezado = configuracion['FTP']
svr= encabezado['Server']
usr= encabezado['Usuario']
pwd= encabezado['Pass']
lista_final = [] ##Resultado de la comparacion de lista_FTP y lista_local
vrs=int( encabezado['Version'])
#VARIABLES de Conexion
HOST = svr
USUARIO = usr
CLAVE = pwd
PUERTO=21

#PASO recuperio version.ini de host
vueltas=[1,2,3,4,5,6,7,8,9,10]
ftp_version= FTP(HOST, USUARIO, CLAVE)
print('Conexion Establecida, ACTUALIZANDO SISTEMA...')
ftp_version.cwd('public_html/actualizar')
filename='version.ini'
try:
   localfile=open(ruta_local+ "/version.ini", "wb")
   ftp_version.retrbinary('RETR '+ filename, localfile.write, 1024)
except Exception as e:
    print ("Error " + str(e))
localfile.close()
ftp_version.quit()

#Variables para version.ini
version = configparser.ConfigParser()
version.read(ruta_local+'\\version.ini')
encabezado2 = version['FTP']
vrs_hosting= int( encabezado2['Version2'])

def CrearArchivo(NombreArchivo):
	archivo=open(NombreArchivo, 'w')
	archivo.close()

if vrs == 0:
    print ('Creando Carpetas')
    os.system("lanzar.py ")
    time.sleep(3)
    

if vrs < vrs_hosting:


     
     #Variables Globales de configuracion     
     ruta = "public_html/actualizar/bitmaps"
     ruta_compara = ruta_local+"\\actualizar\\bitmaps\\"
     ruta2 = "bitmaps"
     ruta3 = ruta_local+"\\actualizar"
     ruta4 = ruta_local+"\\"
     destino = ruta_local+"\\actualizar\\"     
     ftp = FTP()
     
     
     #Variables globales para logs
     listaErrores = []
     numErrores = 0
     
     
     #Ruta donde se guardará un .zip de todo lo descargado
     #COPIAZIP='C:\\Users\\PC\\Documents\\Python\\FTP\\'
     
     #Metodos
     ##################################################################
     #Metodo de conexion al servidor FTP
     def conectar():
         ftp.connect(HOST, PUERTO)
         ftp.login(USUARIO, CLAVE)
         #print('Conectado al servidor')
         #print(str(ftp.welcome))
         return
     
     #Método recursivo de descarga
     def descargaRecursiva(ruta):         
         global numErrores
         #Nos movemos a la ruta en el servidor
         ftp.cwd(ruta)
         #print('En ruta: '+ruta)
         #Obtenemos una lista de string, cada string define un archivo
         listaInicial =[]
         lista_ftp=[] 
         lista_ftp2=[]         
         lista_local=[]
         lista_fechas = []
         lista_final = [] # contiene los Archivos que se descargaran desde FTP a local
         nombres_ftp=[] #lista de nombres para filtrar compara con nombres_local
         nombres_local=[]# lista de nombres para filtrar compara con nomres_ftp
         lista_falt=[] # contiene archivos que existen en FTP y no en local, se agregan a lista_final
         lista_cont=[]
         #########Obtengo Lista de archivos remotos 
         ftp.dir(listaInicial.append)  
         for line in listaInicial:
             tokens = line.split(maxsplit = 9)
             nombre_ftp = tokens[8]
             date_ftp = tokens[5] + " " + tokens[6] + " " + tokens[7]
             date_ftp = parser.parse(date_ftp)
             lista_ftp2.append(nombre_ftp + '*' + str(date_ftp))
         lista_ftp3 = [x for x in lista_ftp2 if x.startswith('.')or x.startswith('..') ] ##lista con puntos . y ..
         lista_ftp = [x for x in lista_ftp2 if x not in lista_ftp3]  # quito array con puntos de lista original         
         #print('Lista FTO:')
         #print(lista_ftp)
             #print ('LISTA SEPARADAAAAA:' + nombre_ftp + ' - ' + str(time_ftp))
        #############################################
        ##########Obtengo lista de archivos locales
         for carpeta in glob.glob(ruta_compara):
            for file in glob.glob(carpeta + '/*.*'):
                stats = os.stat(file)        
                lastmod_date = time.localtime(stats[8])        
                date_file_tuple = lastmod_date, file
                lista_fechas.append(date_file_tuple)    

         lista_fechas.sort()
         lista_fechas.reverse() 
         for file in lista_fechas:
             carpeta, nombre_local = os.path.split(file[1])    
             date_local = time.strftime("%Y-%m-%d %H:%M:%S", file[0])
             lista_local.append(nombre_local+ '*' + date_local)
         #print ('Lista local:')
         #print (lista_local)
         
         
         #####Lista Original
   
         listaIntermedia = []
         for elemento in listaInicial:
             listaIntermedia.append(str(elemento).split())
         '''
         Tras obtener en listaIntermedia el array bidimensional, generamos dos listas:
             -Una lista de pos[8] (nombres de ficheros) que cumplen que pos[0] no comienza con d
             -Una lista de pos[8] (carpetas) que cumplen que pos[0] comienza con d
         '''
         listaArchivos = []         
         listaCarpetas=[]
         for elemento in listaIntermedia:
             if elemento[0].startswith('d'):
                 listaCarpetas.append(str(elemento[8]))
             else:
                 listaArchivos.append(str(elemento[8]))
                 
         '''
         Eliminamos de la lista de carpetas . y .. para evitar bucles por el servidor
         '''
         try:
             listaCarpetas.remove('.')
             listaCarpetas.remove('..')
         except:
             pass
         '''
         Listamos los elementos a trabajar de la ruta actual
         '''
         #print('\tLista de Archivos: '+str(listaArchivos))
         
         #print('\tLista de Carpetas: '+str(listaCarpetas))
         
         '''
         Si la ruta actual no tiene su equivalente local, creamos la carpeta a nivel local
         '''
         if not os.path.exists(destino+ruta2):
             os.makedirs(destino+ruta2)
         '''
         Los elementos de la lista de archivo se proceden a descargar de forma secuencial en la ruta
         '''
         ##### Obtener lista de archivos FINAL para descargar
         if not lista_ftp:
             #print ('')
             info=1
         else:

             if not lista_local:
                 lista_local=listaArchivos #Sil las carpetas locales estan vacias                 
                
             else:
                 for i in range(len(lista_ftp)):
                     [textoA, fechaA] = lista_ftp[i].split("*")
                     for j in range(len(lista_local)):
                         [textoB, fechaB] = lista_local[j].split("*")
                         nombres_ftp.append(textoA)
                         nombres_local.append(textoB)
                         if textoA in textoB:
                             if fechaA > fechaB:
                                 lista_final.append(textoA)                  
         lista_final = list(set(lista_final))
         lista_falt= ([el for el in nombres_ftp if not any(ignore in el for ignore in nombres_local)])
         lista_falt = list(set(lista_falt))

         for i in lista_falt:
             lista_final.append(i)

         #if not lista_final:
         #        lista_final=listaArchivos #Sil las carpetas remotas estan vacias
         #print('Lista de Archivos lista Final: ')
         #print(lista_final)
         #for elemento in listaArchivos:

         '''
         contador=0
         for j in lista_final:
             contador=contador+1
             lista_cont.append(contador)         
         '''

         for elemento2 in lista_final:

             print('\t\tDescargando '+elemento2+' en '+destino+ruta2)
             try:
             	 
                 ftp.retrbinary("RETR "+elemento2, open(os.path.join(destino+ruta2,elemento2),"wb").write)
             except:
                # print('Error al descargar '+elemento2+' ubicado en '+destino+ruta2)
                 listaErrores.append('Archivo '+elemento2+' ubicado en '+destino+ruta2)
                 numErrores = numErrores+1
        
         del lista_final[:]
         del lista_ftp[:]
         del lista_local[:]
         del listaInicial[:]       
         del lista_ftp2[:]        
         del lista_local[:]
         del lista_fechas[:]        
         del nombres_ftp[:]
         del nombres_local[:]
         del lista_falt[:]
         del lista_cont[:]
     
     #Método para imprimir resultado de errores detectados y crear un log con los ficheros que dieron fallo
     def mostrarLog():
         global numErrores
         #print('##################################################################')

         with fileinput.FileInput(ruta_local+"\\logFTP.txt",inplace=True)as f:
             for line in f:
                 if f.isfirstline():
                    # print('Errores detectados = '+str(numErrores), end='\n')
                     print('Version Anterior = '+str(vrs)+ ' Ultima Version ='+str(vrs_hosting), end='\n')
                 else:
                     print(line,end='')

        
     #Main 
     
     
     mylist = [1,2,3,4,5,6,7,8,9,10]
     for i in tqdm(mylist):

         time.sleep(1)
         print('')
         
         
         if i == 2:
             ruta = "public_html/actualizar/forms"
             ruta_compara = ruta_local+"\\actualizar\\forms\\"
             ruta2 = "forms"
           
         if i == 3:
             ruta = "public_html/actualizar/libs"
             ruta_compara = ruta_local+"\\actualizar\\libs\\"
             ruta2 = "libs"
            
         if i == 4:
             ruta = "public_html/actualizar/menus"
             ruta_compara = ruta_local+"\\actualizar\\menus\\"
             ruta2 = "menus"
             
         if i == 5:
             ruta = "public_html/actualizar/progs"
             ruta_compara = ruta_local+"\\actualizar\\progs\\"
             ruta2 = "progs"
             contador=5
         if i == 6:
             ruta = "public_html/actualizar/raiz"
             ruta_compara = ruta_local+"\\"
             ruta2 = ""
             
         if i == 7:
             ruta = "public_html/actualizar/txrx"
             ruta_compara = ruta_local+"\\actualizar\\txrx\\"
             ruta2 = "txrx"
         if i == 8:
             ruta = "public_html/actualizar/data"
             ruta_compara = ruta_local+"\\actualizar\\data\\"
             ruta2 = "data"
         if i == 9:
             ruta = "public_html/actualizar/reports"
             ruta_compara = ruta_local+"\\actualizar\\reports\\"
             ruta2 = "reports"
         if i == 10:
             ruta = "public_html/actualizar/ocx"
             ruta_compara = ruta_local+"\\actualizar\\ocx\\"
             ruta2 = "ocx"
         
         conectar()
         descargaRecursiva(ruta)
         mostrarLog()
         print('')
     #comprimirYBorrar(destino)
     #Desconectamos con el servidor de forma protocolaria
         ftp.quit()
         #Aqui Conexion cerrada correctamente :
         #print('ACTUALIZANDO... ')
     
 ### En version completa los archivos se eliminan de la carpeta actulizar
     for src_dir, dirs, files in os.walk(ruta3):
            dst_dir = src_dir.replace(ruta3, ruta4, 1)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    os.remove(dst_file)
                shutil.move(src_file, dst_dir)
     

     #### Editar dato.ini
     for line in fileinput.FileInput(src_dato,inplace=1):
         if 'Version=' in line:
            # line =line.rstrip()
             line= line.replace(line,'Version='+str(vrs_hosting))
         print (line, end = '')
     
else:
    print('Fin de Actualizacion,Ejecutando Dato...')





