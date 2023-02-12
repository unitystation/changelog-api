FROM python:3.10.6-alpine3.16

# enables proper stdout flushing
ENV PYTHONUNBUFFERED yes
# no .pyc files
ENV PYTHONDONTWRITEBYTECODE yes

# pip optimizations
ENV PIP_NO_CACHE_DIR yes
ENV PIP_DISABLE_PIP_VERSION_CHECK yes

WORKDIR /src

COPY poetry.lock pyproject.toml ./

RUN apk update && \
    apk add --no-cache libpq npm \
    && apk add --no-cache --virtual .build-deps \
    # https://cryptography.io/en/latest/installation/#alpine
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    postgresql-dev \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev \
    && apk del --purge .build-deps

COPY src .
RUN cd django_ckeditor_5/ && \
    npm install && \
    npm run prod

RUN mkdir -p /home/website/staticfiles
RUN mkdir -p /home/website/media

RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]