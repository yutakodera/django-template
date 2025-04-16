# Django-template

This is a template for Django projects. It is based on the [django-on-docker](https://github.com/dsonoda/django-on-docker) projects.

## Usage
```
cp .env.sample .env
sudo make init
```


## Usage
### Development
```bash
sudo docker-compose up -d --build
```
```bash
sudo docker-compose exec app python manage.py flush --no-input
sudo docker-compose exec app python manage.py makemigrations
sudo docker-compose exec app python manage.py migrate
sudo docker-compose exec app python manage.py collectstatic --no-input --clear
sudo docker-compose exec app python manage.py createsuperuser
```
----
### Make a new app
```bash
sudo docker-compose exec app python manage.py startapp <app_name>
```

## License
### MIT License
Copyright (C) 2020 dsonoda ([django-on-docker](https://github.com/dsonoda/django-on-docker))  

This license as follows:  
https://opensource.org/licenses/MIT

## Acknowledgments
- [django-on-docker](https://github.com/dsonoda/django-on-docker)
- [djang0-template](https://github.com/r74tech/django-template)

