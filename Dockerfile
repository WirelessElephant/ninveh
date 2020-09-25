FROM python:3

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "gunicorn", "-c", "config/gunicorn.conf.py", "ninveh.wsgi" ]