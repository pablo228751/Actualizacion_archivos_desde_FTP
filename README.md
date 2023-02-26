<h1 align="center">Actualizacion de archivos desde un servidor FTP</h1>


## Video

[![Juego](https://img.youtube.com/vi/Nvh0pDMDO3o/0.jpg)](https://www.youtube.com/watch?v=Nvh0pDMDO3o)

<p >
El código realiza la descarga y actualización de archivos de un servidor FTP en una carpeta local. A continuación, se detalla su funcionamiento.

En primer lugar, se importan varias librerías de Python necesarias para la ejecución del script, como "ZipFile" para comprimir archivos, "FTP" para establecer la conexión con el servidor FTP, "shutil" para mover archivos, "configparser" para leer archivos de configuración, "fileinput" para realizar operaciones en archivos de texto, "time" para manejar operaciones con fechas y tiempo, y "glob" para realizar búsquedas de archivos en un directorio.

Luego, se definen varias variables que se utilizan en el script, como "ruta_local" que almacena la ruta de la carpeta local donde se ejecuta el script, "src_dato" que almacena la ruta del archivo de configuración "dato.ini", "ruta_version" que almacena la ruta en el servidor FTP donde se encuentra la carpeta con los archivos a actualizar, "ftp_version" que es una instancia de la clase "FTP" para establecer la conexión con el servidor FTP, "configuracion" que es una instancia de la clase "ConfigParser" para leer el archivo de configuración "dato.ini", entre otras.

A continuación, se realiza una conexión con el servidor FTP y se descarga el archivo "version.ini" a la carpeta local. Este archivo contiene la versión actual de los archivos en el servidor FTP y se utiliza para comparar con la versión actual de los archivos en la carpeta local.

Después, se definen varias funciones, como "CrearArchivo" que crea un archivo vacío en una ruta determinada, "conectar" que establece la conexión con el servidor FTP, y "descargaRecursiva" que es el método principal que realiza la descarga de los archivos del servidor FTP a la carpeta local.

En este método, se realiza un cambio de directorio al servidor FTP a la ruta especificada en "ruta_version" y se obtiene una lista de los archivos y directorios presentes en esa carpeta del servidor FTP. Luego, se obtiene una lista de los archivos locales presentes en la carpeta "actualizar/bitmaps" de la carpeta local.

A continuación, se realiza una comparación entre las listas de archivos del servidor FTP y la lista de archivos locales para determinar cuáles archivos son necesarios descargar. Para ello, se comparan las fechas de modificación de los archivos y se descargan solo los archivos que han sido modificados en el servidor FTP después de la última descarga en la carpeta local.

Una vez que se determinan los archivos necesarios para descargar, se descargan a la carpeta local mediante el método "retrbinary" de la clase "FTP". Luego, se mueven los archivos descargados a sus respectivas carpetas en la carpeta local.

En resumen, este script permite descargar y actualizar archivos en una carpeta local desde un servidor FTP de manera automática y eficiente.

</p>
