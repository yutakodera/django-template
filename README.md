# Django-template

This is a template for Django projects. It is based on the [django-on-docker](https://github.com/dsonoda/django-on-docker) & [django-account-ja](https://github.com/motoitanigaki/django-account-ja) projects.

## Usage
### Git clone
```
git clone https://github.com/RTa-technology/Django-template.git
```
----
### Development
```bash
docker-compose up -d --build
```
```bash
docker-compose exec app python manage.py flush --no-input
docker-compose exec app python manage.py makemigrations
docker-compose exec app python manage.py migrate
docker-compose exec app python manage.py collectstatic --no-input --clear
docker-compose exec app python manage.py createsuperuser
```
----
### Make a new app
```bash
python -m venv venv
```
Linux
```bash
source venv/bin/activate
```
Win
```bash
.\venv\Scripts\activate 
```
```bash
cd app
pip install -r requirements.txt
python manage.py startapp <app_name>
```

## License
Copyright (C) 2020 dsonoda ([django-on-docker](https://github.com/dsonoda/django-on-docker))  
Copyright (C) 2020 motoitanigaki ([django-account-ja](https://github.com/motoitanigaki/django-account-ja)  
Copyright (C) 2020 RTa-technology ([Django-template](https://github.com/RTa-technology/Django-template))

## Acknowledgments
- [django-on-docker](https://github.com/dsonoda/django-on-docker)
- [django-account-ja](https://github.com/motoitanigaki/django-account-ja)