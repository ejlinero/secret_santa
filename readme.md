# Planandgo Backend Test

Aplicación para generar parejas de amigos invisibles.


## Consideraciones 

Se considera que para generar de forma aleatoria las parejas, debe de existir al menos 4 componenetes.

Además un participante no podrá ser asignado al mismo participante que él tiene asignado.


## Asignación Aleatoria

La Asignación Aleatoria se hace a petición de los usarios, desde la url api/v1/member/randomly_assigning.

Cada vez que se ejecute, se eliminará las parejas que hubiese asignado con anterioridad y se crearan parejas nuevas.


## Instalación

Clonar el repositorio

```
./manage.py test apps.members
```

Instalar los paquetes

```
pip install -r requirements
```


Crear la base de datos.

```
./manage.py makemigrations
./manage.py migrate
```

## Ejecutar los test

Desde el directorio de trabajo puedes ejecutar el siguiente comando para comprobar 19 test.

```
./manage.py test apps.members
```

## Endpoints

Para introducir un miembro enviar por post  

{'name': nombre_usuario
 'email': email_usuario }

```
[POST] api/v1/member/create 
``` 

Para generar la parejas.

```
[POST] api/v1/member/randomly_assigning 
``` 

Para obtener la pareja asignada

```
[GET] api/v1/member/<id>/assigned_member
``` 