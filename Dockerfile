FROM python:3.7
RUN mkdir /data
WORKDIR /data
ADD ./requirements.txt /data
RUN pip install -r requirements.txt
ADD . /data
CMD ["/data/manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000

