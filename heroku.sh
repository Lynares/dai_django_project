

wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh   
	heroku login
	heroku create alvarobares
	git add .
	git commit -m "Despliegue heroku"
	git push heroku master
	heroku run python manage.py syncdb --noinput
	heroku ps:scale web=1
	heroku open

