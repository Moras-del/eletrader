FROM python:3.8.9


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt


# copy project
RUN mkdir -p /home/eletrader

# create the app user
RUN addgroup --system eletrader && adduser --system --group eletrader

# create the appropriate directories
ENV HOME=/home/eletrader
ENV APP_HOME=/home/eletrader/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
RUN mkdir /home/eletrader/web/staticfiles
RUN mkdir /home/eletrader/web/mediafiles

COPY . $APP_HOME
RUN chown -R eletrader:eletrader $APP_HOME
USER eletrader

