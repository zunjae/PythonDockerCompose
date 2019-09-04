FROM python:3.6-alpine

ADD requirements.txt /Project/
WORKDIR /Project
RUN pip install -r requirements.txt

COPY . /Project

# run the project
CMD ["python", "Otter.py"]