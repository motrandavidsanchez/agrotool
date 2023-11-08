# Agrotool Admin/Api
Proyecto Agrotool Admin/Api (Backend)

---
### Requirements tools
 - Docker
 - Docker-compose
 - Python 3.8.X
 - Git
 - Virtualenv
 - Pycharm | VScode

---
### Execute Agrotool Admin/Api

#### Clone project:
```bash
git clone git@github.com:motrandavidsanchez/agrotool.git
```
 
#### Duplicate the **env.template** file and rename it to **.env**
```bash
 cp env.template .env
```

#### Install requirements:
```bash
pip install -r requirements/local.txt
```
---
### Run API local:

##### Run: 
###### * the database docker must be running
```bash
python manage.py runserver
```
---

### Run with docker-compose:
```bash
docker-compose build
```
```bash
docker-compose up
```
---
### Migrations

#### Make migration:
```bash
cd reciclads
python manage.py makemigrations
```

#### Apply migration:
```bash
sudo docker-compose run --rm backend_api bash
cd reciclads
python manage.py migrate
```
---
#### To access the documentation
`<link>` : <http://0.0.0.0:8000/api/v1/docs>

---
#### To access the admin Django
`<link>` : <http://0.0.0.0:8000/admin>

---
### Run testing
#### Local all tests
```bash
pytest .
```
#### Local one test
```bash
pytest app/tests/test_app.py::name_test
```
#### Docker all tests
```bash
sudo docker-compose run backend_api pytest .
```
#### Docker one test
```bash
sudo docker-compose run backend_api pytest app/tests/test_app.py::name_test
```