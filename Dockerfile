# python:alpine is 3.{latest}
FROM python:alpine

LABEL maintainer="Abel Coronado"

RUN pip install flask request requests pyyaml

COPY FlaskApp /src/

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
