Steps to clone and run locally:

CLONE AND CHECKOUT

git clone *url*

CREATE VIRTUAL ENVIRONEMENT

python3 -m venv venv

ACTIVATE VENV

source venv/bin/activate

INSTALL DEPENDENCIES

python3 -m pip install -r requirements.txt

MAKEMIGRATIONS

python3 manage.py makemigrations

MIGRATE

python3 manage.py migrate

RUN

python3 manage.py runserver

---

TESTING INSTRUCTIONS

Coverage instructions:

pip3 install coverage

coverage --version

coverage run manage.py test

coverage report

