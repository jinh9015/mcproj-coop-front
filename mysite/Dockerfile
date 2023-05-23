FROM python:3.10.8

WORKDIR /app

RUN pip3 install django

COPY mysite /app/mysite

WORKDIR /app/mysite

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000" ]

EXPOSE 8000
