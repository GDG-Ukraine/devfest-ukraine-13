APP_DIR = ./appengine_app/
SDK_DIR = /usr/local/google_appengine/
MANAGE = $(APP_DIR)manage.py
APPCFG = $(SDK_DIR)appcfg.py


deploy:
	$(APPCFG) update --oauth2 $(APP_DIR)

run:
	$(MANAGE) runserver

build:
	./build.sh $(APP_DIR)

syntax:
	pep8 $(APP_DIR)app
	pyflakes $(APP_DIR)app

sync:
	$(MANAGE) syncdb --noinput
