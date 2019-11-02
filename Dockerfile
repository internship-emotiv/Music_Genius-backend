FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /musicgenius
WORKDIR /musicgenius
COPY requirements.txt /musicgenius/
RUN pip install -r requirements.txt
COPY . /musicgenius/