FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /usr/src/app

CMD [ "python", "miscript.py"] #es lo que hace nuestro contenedor.
