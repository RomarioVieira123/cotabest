FROM python:3.10-buster

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN python3 -m pip install --upgrade pip setuptools wheel

RUN mkdir /app

# a ordem de COPY RUN COPY foi deixada desta forma para agilizar o processo de build em ambiente de testes
# pois reutiliza os layers anterioriomente criados quando apenas são alterados os arquivos da aplicação (/app ou /config)

COPY requirements.txt /app
COPY entrypoint.sh /app/entrypoint.sh

#RUN pip install --require-hashes -r /app/requirements.txt
RUN chmod +x /app/entrypoint.sh

COPY cart /app/cart
COPY cotabest /app/cotabest
COPY product /app/product
COPY purchase /app/purchases
COPY user /app/user
COPY manage.py /app/manage.py

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["bash", "entrypoint.sh"]

LABEL maintainer="romario.lara.vieira@gmail.com"\
	  vendor=RomarioVieira \
	  app-group-id=inovageek \
	  app-artifact-id=api-django-test \
  	  app-artifact-version=1.0.0-rc7 \
  	  gunicorn-version=20.1.0