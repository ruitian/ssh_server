FROM python:2

RUN mkdir /ssh
WORKDIR /ssh
COPY . /ssh

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install nginx -y
RUN apt-get install uwsgi uwsgi-plugin-python -y
RUN chown -R www-data:www-data /ssh
RUN chown -R www-data:www-data /ssh

RUN chown -R +x /ssh/setup.sh
ADD default /etc/nginx/sites-available/default

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN /etc/init.d/nginx restart

CMD sh /ssh/setup.sh

EXPOSE 80
