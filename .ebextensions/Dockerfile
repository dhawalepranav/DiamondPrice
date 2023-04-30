FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
RUN sudo apt update -y && sudo apt install -y
RUN sudo apt upgrade -y
CMD ["python3","app.py"]