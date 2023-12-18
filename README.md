# Django-template

This is a template for Django projects. It is based on the [django-on-docker](https://github.com/dsonoda/django-on-docker) & [django-account-ja](https://github.com/motoitanigaki/django-account-ja) projects.

## Usage
```
cp .env.sample .env
make init
```


## Usage
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
docker-compose exec app python manage.py startapp <app_name>
```

## License
### MIT License
Copyright (C) 2020 dsonoda ([django-on-docker](https://github.com/dsonoda/django-on-docker))  
Copyright (C) 2022 R74 ([Django-template](https://github.com/RTa-technology/Django-template))

This license as follows:  
https://opensource.org/licenses/MIT

## Acknowledgments
- [django-on-docker](https://github.com/dsonoda/django-on-docker)
- [django-account-ja](https://github.com/motoitanigaki/django-account-ja)
