FROM python:3.8.9


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt


RUN mkdir -p /home/eletrader

RUN addgroup --system eletrader && adduser --system --group eletrader

RUN mkdir /home/eletrader/web
RUN mkdir /home/eletrader/web/staticfiles
RUN mkdir /home/eletrader/web/mediafiles

WORKDIR /home/eletrader/web
COPY . .
RUN chown -R eletrader:eletrader .
USER eletrader
CMD ["./docker-entrypoint.sh"]
