FROM node:20.6-alpine

WORKDIR /app/frontend

COPY . .

RUN npm install -g @angular/cli

RUN npm install

ENTRYPOINT [ "sh", "run.sh" ]