FROM python:3.6-slim
RUN mkdir /foo

COPY services/* /foo
COPY config.yaml /foo
COPY requirements.txt /foo

WORKDIR /foo
RUN pip install -r requirements.txt
CMD ["nameko", "run", "--config", "config.yml", "foo"]
