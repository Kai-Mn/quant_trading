FROM alpine:3.19.1

WORKDIR /app

RUN set -xe;

ADD requirements.txt .

RUN apk add --virtual build-deps gcc python3-dev musl-dev python3 py3-pip mariadb-dev tini python3-tkinter

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV /opt/venv
RUN python3 -m venv $VIRTUAL_ENV; 
RUN source $VIRTUAL_ENV/bin/activate;
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install -r requirements.txt

RUN pip install --upgrade pip setuptools-scm; \
    addgroup -g 1000 appuser; \
    adduser -u 1000 -G appuser -D -h /app appuser; \
    chown -R appuser:appuser /app

USER appuser
EXPOSE 8000/tcp

ENTRYPOINT [ "tini", "--" ]
