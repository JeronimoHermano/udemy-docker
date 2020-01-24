FROM python:3.6
LABEL maintener 'jeronimohermano.nc@gmail.com'

# instução para que o python não utilize o buffer de impressão
ENV PYTHONUNBUFFERED 1
RUN pip install redis==2.10.5

ENTRYPOINT ["/usr/local/bin/python"]
