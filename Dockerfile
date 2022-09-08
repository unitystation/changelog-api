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

RUN apk add --no-cache libpq \
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

RUN mkdir /home/website
RUN mkdir /home/website/statics
RUN mkdir /home/website/media

# I'm too dumb to make user permissions over shared volumes work
#RUN addgroup -S unitystation \
#    && adduser -S central_command -G unitystation \
#    && chown -R central_command:unitystation /src \
#    && chown -R central_command:unitystation $home
#
#USER central_command

RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]