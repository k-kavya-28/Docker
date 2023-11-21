FROM python:3

WORKDIR /user/test

COPY . .

CMD [ "python", "./app.py" ]