FROM python:3.8

ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "criptosite.wsgi:application"]