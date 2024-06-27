# pull official base image
FROM python:3.12-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create Django directory for the app user
ENV APP_HOME=/usr/src/app
RUN mkdir -p $APP_HOME && \
    mkdir $APP_HOME/staticfiles && \
    mkdir $APP_HOME/mediafiles

# create the app user
RUN addgroup -S app && adduser -S app -G app

# set work directory
WORKDIR $APP_HOME

RUN apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev libpq && \
    pip install --upgrade pip && \
    pip install uv

ENV VIRTUAL_ENV=/usr/local

# install dependencies
COPY ./requirements.txt .

RUN pip install -r requirements.txt

# copy entrypoint shell file
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint shell file
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]