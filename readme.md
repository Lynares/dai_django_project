Lo primero que haremos será descargarnos gunicorn mediante pip install gunicorn y quitamos el ambiente de depuración de la aplicación
cambiando en settings.py DEBUG = True, por DEBUG = False y ALLOWED_HOSTS = [] por ALLOWED_HOSTS = ['*'] 


Ahora nos registraremos en heroku, consiguiendo una cuenta gratuita, siguiendo los pasos que se nos indica.