# Planandgo Backend Test

Aplicación para generar parejas de amigos invisibles.


## Consideraciones 

Se considera que para generar de forma aleatoria las parejas, deben de existir al menos 4 participantes.

Además a un participante no se le asignará su amigo invisible, evitando de esa forma que una pareja se realizen regalos entre sí.

Al finalizar la asignación aletoria de parejas, al quedar dos participantes pendientes de asignar a un amigo invisible, se seleccionará siempre al participante que no es amigo invisible de nadie, ya que si se
selecciona al pariticipante que ya es amigo invisible, nos quedará un participante por asignar sin pareja.

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

Para introducir un miembro, enviar por post  

{'name': nombre_usuario
 'email': email_usuario }

```
[POST] api/v1/member/create 
``` 

Para generar las parejas.

```
[POST] api/v1/member/randomly_assigning 
``` 

Para obtener la pareja asignada

```
[GET] api/v1/member/<id>/assigned_member
``` 