FROM python:3
MAINTAINER Jan-Philippe Lavoie "janphilippelavoie@gmail.com"
COPY app /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
