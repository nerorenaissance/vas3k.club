FROM python:3.8-slim-buster

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get dist-upgrade -y \
    && apt-get install --no-install-recommends -yq \
      gcc \
      libc-dev \
      libpq-dev \
      gdal-bin \
      python3-gdal \
      libgdal-dev \
      make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir pipenv \
    && pipenv install --dev \ 
    && pip install --no-cache-dir nltk 
  
RUN [ "python", "-c", "import nltk; nltk.download('punkt')" ]
