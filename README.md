# dai_django_project
## Práctica 7


Lo primero que haremos será descargarnos *gunicorn* mediante *pip install gunicorn* y quitamos el ambiente de depuración de la aplicación cambiando en *settings.py* la variable *DEBUG = True*, por *DEBUG = False* y *ALLOWED_HOSTS = []* por *ALLOWED_HOSTS = ['**']. De esta forma:
1. Deshabilitamos el entorno de producción.
2. Permitimos todos los nombres de dominio.

Ahora nos registraremos en heroku, consiguiendo una cuenta gratuita, siguiendo los pasos que se nos indica.
