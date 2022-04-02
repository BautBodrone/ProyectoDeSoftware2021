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

## Resultado de proyecto
Aprobado

## Iniciar ambiente

### Requisitos

- python3
- vue3
- virtualenv

### Ejecución 

```bash
$ virtualenv -p python3 venv
# Para iniciar el entorno virtual
$ source venv/bin/activate
# Instalar las dependencias dentro del entorno virtual
$ pip install -r requirements.txt
```

## Pre requisitos para empezar a utilizar la aplicación privada

Se va a necesitar tener un usuario administrador en el sistema.
Para esto podemos correr los siguientes comandos SQL en nuestra base de datos:

Creamos los roles administrador y operador:
```bash
INSERT INTO rols VALUES (1,admin),(2,operador);
```
Creamos los permisos de la aplicacion:
```bash
INSERT INTO permisos VALUES (1,'user_index','Ver pagina de usuario'),(2,'user_new','Crear nuevo usuario'),(3,'user_edit','Editar usuario'),(4,'user_delete','Eliminar usuario'),(5,'zona_index','Ver pagina de zonas'),(6,'zona_new','Crear nueva zona'),(7,'zona_edit','Editar zona'),(8,'zona_delete','Eliminar zona'), (9,'punto_index','Ver pagina de puntos'),(10,'punto_new','Crear nuevo Punto'),(11,'punto_edit','Editar punto'),(12,'punto_delete','Eliminar punto'),(13,'recorrido_index','Ver pagina de recorridos'),(14,'recorrido_new','Crear nuevo recorrido'),(15,'recorrido_edit','Editar recorrido'),(16,'recorrido_delete','Eliminar recorrido'), (17,'denuncia_index','Ver pagina de denuncia'),(18,'denuncia_new','Crear nueva denuncia'),(19,'denuncia_edit','Editar denuncia'),(20,'denuncia_delete','Eliminar denuncia');
```
Le anexamos los permisos a los roles:
```bash
INSERT INTO rols_permisos VALUES (1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(1,12),(1,13),(1,14),(1,15),(1,16),(1,17),(1,18),(1,19),(1,20),(2,1),(2,2),(2,3),(2,5),(2,6),(2,7),(2,9),(2,10),(2,11),(2,13),(2,14),(2,15),(2,17),(2,18),(2,19);
```
Creamos el usuario administrador. Donde el hash es la contraseña '123123', y una vez iniciados podemos modificarla en la seccion de usuarios:
```bash
INSERT INTO users VALUES (1,admin,admin,'email_admin@mail.com',pbkdf2:sha256:260000$I6AjJ9H7SdPMZlCX$d1e84a5061d75e1acfd295a2980f2c419f0f80992ba2494b7a1eaca1869abf26,1,admin)
```
Le asignamos el rol de administrador al usuario recien creado:
```bash
INSERT INTO users_rols VALUES (1,1);
```

Una vez ingresados los datos en la base de datos, nos podremos logear con el usuario admin y la contraseña '123123'

## Correr app localmente

Para ejecutar la app de manera local y no tener un error a la hora de manejar las url,
debemos ejecutar el siguiente comando:

```bash
$ FLASK_ENV=development python run.py
```

Para correr la aplicacion de manera local y que funcione el iniciar sesion con google, deberemos 
correr el programa con el siguiente codigo:

$ FLASK_ENV=development python run.py --cert=adhoc

Esto para poder correr localmente en https y asi funciona correctamente iniciar sesion con google, caso 
contrario a la hora de iniciar sesion con google causara el error SSL_ERROR_RX_RECORD_TOO_LONG.


Para salir del entorno virutal, ejecutar:

```bash
$ deactivate
```

## Correr la appicacion publica

Nos situamos en la carpeta de la aplicacion:

```bash
$ cd web
```
Creamos un archivo .env con setteando la variable VUE_APP_ROOT_API
con la direccion para consumir las APIs

Ejemplo:
VUE_APP_ROOT_API=http://localhost:5000/api

Instalamos y corremos la aplicación:
```bash
$ yarn install
$ yarn serve
```

En caso de correrlo en produccion:

```bash
$ yarn build
```
Antes de ejecutar yarn serve.

En el archivo .env.production está seteado la direccion
para consumir las Apis del servidor de la facultad

## Servidor de la catedra

En caso de correrlo en el servidor de la facultad estara el env con la configuracion de development

```bash
$ FLASK_ENV=production python run.py
```

## Base de datos del programa

Si se crea la venv se debe crear un archivo .env para declarar los datos de nuestra base de datos, ej:

DB_HOST=localhost
DB_USER=my_user
DB_PASS=my_password
DB_NAME=my_db_name

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
schema            # Modulo de manejo de las API
web               # Modulo de app publica con vue

```
