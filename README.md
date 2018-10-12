# vPostHorde Herramienta para realizar pruebas de funcionamiento y/o estrés de servicios web

## instrucciones modo grafica


```
$ main
```

## Instrucciones de uso en modo linea de comandos

Para poder ejecutar desde la linea de comandos se ejecuta el binario del ejecutable con la bandera --cli por ejemplo:

```
$ main --cli [comandos]
```

### banderas de la linea de comandos

```
-u [url]    para definir la URL a donde se va hacer el test por ejemplo -u http://localhost/get
--outfile [archivo de salida]    Define el archivo de salida de las respuestas por ejemplo --outfile respuestas.txt
-d [datos de post]    Para agregar los parametros que seran enviados por post por ejemplo --d user=admin&pass=123456
-H [datos del header]   Aqui se añaden los datos del header usando la sintaxis de headers curl ejemplo: --H {bearer:123}
--auth [authorizacion] Aqui se añaden los datos de la cabecera auth. Solo BASIC  ejemplo: --auth (usuario:contraseña)
-X [tipo]   Se añade el verbo de la peticion GET, POST, PUT, DELETE, OPTIONS, HEAD ejemplo: -X POST
--threads [numero de hilos]   Se define cuantas peticiones simultaneas se van a enviar ejemplo: --threads 100
--tiempo [segundos]   Se añade el tiempo en segundos de lo que va a durar la prueba si se deja en 0 la prueba terminara cuando acabe el numero de peticiones en ejecucuion ejemplo: --tiempo 3600
--file [archivo]    Se agrega la ruta del archivo que puede ser enviado por medio de multipart ejemplo: --file imagen.jpg 
```
