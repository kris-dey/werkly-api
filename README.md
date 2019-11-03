# werkly-backend
User model and Jobs model contained within app

## Installation
You will need to install python3, pip3 and virtualenv to get going.

On first run you need to...
```sh
mkdir <project-name>
cd <project-name>
virtualenv venv
source venv/bin/activate
git clone https://github.com/KrishanuDey/werkly-api
cd werkly-api
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
python3 manage.py createsuperuser
```
## General Project Dev
```sh
cd <project=root-directory>
source venv/bin/activate
cd werkly-api
python3 manage.py runserver
```
