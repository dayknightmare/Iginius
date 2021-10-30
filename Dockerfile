FROM python:3

RUN mkdir /iginius
RUN chmod 777 -R /iginius

WORKDIR /iginius

COPY . /iginius

RUN pip install -r requirements.txt