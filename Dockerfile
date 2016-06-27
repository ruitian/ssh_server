FROM python:2.7

RUN mkdir /ssh
WORKDIR /ssh
COPY . /ssh

RUN chown -R www-data:www-data /ssh
RUN chown -R www-data:www-data /ssh


RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD python manage.py runserver

EXPOSE 80
