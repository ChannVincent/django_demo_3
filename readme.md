# DEVLOPMENT

## install pip

curl https://bootstrap.pypa.io/get-pip.py | python3

## install virtual env

pip install virtualenv

## create virtual env

cd Desktop/
virtualenv env
(mac) python3 -m virtualenv env

## activer environnement virtuel

source env/bin/activate

## install django

pip install django

## django-admin

see all django commands

## create project

django-admin startproject django_demo

## run project

cd django_demo/
python3 manage.py runserver

## add app to the project

python3 manage.py startapp appname

# install requirements
pip install -r requirements.txt
pip freeze (créer fichier requirements)

## create and update database up to day

python3 manage.py makemigrations (new table)
python3 manage.py migrate

## site

http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/

## generate user

python3 manage.py createsuperuser
admin (ad@min.com)
admin

# PRODUCTION

source env/bin/activate

## install heroku

brew install heroku/brew/heroku
heroku login
// heroku git:remote -a vincent-demo-2 

## push to heroku

// python3 manage.py collectstatic
git push heroku main

## debug heroku

heroku logs
heroku run bash -a vincent-demo-2

## requirements

pip install -r requirements.txt
pip freeze > requirements.txt
=======
admin 

# LOG
print('logging text')
