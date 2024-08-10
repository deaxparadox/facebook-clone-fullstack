FROM python:3.12-alpine

WORKDIR /app/backend

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "sh", "run.sh" ]