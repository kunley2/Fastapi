FROM python:3.9.7-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTONUNBUFFERED 1
WORKDIR /main
COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . .
EXPOSE 8008:8000
CMD ['uvicorn','main:app','--host',"0.0.0.0","--port","8000"]