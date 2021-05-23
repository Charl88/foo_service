FROM python:3.6-slim
RUN mkdir /foo

COPY src/* /foo/
COPY config.yml /foo/
COPY requirements/prod.txt /foo/requirements.txt

WORKDIR /foo
RUN pip install -r requirements.txt
CMD ["nameko", "run", "--config", "config.yml", "foo"]
