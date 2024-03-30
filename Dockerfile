FROM surnet/alpine-wkhtmltopdf:3.16.2-0.12.6-full as wkhtmltopdf
# Use the official Python Alpine image as the base image
FROM python:3.9-alpine3.13
LABEL maintainer="venky-web"

# Set environment variables for Python buffering
ENV PYTHONUNBUFFERED 1

# Copying requirements to the container
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
# COPY ./scripts /scripts
COPY ./app /app
WORKDIR /app
ARG DEV=false

# Expose port 8000 to the outside world
EXPOSE 8000

# Install system dependencies for wkhtmltopdf
RUN apk add --update --no-cache \
    libxrender \
    fontconfig \
    libx11-dev \
    libjpeg-turbo-dev \
    libxext \
    ttf-dejavu \
    ttf-droid \
    ttf-freefont \
    ttf-liberation \
    ttf-ubuntu-font-family \
    && rm -rf /var/cache/apk/*

# Install wkhtmltopdf
COPY --from=wkhtmltopdf /bin/wkhtmltopdf /bin/libwkhtmltox.so /bin/
# RUN apk add --update --no-cache --virtual .build-deps \
#     && wget -q -O /tmp/wkhtmltox.tar.xz "https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.alpine-3.13_x86_64.tar.xz" \
#     && tar -xJf /tmp/wkhtmltox.tar.xz -C /tmp/ \
#     && mv /tmp/wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf \
#     && rm -rf /tmp/* \
#     && apk del .build-deps

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev bash openssl libgcc libstdc++ ncurses-libs && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user
    # mkdir -p /vol/web/media && \
    # mkdir -p /vol/web/static && \
    # chown -R django-user:django-user /vol && \
    # chmod -R 755 /vol && \
    # chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER django-user

# CMD ["run.sh"]