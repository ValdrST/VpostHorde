# usecad-estres Herramienta para realizar pruebas de funcionamiento y/o estrés de servicios web

## Instrucciones de uso en modo linea de comandos

Para poder ejecutar desde la linea de comandos se ejecuta el binario del ejecutable con la bandera --cli por ejemplo:

```
$ usecad-estres --cli [comandos]
```

Si no se indica --cli se iniciara en modo interfaz grafica

### banderas de la linea de comandos

```
usage: main.py [-h] [--cli] [-u [URL]] [-o [OUT_FILE]] [-d [PAYLOAD]]
               [-H [HEADERS]] [--auth [AUTH]] [-X [TYPE]] [-t [THREADS]]
               [-s [SECONDS]] [-f [FILE]]

argumentos opcionales:
  -h, --help            Ver ayuda
  --cli                 si esta activado se iniciara en modo consola usando
                        los parametros
  -u [URL], --url [URL]
                        Define la url objetivo
  -o [OUT_FILE], --out-file [OUT_FILE]
                        Se define el archivo de salida de la prueba
  -d [PAYLOAD], --payload [PAYLOAD]
                        Define el payload para cada peticion (formato Curl) [nombre]=[valor]|[nombre]=[valor]&[nombre]=[valor]&...
  -H [HEADERS], --headers [HEADERS]
                        Define las cabeceras de cada peticion
  --auth [AUTH]         Define la cabecera de autenticacion (bearer o diggest
                        o basic)[nombre]:[valor]|[nombre]:[valor],[nombre]:[valor],...
  -X [TYPE], --type [TYPE]
                        Se define el tipo de la peticion [GET|POST|PUT|DELETE|OPTIONS|HEAD]
  -t [THREADS], --threads [THREADS]
                        Se la cantidad de peticiones simultaneas activas
  -s [SECONDS], --seconds [SECONDS]
                        Se define la cantidad de segundos que durara la prueba
                        si se deja en 0 la prueba durara lo que tarden los
                        hilos especificados en ejecutares
  -f [FILE], --file [FILE]
                        Se añade la ruta del archivo que va a ser enviado por
                        multipart en cada peticion

```
