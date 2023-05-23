FROM python:3.10.8

RUN pip3 install django

WORKDIR /usr/src/app

COPY . .

WORKDIR /usr/src/app/mysite

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000" ]

EXPOSE 8000

