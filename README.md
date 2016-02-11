# dai_django_project
## Práctica 7, explicación despliegue en Heroku

Lo primero que haremos será descargarnos *gunicorn* mediante *pip install gunicorn* y quitamos el ambiente de depuración de la aplicación cambiando en *settings.py* la variable *DEBUG = True*, por *DEBUG = False* y *ALLOWED_HOSTS = []* por *ALLOWED_HOSTS = ['**']. De esta forma hemos conseguido:


1. Deshabilitar el entorno de producción.

2. Permitir todos los nombres de dominio.


Ahora nos registraremos en *heroku*, consiguiendo una cuenta gratuita, siguiendo los pasos que se nos indica.
Para usar heroku necesitaremos usar *git*, en mi caso ya tengo creada la cuenta en *github* por lo que no será necesario ningún paso extra.

Una vez realizados estos pasos tendremos que crear un *script* al que llamaremos *heroku.sh* en el cual estará todo lo necesario para desplegar automaticamente nuestra aplicación en *heroku*. El script contiene lo siguiente:

  wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh

  heroku login

  heroku create alvarobares

  git add .

	git commit -m "Despliegue heroku"

	git push heroku master

	heroku run python manage.py syncdb --noinput

	heroku ps:scale web=1

	heroku open

Una vez que se ejecute este script se nos abrirá una pestaña en la cual estará nuestra aplicación corriendo, si todo ha ido bien, si no ha salido todo bien nos enlazará con la documentación de *heroku*.
