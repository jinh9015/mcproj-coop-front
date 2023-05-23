FROM python:3.10.8

RUN mkdir /app/mysite

WORKDIR /app/mysite

RUN pip3 install django

COPY . /app/mysite

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000" ]

EXPOSE 8000
