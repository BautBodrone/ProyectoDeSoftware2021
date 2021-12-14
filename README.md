# Proyecto de Software - Grupo 33

Aplicación de grupo 33 para la cátedra de Proyecto de Software de la Facultad de Informática de la U.N.L.P.

Acceso a la aplicación publica: https://grupo33.proyecto2021.linti.unlp.edu.ar/

Acceso a la aplicación privada: https://admin-grupo33.proyecto2021.linti.unlp.edu.ar/

Credenciales:

    Administrador: admin   Contraseña:123123
    
    Operario: matias Contraseña: 54321

Miembros Grupo 33

Tobias Ajenjo 
Legajo: 16286/5

Pugliese Alejo
Legajo: 14414/5

Bodrone Bautista
Legajo: 15563/3

De Lena Ignacio
Legajo: 16883/1


## Iniciar ambiente

### Requisitos

- python3
- virtualenv

### Ejecución 

```bash
$ virtualenv -p python3 venv
# Para iniciar el entorno virtual
$ source venv/bin/activate
# Instalar las dependencias dentro del entorno virtual
$ pip install -r requirements.txt
```

## Correr app localmente

Para ejecutar la app de manera local y no tener un error a la hora de manejar las url,
debemos ejecutar el siguiente comando:

```bash
FLASK_ENV=development flask shell
```

Para correr la aplicacion de manera local y que funcione el iniciar sesion con google, deberemos 
correr el programa con el siguiente codigo:

$ flask run --cert=adhoc

Esto para poder correr localmente en https y asi funciona correctamente iniciar sesion con google, caso 
contrario se podra correr con:

$ flask run 

Pero a la hora de iniciar sesion con google causara el error SSL_ERROR_RX_RECORD_TOO_LONG.


Para salir del entorno virutal, ejecutar:

```bash
$ deactivate
```

## Servidor de la catedra

En caso de correrlo en el servidor de la facultad estara el env con la configuracion de development

```bash
FLASK_ENV=production flask shell
```

## Base de datos del programa

Si se crea la venv se debe crear un archivo .env para declarar los datos de nuestra base de datos, ej:

DB_HOST=localhost
DB_USER=Ejemplo
DB_PASS=1234
DB_NAME=ejemplo

Sino en el archivo config.py se puede modificar en la parte de development, los datos de la base de datos 
igual al ejemplo de arriba.


## Estructura de carpetas del proyecto

```bash
config            # Módulo de donde se obtienen las variables de configuración
helpers           # Módulo donde se colocan funciones auxiliares para varias partes del código
models            # Módulo con la lógica de negocio de la aplicación y la conexión a la base de datos
resources         # Módulo con los controladores de la aplicación (parte web)
templates         # Módulo con los templates
db.py             # Instancia de base de datos
__init__.py       # Instancia de la aplicación y ruteo
schema		      # Modulo de manejo de las API
web		          # Modulo de app publica con vue

```