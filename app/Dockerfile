# pull official base image
FROM python:3.12

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create Django directory for the app user
ENV APP_HOME=/usr/src/app
RUN mkdir -p $APP_HOME && \
    mkdir $APP_HOME/staticfiles && \
    mkdir $APP_HOME/mediafiles

# create the app user
RUN groupadd -r app && useradd -r -g app app

# set work directory
WORKDIR $APP_HOME

# install system dependencies for PostgreSQL and Python libraries
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    netcat-openbsd postgresql-client libpq-dev gcc python3-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

# upgrade pip and install uv
RUN pip install --upgrade pip && \
    pip install uv

# install dependencies
COPY ./requirements.txt .

RUN uv pip install --system -r requirements.txt

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
