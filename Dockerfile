# syntax=docker/dockerfile:1
FROM python:3.10
WORKDIR /python-docker
COPY . /python-docker/
RUN pip install -r requirements.txt
ENV FLASK_APP=router.py
CMD ["python", "-m" , "flask", "run", "--host=0.0.0.0"]